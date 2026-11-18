"""Copy the entry image into the harness output directory.

The image (entry.png, JPEG bytes) lives next to this file. This program
places an exact copy at $MAKEFUN_OUTPUT_DIR/entry.png (default /output),
creating the directory when needed. A raw byte copy is deterministic:
the same input always produces the same output bytes. Standard library
only; no network access.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def main() -> None:
    if not IMAGE.is_file():
        raise FileNotFoundError(f"entry image not found: {IMAGE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
