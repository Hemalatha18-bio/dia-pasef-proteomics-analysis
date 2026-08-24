#!/bin/bash
#SBATCH --job-name=proteomics_qc
#SBATCH --output=logs/proteomics_qc_%j.out
#SBATCH --error=logs/proteomics_qc_%j.err
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

set -euo pipefail

mkdir -p logs results figures

# Activate your environment here if required by your HPC system.
# Example: source .venv/bin/activate

python src/proteomics_qc_summary.py \
  --input data/example_diann_output.csv \
  --output results/proteomics_qc_summary.csv

python src/convert_diann_outputs.py summarize \
  --input data/example_diann_output.csv \
  --output results/q_value_summary.json

python src/visualize_qc.py \
  --input results/proteomics_qc_summary.csv \
  --output figures/qvalue_qc_summary.png
