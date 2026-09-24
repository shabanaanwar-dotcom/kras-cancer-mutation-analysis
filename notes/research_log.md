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
# Day 3 — KRAS Mutation Distribution & Sample-Level Analysis

## Objective

The goal of Day 3 was to understand the distribution of KRAS mutations in the pancreatic adenocarcinoma dataset and learn the difference between **mutation records, mutation positions, and unique samples**.

## 1. Mutation Distribution

The dataset contains **119 KRAS mutation records**.

The most frequently observed protein changes were:

| Protein Change | Mutation Records | Percentage |
| -------------- | ---------------: | ---------: |
| G12D           |               49 |     41.18% |
| G12V           |               33 |     27.73% |
| G12R           |               25 |     21.01% |
| Q61H           |                6 |      5.04% |
| Q61R           |                2 |      1.68% |
| G12A           |                1 |      0.84% |
| G13C           |                1 |      0.84% |
| G12S           |                1 |      0.84% |
| G12C           |                1 |      0.84% |

**G12D** was the most frequent specific KRAS protein change, accounting for **41.18% of mutation records**.

G12D means that the amino acid **glycine (G)** at position **12** is changed to **aspartic acid (D)**.

## 2. Mutation Position Analysis

I extracted the amino-acid position from the `Protein Change` column using Python.

The mutation positions were:

| Position | Mutation Records | Percentage |
| -------- | ---------------: | ---------: |
| 12       |              110 |     92.44% |
| 13       |                1 |      0.84% |
| 61       |                8 |      6.72% |

Position **12** was the most frequently observed mutation position, representing **92.44% of all mutation records**.

This is different from saying that 92.44% of patients have a position-12 mutation. The calculation is based on **mutation records**, not unique samples.

## 3. Mutation Records vs Unique Samples

The dataset contains:

* **119 mutation records**
* **117 unique samples**

The number of mutation records per sample was:

* 115 samples → 1 mutation record
* 2 samples → 2 mutation records

Therefore:

**115 × 1 + 2 × 2 = 119 mutation records**

This explains why there are 119 records but only 117 unique samples.

### Important lesson

A **mutation record is not the same thing as a unique sample**.

One sample can contain more than one mutation record, so counting rows does not always tell us how many samples are represented.

## 4. Samples With Multiple Mutation Records

I identified the two samples that contained more than one KRAS mutation record.

### Sample 1

`TCGA-2J-AABH-01`

Mutations:

* G12S
* G12V

Both mutations involve **position 12**.

### Sample 2

`TCGA-FB-A78T-01`

Mutations:

* G12A
* G13C

These mutations involve **positions 12 and 13**.

This showed me that having multiple mutation records in one sample does **not necessarily mean that the mutations occur at the same position**.

## 5. Biological Interpretation

KRAS is involved in intracellular signaling pathways that help regulate processes such as cell proliferation and survival.

KRAS mutations can alter normal signaling activity. Persistent or abnormal KRAS signaling can contribute to uncontrolled cellular growth and cancer development.

However, a KRAS mutation by itself should not automatically be interpreted as meaning that a sample has cancer because cancer involves multiple molecular and cellular changes.

## 6. Python Skills Practiced

During Day 3 I practiced:

* Counting mutation frequencies
* Calculating percentages
* Extracting amino-acid positions from strings
* Using `groupby()` to count records per sample
* Filtering samples with more than one mutation record
* Using `.isin()` to retrieve records belonging to selected samples
* Sorting results with `sort_values()`

## 7. Key Lessons

1. **G12D is the most frequent specific KRAS mutation in this dataset.**
2. **Position 12 accounts for 92.44% of mutation records.**
3. **119 mutation records do not mean 119 unique samples.**
4. **There are 117 unique samples.**
5. **Two samples contain two mutation records each.**
6. A sample can contain mutations at the **same or different positions**.
7. Scientific conclusions must clearly state whether percentages are calculated from **mutation records or unique samples**.

## 8. Questions for Further Analysis

* What percentage of unique samples contain a KRAS mutation?
* Which mutation is most common at the sample level?
* Are particular KRAS mutations associated with clinical variables such as tumor stage?
* How do KRAS mutation patterns compare with findings reported in published studies?
* Can the mutation distribution be visualized using a bar chart?
## 9. Data Visualization

To visualize the mutation distribution, I created two bar charts using Python and Matplotlib.

### Figure 1 — KRAS Protein Change Distribution

File:
`results/figures/kras_protein_change_distribution.png`

This chart shows the number of mutation records for each KRAS protein change.

The most frequent mutation was **G12D (49 records)**, followed by **G12V (33)** and **G12R (25)**.

### Figure 2 — KRAS Mutation Position Distribution

File:
`results/figures/kras_mutation_position_distribution.png`

This chart shows the number of mutation records at each amino-acid position.

Position **12** was the most frequently observed position, with **110 of 119 mutation records (92.44%)**.

### Visualization Lesson

Charts make it easier to identify patterns in mutation data that may be less obvious from a table alone.

I also learned that a visualization must clearly state what is being counted. In these figures, the values represent **mutation records**, not unique samples.