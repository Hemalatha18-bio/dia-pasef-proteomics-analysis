# Project Report: DIA-PASEF Computational Proteomics Analysis

## Author
Hemalatha Ponnam

## Project Overview

This project documents a computational proteomics workflow for DIA-PASEF and crosslinking mass spectrometry data analysis. The workflow focuses on DIA-NN output processing, XL-MSDigger-based rescoring, spectral library generation, FASTA database curation, Q-value/FDR validation, and reproducible reporting.

The project was inspired by my work as a Bioinformatics Research Assistant in the Haijun Liu Lab at Saint Louis University, where I supported computational proteomics and protein biochemistry workflows.

## Background

Proteomics uses mass spectrometry to identify and quantify proteins, peptides, and protein-level interactions. DIA-PASEF combines data-independent acquisition with trapped ion mobility separation, creating rich and complex datasets that require specialized computational workflows.

Crosslinking mass spectrometry adds another layer of biological interpretation by helping identify protein-protein interactions and structural relationships. Because these workflows generate large and complex outputs, reproducible data processing, metric validation, and careful documentation are essential.

## Objective

The objective of this project was to demonstrate a reproducible computational proteomics workflow that could:

1. Organize DIA-PASEF and XL-MS outputs.
2. Curate organism-specific FASTA databases.
3. Support spectral library generation.
4. Process DIA-NN output files.
5. Convert `.parquet` outputs into `.csv` and `.tsv` formats.
6. Validate ML scores, Q-values, and FDR metrics.
7. Summarize QC metrics.
8. Prepare structured outputs for biological interpretation.

## Methods

### 1. FASTA Database Curation

Organism-specific FASTA databases were curated to improve downstream reliability. This included database review, contaminant removal, and preparation of clean sequence files for spectral library workflows.

### 2. Spectral Library Generation

Spectral libraries were generated to support DIA-MS and XL-MS analysis workflows. These libraries provided peptide and protein-level reference information for downstream interpretation.

### 3. DIA-NN Output Processing

DIA-NN output tables were processed and converted into accessible formats such as `.csv` and `.tsv`. This made the outputs easier to review, filter, validate, and share with collaborators.

### 4. XL-MSDigger-Based Analysis

XL-MSDigger deep learning-based rescoring was used to improve confidence in crosslinked peptide identifications.

### 5. Q-Value and FDR Validation

Q-values and FDR-related metrics were reviewed to evaluate confidence in peptide and protein identifications. Lower Q-values supported higher-confidence identifications.

### 6. Workflow Automation

Python scripts were used to reduce repetitive manual processing, including output conversion and QC summary generation.

### 7. Wet-Lab Integration

Computational analysis was connected with wet-lab workflows including protein extraction, SDS-PAGE, affinity chromatography, protein purification, and sample QC.

## Results

Key outcomes included:

- Processed DIA-PASEF crosslinking mass spectrometry datasets.
- Used XL-MSDigger deep learning-based rescoring to support high-confidence crosslinked peptide identification.
- Built organism-specific spectral libraries.
- Curated FASTA databases and removed contaminants.
- Automated DIA-NN `.parquet` to `.csv/.tsv` output conversion.
- Validated ML scores, Q-values, and FDR metrics.
- Reduced manual post-processing time by approximately 50%.
- Prepared reproducible documentation and organized outputs for lab handoff.

## Skills Demonstrated

This project demonstrates experience in:

- Computational proteomics
- DIA-PASEF data analysis
- Crosslinking mass spectrometry workflows
- DIA-NN output processing
- XL-MSDigger workflow understanding
- FASTA database curation
- Spectral library generation
- FDR and Q-value validation
- Python automation
- QC summary generation
- Wet-lab and computational integration
- Scientific documentation

## Limitations

This public repository does not include raw mass spectrometry data, unpublished lab outputs, or confidential project files. Instead, it uses synthetic/example data and code templates to demonstrate workflow structure and computational methods.

## Future Improvements

Future improvements could include:

- Packaging the workflow using Snakemake or Nextflow.
- Adding automated QC report generation.
- Adding visualizations for Q-value and intensity distributions.
- Adding support for additional DIA-MS tools.
- Creating reusable spectral library preparation templates.
- Building dashboard-style result summaries.

## Conclusion

This project demonstrates how computational proteomics workflows can support mass spectrometry data processing, QC validation, output conversion, and biological interpretation. It highlights my ability to work across proteomics, Python automation, wet-lab collaboration, and reproducible scientific reporting.
