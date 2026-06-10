# DIA-PASEF Computational Proteomics Analysis

## Overview

This project documents a computational proteomics workflow for analyzing DIA-PASEF and crosslinking mass spectrometry datasets. The workflow includes FASTA database curation, organism-specific spectral library generation, DIA-NN output processing, XL-MSDigger-based rescoring, FDR/Q-value validation, and reproducible reporting.

The project demonstrates skills in computational proteomics, mass spectrometry data analysis, biological database curation, Python automation, QC validation, and wet-lab/computational integration.

## Objective

The goal of this project was to support reproducible proteomics analysis by:

* Processing DIA-PASEF and XL-MS datasets
* Building organism-specific spectral libraries
* Curating FASTA databases
* Removing contaminants and controlling false identifications
* Validating ML scores, Q-values, and FDR metrics
* Automating DIA-NN output conversion
* Preparing organized outputs and documentation for downstream interpretation

## Background

Proteomics uses mass spectrometry to identify and quantify proteins, peptides, and protein interactions. DIA-PASEF combines data-independent acquisition with trapped ion mobility separation, generating complex datasets that require specialized computational tools for processing and interpretation.

Crosslinking mass spectrometry adds additional biological value by helping identify protein-protein interactions and structural relationships. Because these workflows generate large and complex output files, careful data processing, QC validation, and reproducible documentation are essential.

## Tools and Technologies

### Proteomics and Mass Spectrometry

* DIA-NN
* XL-MSDigger
* DIA-PASEF
* XL-MS
* DIA-MS
* Spectral library generation
* FASTA database curation
* FDR/Q-value analysis
* timsTOF data interpretation

### Programming and Workflow

* Python
* R
* Bash
* Linux/HPC
* pandas
* parquet file handling
* TSV/CSV output processing
* Git/GitHub

### Wet-Lab Connection

* Protein extraction
* SDS-PAGE
* Affinity chromatography
* Protein purification
* Sample QC

## Workflow

### 1. Dataset Organization

DIA-PASEF and crosslinking mass spectrometry outputs were organized for downstream computational processing and interpretation.

### 2. FASTA Database Curation

Organism-specific FASTA databases were curated to improve downstream analysis reliability. This included checking sequence content, removing contaminants, and preparing clean input files for spectral library generation.

### 3. Spectral Library Generation

Organism-specific spectral libraries were generated for DIA-MS and XL-MS workflows. These libraries supported peptide identification and downstream data interpretation.

### 4. XL-MSDigger Analysis

XL-MSDigger was used with deep learning-based rescoring to improve confidence in crosslinked peptide identifications.

### 5. DIA-NN Output Processing

DIA-NN output files were processed and converted from `.parquet` format into `.tsv` and `.csv` files for downstream review.

### 6. QC and Metric Validation

ML scores, Q-values, and FDR metrics were reviewed to evaluate output quality and support reliable biological interpretation.

### 7. Automation

Python scripts were used to automate repetitive post-processing steps, reducing manual processing time by approximately 50%.

### 8. Wet-Lab Integration

Computational results were connected with wet-lab workflows including protein extraction, SDS-PAGE, affinity chromatography, protein purification, and sample QC.

### 9. Documentation

Reproducible analysis notes and organized outputs were prepared for lab handoff and future proteomics experiments.

## Results

Key outcomes included:

* Processed DIA-PASEF crosslinking mass spectrometry datasets
* Used XL-MSDigger deep learning-based rescoring to improve confidence in crosslinked peptide identifications
* Built organism-specific spectral libraries
* Curated FASTA databases and removed contaminants
* Automated DIA-NN `.parquet` to `.tsv/.csv` conversion
* Validated ML scores, Q-values, and FDR metrics
* Reduced manual post-processing time by approximately 50%
* Prepared reproducible analysis documentation for lab handoff

## Key Skills Demonstrated

* Computational proteomics
* DIA-PASEF and XL-MS analysis
* DIA-NN output processing
* XL-MSDigger workflow understanding
* Spectral library generation
* FASTA database curation
* FDR and Q-value validation
* Python-based workflow automation
* Biological data interpretation
* Wet-lab and computational collaboration
* Reproducible documentation

## Repository Structure

```text
dia-pasef-proteomics-analysis/
│
├── README.md
├── data_description.md
├── requirements.txt
├── data/
│   └── example_diann_output.csv
├── notebooks/
│   └── .gitkeep
├── src/
│   ├── convert_diann_outputs.py
│   └── proteomics_qc_summary.py
├── figures/
│   └── workflow_description.md
├── results/
│   └── results_summary.md
├── reports/
│   └── project_report.md
└── LICENSE
```

## Data Privacy and Availability

Raw proteomics datasets are not included in this repository. Some mass spectrometry datasets may be lab-owned, unpublished, large, or restricted. This repository is intended to demonstrate workflow design, code templates, documentation structure, and portfolio-level project organization.

Synthetic or small example files may be included only for code demonstration.

## Limitations

This public repository does not include original lab data or unpublished research outputs. The repository focuses on reproducible workflow structure and general computational methods.

## Future Improvements

Future improvements could include:

* Packaging the workflow with Snakemake or Nextflow
* Adding automated QC report generation
* Adding visualization scripts for FDR and Q-value summaries
* Supporting additional DIA-MS tools
* Creating reusable spectral library preparation templates
* Adding dashboard-style output summaries

## Portfolio Summary

This project demonstrates my ability to process complex proteomics datasets, validate computational outputs, automate file processing, and connect mass spectrometry data analysis with biological interpretation and wet-lab workflows.

## Author

Hemalatha Ponnam
M.S. Bioinformatics & Computational Biology
Saint Louis University
Email: [hema22000latha@gmail.com](mailto:hema22000latha@gmail.com)
