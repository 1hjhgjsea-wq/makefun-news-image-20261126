#!/usr/bin/env python3
"""Copy the pre-drawn 26 November 2026 news infographic to /output/entry.png.

Standard library only: the grader's Python image has no Pillow and no
network, so this program only copies the image file that ships beside it.
The image itself is drawn at build time by draw_infographic.py (Pillow),
which is never imported here.

Usage: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")

MAX_BYTES = 1048576
MAX_DIM = 1024


def validate(path):
    """Check the copied file is a whole PNG within the gate limits.

    Returns a list of problems (empty when valid). Validation is
    non-fatal: the copy is the entry either way, but a problem is
    printed so a bad build is visible instead of silent.
    """
    problems = []
    try:
        with open(path, "rb") as f:
            head = f.read(33)
    except OSError as exc:
        return ["cannot read output: %s" % exc]
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        problems.append("not a PNG (bad magic bytes)")
        return problems
    if head[12:16] != b"IHDR":
        problems.append("PNG has no IHDR chunk")
        return problems
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        problems.append("image %dx%d exceeds %dpx" % (width, height, MAX_DIM))
    if os.path.getsize(path) > MAX_BYTES:
        problems.append("image exceeds 1 MiB")
    return problems


def copy_image(src, dst):
    """Copy src to dst, falling back to a manual chunked copy."""
    try:
        shutil.copyfile(src, dst)
    except OSError:
        with open(src, "rb") as fin, open(dst, "wb") as fout:
            while True:
                chunk = fin.read(65536)
                if not chunk:
                    break
                fout.write(chunk)


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    copy_image(SRC, DST)
    size = os.path.getsize(DST)
    problems = validate(DST)
    if problems:
        for problem in problems:
            print("warning: %s" % problem, file=sys.stderr)
    print("wrote", DST, size, "bytes")


if __name__ == "__main__":
    main()
