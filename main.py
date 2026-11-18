"""news-image-01 entry: copy the cover image to the output directory.

The entry image (entry.png, JPEG bytes) sits next to this file. This program
copies it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
A plain byte copy is deterministic: running it twice writes identical bytes.
Standard library only; no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(f"entry image missing next to main.py: {SRC}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # shutil.copyfile copies raw bytes only: same input, same output, every run.
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
