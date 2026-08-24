# DIA-PASEF Computational Proteomics Analysis

## Overview

This portfolio project documents a computational proteomics workflow involving DIA-PASEF, DIA-NN output processing, crosslinking mass-spectrometry context, FASTA/spectral-library preparation, QC review, and reproducible reporting.

The **public repository is a reproducible demonstration of selected downstream post-processing and QC components**. It does not include raw mass-spectrometry data, the original lab environment, or a full public reproduction of DIA-PASEF acquisition processing, XL-MSDigger rescoring, spectral-library generation, or FASTA-curation workflows.

## Public Repository Scope

The public demo currently includes:

- conversion of DIA-NN `.parquet` output tables to CSV and TSV;
- command-line interfaces for conversion and QC summarization;
- Q-value distribution summaries exported to JSON;
- validation of required DIA-NN-style columns;
- precursor, protein-group, gene, Q-value, and quantity QC summaries;
- example/synthetic DIA-NN-style input data; and
- reproducible portfolio documentation.

The broader project context included DIA-PASEF/XL-MS datasets, FASTA curation, organism-specific spectral-library preparation, XL-MSDigger analysis, FDR/Q-value review, Linux/HPC execution, wet-lab collaboration, and automation of repetitive post-processing. Those activities are documented here as broader project experience and are not all implemented by the current public scripts.

## Data and Privacy

Raw proteomics datasets are not included because laboratory mass-spectrometry data may be large, unpublished, restricted, or lab-owned. The repository uses small example or synthetic files for software demonstration only.

Public-demo outputs should not be interpreted as biological findings or validation of a proteomics experiment.

See `data_description.md` for dataset notes.

## Technologies

### Proteomics context

- DIA-NN
- DIA-PASEF
- DIA-MS
- XL-MS / XL-MSDigger context
- FASTA database curation
- Spectral-library preparation
- FDR / Q-value review
- timsTOF workflow context

### Programming and workflow

- Python
- pandas
- parquet / CSV / TSV processing
- Linux/HPC concepts
- Git/GitHub

## Repository Structure

```text
dia-pasef-proteomics-analysis/
├── README.md
├── data_description.md
├── requirements.txt
├── data/
│   └── example_diann_output.csv
├── src/
│   ├── convert_diann_outputs.py
│   └── proteomics_qc_summary.py
├── figures/
├── results/
├── reports/
├── notebooks/
└── LICENSE
```

## How to Run the Public Demo

### 1. Clone the repository

```bash
git clone https://github.com/Hemalatha18-bio/dia-pasef-proteomics-analysis.git
cd dia-pasef-proteomics-analysis
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, use `.venv\\Scripts\\activate`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate a QC summary from the example CSV

```bash
python src/proteomics_qc_summary.py \
  --input data/example_diann_output.csv \
  --output results/proteomics_qc_summary.csv
```

This validates required columns and exports a one-row QC summary containing precursor count, unique protein groups, unique genes, Q-value thresholds, and quantity summaries.

### 5. Summarize Q-values independently

```bash
python src/convert_diann_outputs.py summarize \
  --input data/example_diann_output.csv \
  --output results/q_value_summary.json
```

### 6. Convert a DIA-NN parquet file

When you have an appropriate `.parquet` file available locally:

```bash
python src/convert_diann_outputs.py convert \
  --input path/to/report.parquet \
  --output-dir results/converted
```

The script writes both CSV and TSV versions. Raw or restricted lab files should not be committed to this public repository.

## Public Demo Outputs

Typical generated outputs are:

```text
results/proteomics_qc_summary.csv
results/q_value_summary.json
results/converted/<input_name>.csv
results/converted/<input_name>.tsv
```

These outputs are demonstrations of post-processing and QC software behavior, not experimental conclusions.

## Broader Project Context

The broader project workflow included:

1. organizing DIA-PASEF and crosslinking mass-spectrometry outputs;
2. curating organism-specific FASTA databases;
3. supporting spectral-library preparation;
4. working with XL-MSDigger and rescoring/QC concepts;
5. processing DIA-NN outputs;
6. reviewing Q-values, FDR-related metrics, and ML scores;
7. automating repetitive post-processing tasks;
8. connecting computational outputs with wet-lab protein workflows; and
9. preparing organized analysis documentation for lab handoff.

Quantitative claims from the broader project, including time-savings estimates, are intentionally **not presented as reproducible public-demo results unless the corresponding benchmark data and code are available in this repository**.

## Limitations

- The public repository does not process raw timsTOF/DIA-PASEF acquisition files.
- It does not reproduce XL-MSDigger analysis or spectral-library generation.
- It does not include original lab data or unpublished outputs.
- The example DIA-NN-style table cannot establish experimental quality or biological validity.
- QC thresholds should be interpreted in the context of the upstream analysis and study design.

## Planned Improvements

- Add automated tests and GitHub Actions CI.
- Add QC visualizations driven by generated summaries.
- Add a generic SLURM example for HPC execution.
- Add a compact Snakemake workflow for public-demo post-processing.
- Improve logging and optional-column handling.
- Add a safe template documenting FASTA/spectral-library preparation without distributing restricted resources.

## Skills Demonstrated

This repository demonstrates computational proteomics context, Python data processing, DIA-NN output handling, Q-value/QC summarization, command-line tool design, input validation, reproducibility practices, Git/GitHub organization, and familiarity with Linux/HPC proteomics workflows.

## Author

Hemalatha Ponnam  
M.S. Bioinformatics & Computational Biology  
Saint Louis University
