"""
DIA-NN Output Conversion Script

This script demonstrates how DIA-NN output files in .parquet format
can be converted into .csv and .tsv formats for downstream analysis.

Author: Hemalatha Ponnam
"""

import os
import pandas as pd


def convert_parquet_to_csv_tsv(input_file, output_folder):
    """
    Convert a DIA-NN .parquet output file into .csv and .tsv formats.

    Parameters
    ----------
    input_file : str
        Path to the input .parquet file.

    output_folder : str
        Folder where converted files will be saved.
    """

    os.makedirs(output_folder, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(input_file))[0]

    print(f"Reading file: {input_file}")
    data = pd.read_parquet(input_file)

    csv_output = os.path.join(output_folder, f"{base_name}.csv")
    tsv_output = os.path.join(output_folder, f"{base_name}.tsv")

    data.to_csv(csv_output, index=False)
    data.to_csv(tsv_output, sep="\t", index=False)

    print(f"CSV saved to: {csv_output}")
    print(f"TSV saved to: {tsv_output}")

    return csv_output, tsv_output


def summarize_q_values(input_file, q_value_column="Q.Value"):
    """
    Summarize Q-value distribution from a DIA-NN output table.

    Parameters
    ----------
    input_file : str
        Path to a .csv or .tsv DIA-NN output file.

    q_value_column : str
        Name of the Q-value column.
    """

    if input_file.endswith(".tsv"):
        data = pd.read_csv(input_file, sep="\t")
    else:
        data = pd.read_csv(input_file)

    if q_value_column not in data.columns:
        raise ValueError(f"Column '{q_value_column}' not found in file.")

    summary = {
        "total_rows": len(data),
        "q_value_less_than_0.01": (data[q_value_column] < 0.01).sum(),
        "q_value_less_than_0.05": (data[q_value_column] < 0.05).sum(),
        "minimum_q_value": data[q_value_column].min(),
        "median_q_value": data[q_value_column].median(),
        "maximum_q_value": data[q_value_column].max()
    }

    return summary


def main():
    """
    Example usage.

    Replace the example file path with a real DIA-NN parquet output file
    when running this workflow on actual data.
    """

    print("DIA-NN conversion workflow template")
    print("Add a DIA-NN .parquet file and update the input path in main().")


if __name__ == "__main__":
    main()
