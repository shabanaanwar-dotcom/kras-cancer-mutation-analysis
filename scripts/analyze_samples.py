import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

print("Total mutation records:", len(df))

print("Unique samples:", df["Sample ID"].nunique())

print("\nMutation records per sample:")
print(df["Sample ID"].value_counts().value_counts().sort_index())