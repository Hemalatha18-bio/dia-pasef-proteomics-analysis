"""Utilities for converting and summarizing DIA-NN output files.

This public portfolio script demonstrates safe post-processing of DIA-NN tables.
It does not reproduce the complete DIA-PASEF or XL-MS workflow.
"""

import argparse
import json
from pathlib import Path

import pandas as pd


def convert_parquet_to_csv_tsv(input_file, output_folder):
    """Convert a DIA-NN parquet table to CSV and TSV outputs."""
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if input_path.suffix.lower() != ".parquet":
        raise ValueError("Conversion input must be a .parquet file.")

    output_dir = Path(output_folder)
    output_dir.mkdir(parents=True, exist_ok=True)

    data = pd.read_parquet(input_path)
    if data.empty:
        raise ValueError("Input parquet table is empty.")

    csv_output = output_dir / f"{input_path.stem}.csv"
    tsv_output = output_dir / f"{input_path.stem}.tsv"
    data.to_csv(csv_output, index=False)
    data.to_csv(tsv_output, sep="\t", index=False)
    return csv_output, tsv_output


def load_tabular_file(input_file):
    """Load CSV or TSV DIA-NN output for summary calculations."""
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    suffix = input_path.suffix.lower()
    if suffix == ".tsv":
        return pd.read_csv(input_path, sep="\t")
    if suffix == ".csv":
        return pd.read_csv(input_path)
    raise ValueError("Summary input must be a .csv or .tsv file.")


def summarize_q_values(input_file, q_value_column="Q.Value"):
    """Summarize Q-value distribution from a DIA-NN output table."""
    data = load_tabular_file(input_file)
    if data.empty:
        raise ValueError("Input DIA-NN table is empty.")
    if q_value_column not in data.columns:
        raise ValueError(f"Column '{q_value_column}' not found in file.")

    q_values = pd.to_numeric(data[q_value_column], errors="coerce")
    if q_values.notna().sum() == 0:
        raise ValueError(f"Column '{q_value_column}' contains no numeric values.")

    return {
        "total_rows": int(len(data)),
        "q_value_less_than_0.01": int((q_values < 0.01).sum()),
        "q_value_less_than_0.05": int((q_values < 0.05).sum()),
        "minimum_q_value": float(q_values.min()),
        "median_q_value": float(q_values.median()),
        "maximum_q_value": float(q_values.max()),
    }


def save_summary(summary, output_file):
    """Write a Q-value summary dictionary to JSON."""
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)


def parse_args():
    parser = argparse.ArgumentParser(description="DIA-NN post-processing demo utilities.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    convert_parser = subparsers.add_parser("convert", help="Convert parquet to CSV/TSV.")
    convert_parser.add_argument("--input", required=True, help="Input DIA-NN parquet file.")
    convert_parser.add_argument("--output-dir", default="results/converted")

    summary_parser = subparsers.add_parser("summarize", help="Summarize Q-values.")
    summary_parser.add_argument("--input", required=True, help="Input CSV or TSV file.")
    summary_parser.add_argument("--q-value-column", default="Q.Value")
    summary_parser.add_argument("--output", default="results/q_value_summary.json")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "convert":
        csv_output, tsv_output = convert_parquet_to_csv_tsv(args.input, args.output_dir)
        print(f"CSV saved to: {csv_output}")
        print(f"TSV saved to: {tsv_output}")
    else:
        summary = summarize_q_values(args.input, args.q_value_column)
        save_summary(summary, args.output)
        print(f"Q-value summary saved to: {args.output}")


if __name__ == "__main__":
    main()
