"""Generate a compact QC summary from a DIA-NN-style output table.

This public script demonstrates downstream QC summarization on example data. It is
not a replacement for DIA-NN, DIA-PASEF acquisition processing, or XL-MS analysis.
"""

import argparse
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["Protein.Group", "Genes", "Q.Value", "Quantity"]


def load_diann_output(file_path):
    """Load CSV or TSV DIA-NN-style output and validate required columns."""
    input_path = Path(file_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() == ".tsv":
        data = pd.read_csv(input_path, sep="\t")
    elif input_path.suffix.lower() == ".csv":
        data = pd.read_csv(input_path)
    else:
        raise ValueError("QC input must be a .csv or .tsv file.")

    if data.empty:
        raise ValueError("Input DIA-NN table is empty.")

    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    return data


def summarize_qc_metrics(data):
    """Summarize key demonstration QC metrics from DIA-NN-style output."""
    q_values = pd.to_numeric(data["Q.Value"], errors="coerce")
    quantity = pd.to_numeric(data["Quantity"], errors="coerce")

    if q_values.notna().sum() == 0:
        raise ValueError("Q.Value contains no numeric values.")
    if quantity.notna().sum() == 0:
        raise ValueError("Quantity contains no numeric values.")

    return {
        "total_precursors": int(len(data)),
        "unique_protein_groups": int(data["Protein.Group"].nunique(dropna=True)),
        "unique_genes": int(data["Genes"].nunique(dropna=True)),
        "q_value_below_0.01": int((q_values < 0.01).sum()),
        "q_value_below_0.05": int((q_values < 0.05).sum()),
        "median_quantity": float(quantity.median()),
        "mean_quantity": float(quantity.mean()),
    }


def save_summary(summary, output_file):
    """Save the QC summary as one-row CSV."""
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([summary]).to_csv(output_path, index=False)


def parse_args():
    parser = argparse.ArgumentParser(description="Summarize DIA-NN output QC metrics.")
    parser.add_argument("--input", default="data/example_diann_output.csv")
    parser.add_argument("--output", default="results/proteomics_qc_summary.csv")
    return parser.parse_args()


def main():
    args = parse_args()
    data = load_diann_output(args.input)
    summary = summarize_qc_metrics(data)
    save_summary(summary, args.output)

    for key, value in summary.items():
        print(f"{key}: {value}")
    print(f"QC summary saved to {args.output}")


if __name__ == "__main__":
    main()
