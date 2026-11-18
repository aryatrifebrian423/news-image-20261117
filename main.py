#!/usr/bin/env python3
"""Entry for news-image-20261117: copy the built poster to the output dir.

The image (entry.png, 1024x1024, drawn in this session) sits next to this
file in the repository. The grader runs this program with no network; it
just copies the image to MAKEFUN_OUTPUT_DIR/entry.png.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image missing: {source}")
    if source.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry image is not a PNG file")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
