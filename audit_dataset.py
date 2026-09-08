from pathlib import Path
import csv
import hashlib
import json
import soundfile as sf

ROOT = Path("dataset_dir")
WAV_DIR = ROOT / "wavs"
META = ROOT / "metadata.csv"

rows = []
with META.open("r", encoding="utf-8") as f:
    for line_no, raw in enumerate(f, 1):
        raw = raw.rstrip("\n\r")
        if not raw:
            continue

        parts = raw.split("|", 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid metadata at line {line_no}: {raw!r}")

        audio_id, text = parts
        rows.append((audio_id, text))

wav_files = sorted(WAV_DIR.glob("*.wav"))
metadata_ids = {r[0] for r in rows}

missing = []
duration = 0.0
sample_rates = {}

for audio_id, _ in rows:
    wav = WAV_DIR / f"{audio_id}.wav"

    if not wav.exists():
        missing.append(str(wav))
        continue

    info = sf.info(wav)
    duration += info.frames / info.samplerate
    sample_rates[str(info.samplerate)] = sample_rates.get(str(info.samplerate), 0) + 1

orphan = [
    str(w)
    for w in wav_files
    if w.stem not in metadata_ids
]

duplicate_ids = len(rows) - len(metadata_ids)

stats = {
    "metadata_rows": len(rows),
    "wav_files": len(wav_files),
    "duration_seconds": round(duration, 3),
    "duration_minutes": round(duration / 60, 3),
    "sample_rates": sample_rates,
    "missing_wavs": missing,
    "orphan_wavs": orphan,
    "duplicate_metadata_ids": duplicate_ids,
}

(ROOT / "dataset_stats.json").write_text(
    json.dumps(stats, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

sha_file = ROOT / "sha256sums.txt"

with sha_file.open("w", encoding="utf-8") as out:
    for path in [META, *wav_files]:
        h = hashlib.sha256()

        with path.open("rb") as f:
            for block in iter(lambda: f.read(1024 * 1024), b""):
                h.update(block)

        out.write(f"{h.hexdigest()}  {path.relative_to(ROOT)}\n")

print(json.dumps(stats, indent=2, ensure_ascii=False))

if missing:
    raise SystemExit("ERROR: missing WAV files")

if orphan:
    print("WARNING: orphan WAV files detected")
