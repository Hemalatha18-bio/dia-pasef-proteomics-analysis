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
    data = pd.DataFrame(
        {
            "Protein.Group": ["P1", "P1", "P2"],
            "Genes": ["G1", "G1", "G2"],
            "Q.Value": [0.005, 0.02, 0.10],
            "Quantity": [100.0, 200.0, 300.0],
        }
    )
    summary = summarize_qc_metrics(data)
    assert summary["total_precursors"] == 3
    assert summary["unique_protein_groups"] == 2
    assert summary["unique_genes"] == 2
    assert summary["q_value_below_0.01"] == 1
    assert summary["q_value_below_0.05"] == 2
    assert summary["percent_q_value_below_0.01"] == pytest.approx(100 / 3)
    assert summary["percent_q_value_below_0.05"] == pytest.approx(200 / 3)
    assert summary["median_q_value"] == pytest.approx(0.02)
    assert summary["mean_quantity"] == pytest.approx(200.0)
    assert summary["missing_q_values"] == 0
    assert summary["missing_quantities"] == 0


def test_qc_summary_tracks_non_numeric_values_as_missing():
    data = pd.DataFrame(
        {
            "Protein.Group": ["P1", "P2", "P3"],
            "Genes": ["G1", "G2", "G3"],
            "Q.Value": [0.005, "bad", 0.02],
            "Quantity": [100.0, "bad", 300.0],
        }
    )
    summary = summarize_qc_metrics(data)
    assert summary["missing_q_values"] == 1
    assert summary["missing_quantities"] == 1
    assert summary["percent_q_value_below_0.05"] == pytest.approx(100.0)


def test_qc_summary_rejects_missing_columns():
    with pytest.raises(ValueError):
        summarize_qc_metrics(pd.DataFrame({"Q.Value": [0.01]}))


def test_qc_summary_rejects_fully_non_numeric_q_values():
    data = pd.DataFrame(
        {
            "Protein.Group": ["P1"],
            "Genes": ["G1"],
            "Q.Value": ["bad"],
            "Quantity": [100.0],
        }
    )
    with pytest.raises(ValueError, match="no numeric values"):
        summarize_qc_metrics(data)


def test_visualization_summary_validation(tmp_path):
    path = tmp_path / "summary.csv"
    pd.DataFrame({"total_precursors": [10]}).to_csv(path, index=False)
    with pytest.raises(ValueError):
        load_summary(path)
