# KRAS Research Log

## 20 September 2026 — Day 1

### What I did

- Explored KRAS in cBioPortal.
- Selected the Pancreatic Adenocarcinoma (TCGA, PanCancer Atlas) study.
- Downloaded the KRAS mutation table.
- Added the dataset to my project.
- Set up Python and Pandas.
- Inspected the dataset.
- Counted KRAS protein changes.
- Counted unique samples.

### Dataset

File:

`data/raw/kras_mutations.tsv`

Dataset size:

- 119 mutation records
- 92 columns

### First analysis

I counted the KRAS protein changes.

Results:

| Protein Change | Records |
|---|---:|
| G12D | 49 |
| G12V | 33 |
| G12R | 25 |
| Q61H | 6 |
| Q61R | 2 |
| G12A | 1 |
| G13C | 1 |
| G12S | 1 |
| G12C | 1 |

Total:

119 records.

### Sample analysis

I checked the number of unique samples.

Results:

- 119 mutation records
- 117 unique samples
- 115 samples had one mutation record
- 2 samples had two mutation records

### What I learned

- A row in a mutation table is a mutation record.
- Mutation records are not necessarily unique samples.
- One sample can have more than one mutation record.
- I need to decide whether an analysis is record-level or sample-level.
- Python and Pandas can be used to analyze cancer genomic datasets.

### Problems I encountered

- Pandas was initially not installed.
- I accidentally tried to enter Python code directly into the Windows terminal.
- I learned that Python code needs to be inside a `.py` file and then executed with Python.

### Next step

Perform sample-level KRAS mutation frequency analysis.

Question:

How many unique samples contain each KRAS protein change?