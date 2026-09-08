# GLaDOS Piper Voice Pipeline

Private archival pipeline used to reconstruct and prepare an English
GLaDOS single-speaker dataset for Piper/VITS training.

## Contents

- `download_glados.py` — retrieves and prepares the source voice lines
- `audit_dataset.py` — validates metadata/audio consistency and creates hashes
- `requirements.txt` — dataset preparation dependencies
- `DATASET_PROVENANCE.md` — dataset provenance and processing information

The actual dataset, trained checkpoints, and ONNX models are intentionally
excluded from this Git repository.

## Dataset

Private Hugging Face dataset:

`WhoIsMrSentry/glados-portal-en-dataset`

Current reconstructed dataset:

- 806 WAV files
- 806 metadata entries
- 62.371 minutes
- 22050 Hz
- English
- single speaker

## Dataset Creation

Create the environment:

    uv python install 3.11
    uv venv .venv --python 3.11 --seed
    source .venv/bin/activate
    python -m pip install -r requirements.txt

Download and prepare:

    python download_glados.py
    mv dataset_dir/manifest.csv dataset_dir/metadata.csv

Audit:

    python audit_dataset.py

Verify hashes:

    cd dataset_dir
    sha256sum -c sha256sums.txt

## Piper Training Context

Known training configuration:

- language: `en-us`
- dataset format: `ljspeech`
- single speaker
- sample rate: 22050 Hz
- model quality: medium
- base checkpoint: `epoch=2164-step=1355540.ckpt`
- final/export checkpoint: `epoch=5308-step=1512740.ckpt`

Surviving exported model:

- `glados_piper_medium_epoch5308.onnx`
- `glados_piper_medium_epoch5308.onnx.json`

## Use

Private personal archival, research, and local text-to-speech experimentation.
