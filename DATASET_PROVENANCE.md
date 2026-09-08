# Dataset Provenance

## Dataset

This dataset contains English GLaDOS voice lines prepared for single-speaker
text-to-speech training with Piper/VITS.

## Source Material

The source audio consists of GLaDOS voice assets originating from Valve titles,
primarily:

- Portal
- Portal 2
- Dota 2 and other GLaDOS-related Valve material

The audio files and corresponding voice-line text were retrieved through
The Portal Wiki voice-line pages.

Retrieval pages:

- https://theportalwiki.com/wiki/GLaDOS_voice_lines_(Portal)
- https://theportalwiki.com/wiki/GLaDOS_voice_lines_(Portal_2)
- https://theportalwiki.com/wiki/GLaDOS_voice_lines_(Other)

The Portal Wiki is used here as the retrieval/indexing source. Ownership of the
underlying game audio and character material remains with the respective
rights holders, including Valve.

## Acquisition

The dataset acquisition script scans the GLaDOS voice-line pages and:

1. discovers linked WAV files;
2. extracts the associated English transcript text;
3. removes duplicate URLs;
4. removes selected unwanted/problematic entries;
5. converts numeric tokens in transcripts to English words;
6. downloads the corresponding WAV files;
7. creates Piper/LJSpeech-style metadata;
8. resamples all audio to 22050 Hz.

## Filtering

The acquisition pipeline excludes URLs containing:

- `potato`
- `_ding_`
- `00_part1_entry-6`
- `_escape_`

Extracted transcript entries containing the following characters are also
excluded:

- `[`
- `]`
- `$`

## Dataset Format

Directory structure:

    dataset_dir/
    ├── metadata.csv
    ├── dataset_stats.json
    ├── sha256sums.txt
    └── wav/
        ├── *.wav
        └── ...

Metadata format:

    audio_id|text

Each `audio_id` corresponds to:

    wav/<audio_id>.wav

## Dataset Statistics

- Language: English
- Speaker configuration: single speaker
- WAV files: 806
- Metadata entries: 806
- Total duration: 3742.288 seconds
- Total duration: 62.371 minutes
- Sample rate: 22050 Hz
- Missing WAV files: 0
- Orphan WAV files: 0
- Duplicate metadata IDs: 0

## Integrity

`sha256sums.txt` contains SHA-256 hashes for:

- `metadata.csv`
- every WAV file in the dataset

Integrity can be checked with:

    cd dataset_dir
    sha256sum -c sha256sums.txt

## Piper Training Configuration

The dataset was prepared for Piper/VITS with:

- Language: `en-us`
- Dataset format: `ljspeech`
- Speaker mode: single speaker
- Sample rate: 22050 Hz
- Quality/model size: medium

The known training configuration used an English US medium Piper base model.

Base checkpoint:

    epoch=2164-step=1355540.ckpt

Known final training/export checkpoint:

    epoch=5308-step=1512740.ckpt

The surviving local export is:

    glados_piper_medium_epoch5308.onnx
    glados_piper_medium_epoch5308.onnx.json

## Reconstruction Note

This dataset was reconstructed by re-running the original acquisition and
processing workflow against the source voice-line pages.

Because the previous local dataset was deleted and its historical hashes were
not preserved, byte-for-byte identity with the previously trained dataset
cannot be guaranteed.

The current reconstructed dataset is internally consistent and its hashes are
recorded in `sha256sums.txt`.

## Intended Use

Private personal research, archival, and local text-to-speech experimentation.

This dataset is not intended for public redistribution or commercial use.

The presence of source material in this private archive does not transfer any
rights to the underlying character, recordings, games, or other copyrighted
material.
