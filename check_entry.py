#!/usr/bin/env python3
"""Validate the news-image-20261119 entry: run main.py twice into temp dirs
and assert the output is a 1024x1024 PNG under 1 MiB, identical across runs.
"""
import hashlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def run_once():
    tmp = tempfile.mkdtemp(prefix="news-image-check-")
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
    r = subprocess.run([sys.executable, os.path.join(HERE, "main.py")],
                       env=env, capture_output=True, text=True)
    assert r.returncode == 0, f"main.py failed: {r.stderr}"
    path = os.path.join(tmp, "entry.png")
    assert os.path.exists(path), "entry.png not written"
    return path


def main():
    from PIL import Image
    p1, p2 = run_once(), run_once()
    b1 = open(p1, "rb").read()
    b2 = open(p2, "rb").read()
    assert b1 == b2, "not deterministic: two runs differ"
    assert len(b1) <= 1048576, f"over 1 MiB: {len(b1)} bytes"
    im = Image.open(p1)
    assert im.size == (1024, 1024), f"wrong size: {im.size}"
    assert im.format == "PNG", f"not PNG: {im.format}"
    print(f"PASS: {im.size} PNG, {len(b1)} bytes, "
          f"sha256 {hashlib.sha256(b1).hexdigest()[:16]}..., deterministic")
    return 0


if __name__ == "__main__":
    sys.exit(main())
