from dataclasses import dataclass

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
