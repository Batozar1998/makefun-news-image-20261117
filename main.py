"""Put the cover image where the harness looks for it.

The harness reads entry.png from the directory named by
MAKEFUN_OUTPUT_DIR. This script loads the image kept beside it and
recreates those exact bytes in that directory, creating the folder
first when it is missing. Only the standard library is used.
"""

from os import getenv, makedirs
import pathlib


def place_image() -> pathlib.Path:
    folder = pathlib.Path(getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    makedirs(folder, exist_ok=True)
    target = folder / "entry.png"
    data = pathlib.Path(__file__).with_name("entry.png").read_bytes()
    target.write_bytes(data)
    return target


place_image()
