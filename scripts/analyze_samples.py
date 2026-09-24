import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

print("Total mutation records:", len(df))

print("Unique samples:", df["Sample ID"].nunique())

print("\nMutation records per sample:")
print(df["Sample ID"].value_counts().value_counts().sort_index())
# Find samples with more than one mutation record
multiple_mutations = df.groupby("Sample ID").size()
multiple_mutations = multiple_mutations[multiple_mutations > 1]

print("\nSamples with multiple mutation records:")
print(multiple_mutations)

# Show the actual mutations for those samples
sample_ids = multiple_mutations.index

print("\nMutation records for these samples:")
print(
    df[df["Sample ID"].isin(sample_ids)]
    [["Sample ID", "Protein Change", "Mutation Type"]]
    .sort_values("Sample ID")
)