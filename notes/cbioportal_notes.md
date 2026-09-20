# cBioPortal Notes

## Study Information

Study:
Pancreatic Adenocarcinoma (TCGA, PanCancer Atlas)

Study ID:
`paad_tcga_pan_can_atlas_2018`

Gene:
`KRAS`

Cancer type:
Pancreatic adenocarcinoma

---

## OncoPrint Observations

When I searched KRAS in the study:

- Total queried samples: 184
- Samples with KRAS alterations: 117
- Alteration frequency: approximately 64%

The alteration view showed:
- KRAS missense mutations
- KRAS copy-number changes such as amplification

Important:
The 64% value represents KRAS alterations. It should not automatically be described as the KRAS mutation frequency because the alteration category can include different types of genomic alterations.

---

## Mutations Tab

The Mutations tab showed:

- 119 mutation records
- KRAS protein length shown: 188 amino acids
- Mutation positions included position 12 and position 61
- Examples of protein changes:
  - G12D
  - G12V
  - G12R
  - G12C
  - G12S
  - Q61H
  - Q61R

The mutations shown were classified as missense mutations.

---

## Example Sample

Sample:

`TCGA-YH-A8SY-01`

Observed:
- KRAS G12V
- KRAS amplification

This is an example of why mutation information and copy-number information need to be considered separately.

---

## Important Observations

- The same protein change can occur in multiple samples.
- A sample can have more than one KRAS mutation record.
- Mutation records are not automatically the same as unique samples.
- 119 mutation records were later found to come from 117 unique samples.

---

## Questions From cBioPortal Exploration

- Which mutation is most common among unique samples?
- Why do some samples have two KRAS mutation records?
- What are the DNA-level changes corresponding to the protein changes?
- Are the mutations associated with specific copy-number states?