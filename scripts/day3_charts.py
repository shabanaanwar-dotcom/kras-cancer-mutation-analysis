import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
data_path = Path("data/raw/kras_mutations.tsv")
output_dir = Path("results/figures")
output_dir.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(data_path, sep="\t")

# -----------------------------
# Chart 1: Protein Change Distribution
# -----------------------------

protein_counts = df["Protein Change"].value_counts()

plt.figure(figsize=(10, 6))
protein_counts.plot(kind="bar")

plt.title("KRAS Protein Change Distribution")
plt.xlabel("Protein Change")
plt.ylabel("Number of Mutation Records")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    output_dir / "kras_protein_change_distribution.png",
    dpi=300
)
plt.close()


# -----------------------------
# Chart 2: Mutation Position Distribution
# -----------------------------

df["Position"] = df["Protein Change"].str.extract(r"(\d+)").astype(int)

position_counts = df["Position"].value_counts().sort_index()

plt.figure(figsize=(8, 6))
position_counts.plot(kind="bar")

plt.title("KRAS Mutation Position Distribution")
plt.xlabel("Amino Acid Position")
plt.ylabel("Number of Mutation Records")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_dir / "kras_mutation_position_distribution.png",
    dpi=300
)
plt.close()

print("Day 3 charts created successfully.")
print(f"Saved to: {output_dir}")