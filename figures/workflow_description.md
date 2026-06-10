# Workflow Description

## DIA-PASEF Computational Proteomics Workflow

```text
DIA-PASEF / XL-MS Data
        |
        v
FASTA Database Curation
        |
        |-- Organism-specific FASTA selection
        |-- Contaminant removal
        |-- Database formatting
        |
        v
Spectral Library Generation
        |
        v
DIA-NN / XL-MSDigger Processing
        |
        |-- DIA-NN output processing
        |-- XL-MSDigger deep learning-based rescoring
        |
        v
Output Conversion
        |
        |-- .parquet to .csv
        |-- .parquet to .tsv
        |
        v
QC and Metric Validation
        |
        |-- ML scores
        |-- Q-values
        |-- FDR metrics
        |
        v
Biological Interpretation
        |
        |-- Peptide/protein-level review
        |-- Crosslinked peptide confidence
        |-- Wet-lab result integration
        |
        v
Reproducible Documentation
```

## Workflow Purpose

This workflow supports reproducible computational proteomics analysis by converting complex mass spectrometry outputs into structured, interpretable files and validating confidence metrics before downstream biological interpretation.

## Key Outputs

- Curated FASTA database documentation
- Spectral library workflow notes
- Converted DIA-NN result tables
- Q-value and FDR summaries
- QC reports
- Reproducible analysis notes
