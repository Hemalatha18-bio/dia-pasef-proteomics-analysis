# Data Description

## Public Demo Data

This repository uses a small DIA-NN-style example table to demonstrate downstream proteomics post-processing and quality-control code. The example data are intended for software testing, documentation, and portfolio demonstration only.

The public demo expects fields used by the QC utilities, including:

- `Protein.Group` — example protein-group identifier.
- `Genes` — example gene annotation.
- `Q.Value` — numeric Q-value used for threshold summaries.
- `Quantity` — numeric abundance/intensity-style value used for summary statistics.

Additional DIA-NN columns may be present in real outputs, but the public scripts only require the fields documented by their validation logic.

## What Is Not Included

This repository does not include original raw timsTOF/DIA-PASEF acquisition files, unpublished laboratory datasets, restricted or lab-owned outputs, original XL-MS datasets, or proprietary/intermediate analysis resources.

The broader project involved additional computational and experimental context such as DIA-PASEF, crosslinking mass spectrometry, FASTA curation, spectral-library preparation, XL-MSDigger/rescoring concepts, and HPC execution. Those broader project components should not be inferred from the small public example dataset alone.

## Interpretation

The example table and generated summaries are not biological findings and should not be used to assess experimental quality, protein significance, clinical relevance, or biological validity. Q-value thresholds and abundance summaries require interpretation in the context of the upstream analysis, experimental design, and appropriate proteomics QC practices.

## Using Your Own Data

Users may run the public utilities on compatible local DIA-NN outputs. Keep restricted, unpublished, patient-related, or lab-owned data outside the public repository. Before running the QC scripts, ensure the required columns are present and numeric fields contain valid values.
