import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

# Keep only unique sample + protein change combinations
sample_mutations = df[["Sample ID", "Protein Change"]].drop_duplicates()

# Count unique samples for each protein change
mutation_counts = sample_mutations["Protein Change"].value_counts()

# Total number of unique samples
total_samples = df["Sample ID"].nunique()

print("Total unique samples:", total_samples)

print("\nKRAS mutation frequency among unique samples:")

for mutation, count in mutation_counts.items():
    percentage = (count / total_samples) * 100
    print(f"{mutation}: {count} samples ({percentage:.2f}%)")
    df[["Sample ID", "Protein Change"]].drop_duplicates()
    