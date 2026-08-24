import pandas as pd
import pytest

from src.convert_diann_outputs import summarize_q_values
from src.proteomics_qc_summary import summarize_qc_metrics
from src.visualize_qc import load_summary


def test_summarize_q_values(tmp_path):
    path = tmp_path / "q.csv"
    pd.DataFrame({"Q.Value": [0.005, 0.02, 0.10]}).to_csv(path, index=False)
    summary = summarize_q_values(path)
    assert summary["total_rows"] == 3
    assert summary["q_value_less_than_0.01"] == 1
    assert summary["q_value_less_than_0.05"] == 2


def test_qc_summary_metrics():
    data = pd.DataFrame({
        "Protein.Group": ["P1", "P1", "P2"],
        "Genes": ["G1", "G1", "G2"],
        "Q.Value": [0.005, 0.02, 0.10],
        "Quantity": [100.0, 200.0, 300.0],
    })
    summary = summarize_qc_metrics(data)
    assert summary["total_precursors"] == 3
    assert summary["unique_protein_groups"] == 2
    assert summary["q_value_below_0.01"] == 1


def test_qc_summary_rejects_missing_columns():
    with pytest.raises(ValueError):
        summarize_qc_metrics(pd.DataFrame({"Q.Value": [0.01]}))


def test_visualization_summary_validation(tmp_path):
    path = tmp_path / "summary.csv"
    pd.DataFrame({"total_precursors": [10]}).to_csv(path, index=False)
    with pytest.raises(ValueError):
        load_summary(path)
