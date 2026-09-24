import pandas as pd

file_path = "data/raw/kras_mutations.tsv"

df = pd.read_csv(file_path, sep="\t")

print("Total mutation records:", len(df))

print("\nProtein changes:")
print(df["Protein Change"].value_counts())

# Calculate mutation percentages
mutation_counts = df["Protein Change"].value_counts()

mutation_percentages = (mutation_counts / len(df)) * 100

print("\nMutation percentages:")
print(mutation_percentages.round(2))

# Extract amino-acid position
df["Position"] = df["Protein Change"].str.extract(r"(\d+)").astype(int)

print("\nMutation positions:")
print(df["Position"].value_counts().sort_index())
position_counts = df["Position"].value_counts().sort_index()

position_percentages = (position_counts / len(df)) * 100

print("\nPosition percentages:")
print(position_percentages.round(2))
