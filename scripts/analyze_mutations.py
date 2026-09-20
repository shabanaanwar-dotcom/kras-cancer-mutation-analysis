import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

print("Total mutation records:", len(df))

print("\nProtein changes:")
print(df["Protein Change"].value_counts())