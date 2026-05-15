from .models import Ligand, Protein, Benchmark
import json
from pathlib import Path

def load_benchmarks(file_path: str | Path) -> list[Benchmark]:

    file_path = Path(file_path)
    file_content = file_path.read_text()
    json_content = json.loads(file_content)

    benchmarks = []

    for benchmark_name, benchmark_data in json_content.items():
        chain = list(benchmark_data["protein_sequence"].keys())[0]
        sequence = list(benchmark_data["protein_sequence"].values())[0]
        protein = Protein(chain=chain, sequence=sequence)

        ligands = []
        for query_ligand in benchmark_data["query_ligands"]:
            params = {
                    "smiles": query_ligand["smiles"],
                    "name": query_ligand["ligand_name"],
                    "exp_dG": query_ligand["exp_dG (kcal/mol)"],
                    }
            ligand = Ligand(**params)
            ligands.append(ligand)
        benchmark = Benchmark(name=benchmark_name, protein=protein, ligands=ligands)
        benchmarks.append(benchmark)
    return benchmarks
