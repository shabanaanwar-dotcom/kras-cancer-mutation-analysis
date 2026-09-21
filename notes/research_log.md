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

## 21 September 2026 — Day 2

### What I did

- Performed sample-level KRAS mutation frequency analysis.
- Counted unique samples containing each KRAS protein change.
- Investigated samples containing multiple KRAS mutation records.
- Checked whether those samples contained multiple unique protein changes.

### Sample-level results

There were 117 unique samples.

| Protein Change | Unique Samples | Percentage |
|---|---:|---:|
| G12D | 49 | 41.88% |
| G12V | 33 | 28.21% |
| G12R | 25 | 21.37% |
| Q61H | 6 | 5.13% |
| Q61R | 2 | 1.71% |
| G12A | 1 | 0.85% |
| G13C | 1 | 0.85% |
| G12S | 1 | 0.85% |
| G12C | 1 | 0.85% |

G12D was observed in 49 of 117 unique samples (41.88%).

These percentages do not sum to 100% because some samples contain more than one KRAS protein change.

### Samples with multiple KRAS protein changes

Two samples contained multiple unique KRAS protein changes:

- `TCGA-2J-AABH-01`: G12S and G12V
- `TCGA-FB-A78T-01`: G12A and G13C

Both samples had their KRAS mutations classified as missense mutations and had a diploid copy-number status in the analyzed records.

### What I learned

- Sample-level analysis is different from mutation-record analysis.
- One sample can contain multiple KRAS mutation records.
- One sample can contain multiple unique KRAS protein changes.
- Mutation-specific sample percentages do not necessarily form a mutually exclusive distribution.
- I should not automatically treat a mutation record as equivalent to a patient or sample.
- Before interpreting biological meaning, I need to understand what the dataset actually represents.

### Scripts created

- `scripts/sample_mutation_frequency.py`
- `scripts/multiple_kras_samples.py`
- `scripts/cooccurring_kras_mutations.py`

### Next question

What are the amino-acid positions and mutation types represented in the KRAS dataset, and how are the mutations distributed across KRAS protein positions?