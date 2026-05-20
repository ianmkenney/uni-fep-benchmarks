from dataclasses import dataclass
from random import randint
from pathlib import Path

@dataclass
class InferenceExperimentSettings:
    seeds: list[int]

    @classmethod
    def with_random_seeds(cls, num_seeds: int) -> InferenceExperimentSettings:
        seeds = [randint(0, 2**32 - 1) for _ in range(num_seeds)]
        return cls(seeds=seeds)


    def write_yaml(self, file_path: str | Path):
        file_path = Path(file_path)

        content = """
msa_computation_settings:
  msa_output_directory: ./msas/
  cleanup_msa_dir: False
  save_mappings: True
  msa_file_format: a3m

template_preprocessor_settings:
  output_directory: ./msas/

model_update:
  presets:
    - predict
    - low_mem
  custom:
    settings:
      memory:
        eval:
          use_deepspeed_evo_attention: false

"""
        content += "experiment_settings:\n"
        content += "  seeds:\n"

        for seed in self.seeds:
            content += f"    - {seed}\n"

        with open(file_path, "w") as f:
            f.write(content)

@dataclass
class Protein:
    sequence: str
    chain: str

@dataclass
class Ligand:
    smiles: str
    name: str
    exp_dG: float

@dataclass
class Benchmark:
    name: str
    protein: Protein
    ligands: list[Ligand]

    def to_openfold3_query(self):
        queries = {"queries": {}}
        inner_queries = queries["queries"]

        for lig in self.ligands:
            query_name = self.name + "|" + str(lig.name)
            inner_queries[query_name] = {
                "chains": [
                    {
                        "molecule_type": "protein",
                        "chain_ids": self.protein.chain,
                        "sequence": self.protein.sequence,
                    },
                    {
                        "molecule_type": "ligand",
                        "chain_ids": "Z",
                        "smiles": lig.smiles,
                    },
                ]
            }
        return queries
