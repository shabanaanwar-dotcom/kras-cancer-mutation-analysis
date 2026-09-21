import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

sample_counts = df["Sample ID"].value_counts()

multiple_samples = sample_counts[sample_counts > 1]

print("Samples with multiple KRAS mutation records:")
print(multiple_samples)

print("\nDetails:")
print(
    df[df["Sample ID"].isin(multiple_samples.index)]
    [["Sample ID", "Protein Change", "Mutation Type", "Copy #"]]
    .sort_values("Sample ID")
)