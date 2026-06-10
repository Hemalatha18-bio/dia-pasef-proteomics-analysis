"""
Proteomics QC Summary Script

This script summarizes example DIA-NN output metrics including
Q-values, protein counts, peptide counts, and intensity distribution.

Author: Hemalatha Ponnam
"""

import pandas as pd


def load_diann_output(file_path):
    """
    Load DIA-NN output file.
    """
    data = pd.read_csv(file_path)
    return data


def summarize_qc_metrics(data):
    """
    Summarize key QC metrics from DIA-NN output.
    """

    summary = {
        "total_precursors": len(data),
        "unique_protein_groups": data["Protein.Group"].nunique(),
        "unique_genes": data["Genes"].nunique(),
        "q_value_below_0.01": (data["Q.Value"] < 0.01).sum(),
        "q_value_below_0.05": (data["Q.Value"] < 0.05).sum(),
        "median_quantity": data["Quantity"].median(),
        "mean_quantity": data["Quantity"].mean()
    }

    return summary


def save_summary(summary, output_file):
    """
    Save QC summary as a CSV file.
    """

    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(output_file, index=False)


def main():
    input_file = "data/example_diann_output.csv"
    output_file = "results/proteomics_qc_summary.csv"

    print("Loading DIA-NN output...")
    data = load_diann_output(input_file)

    print("Summarizing QC metrics...")
    summary = summarize_qc_metrics(data)

    for key, value in summary.items():
        print(f"{key}: {value}")

    print("Saving summary...")
    save_summary(summary, output_file)

    print(f"QC summary saved to {output_file}")


if __name__ == "__main__":
    main()
