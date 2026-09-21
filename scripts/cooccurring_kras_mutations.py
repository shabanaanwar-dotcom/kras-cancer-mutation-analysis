import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

# Find samples containing more than one KRAS mutation
mutation_counts = df.groupby("Sample ID")["Protein Change"].nunique()

multiple_mutation_samples = mutation_counts[mutation_counts > 1]

print("Samples with multiple unique KRAS protein changes:")
print(multiple_mutation_samples)

print("\nKRAS protein changes in those samples:")

for sample in multiple_mutation_samples.index:
    mutations = (
        df[df["Sample ID"] == sample]["Protein Change"]
        .drop_duplicates()
        .tolist()
    )

    print(f"{sample}: {', '.join(mutations)}")