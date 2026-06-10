# Results Summary

## Project
DIA-PASEF Computational Proteomics Analysis

## Summary

This project documents a computational proteomics workflow for DIA-PASEF and crosslinking mass spectrometry data analysis. The workflow focuses on DIA-NN output processing, XL-MSDigger-based analysis, spectral library generation, FASTA database curation, Q-value/FDR validation, and reproducible reporting.

## Key Outcomes

- Processed DIA-PASEF crosslinking mass spectrometry datasets.
- Used XL-MSDigger deep learning-based rescoring to improve confidence in crosslinked peptide identifications.
- Built organism-specific spectral libraries for DIA-MS and XL-MS workflows.
- Curated FASTA databases and removed contaminants.
- Automated DIA-NN output conversion from `.parquet` to `.csv` and `.tsv`.
- Validated ML scores, Q-values, and FDR metrics.
- Reduced manual post-processing time by approximately 50%.
- Prepared reproducible analysis notes and organized outputs for lab handoff.

## Example QC Metrics

The example DIA-NN output summary includes:

- Total precursor entries
- Unique protein groups
- Unique genes
- Number of entries with Q.Value < 0.01
- Number of entries with Q.Value < 0.05
- Median quantity
- Mean quantity

## Example Interpretation

Q-values and FDR-related metrics are important for evaluating the confidence of peptide and protein identifications. Lower Q-values indicate higher-confidence identifications. Summarizing these metrics helps support quality control and reproducible downstream interpretation.

## Note

This repository uses synthetic/example data for public demonstration. Raw mass spectrometry data and unpublished lab outputs are not included.
