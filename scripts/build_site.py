#!/usr/bin/env python3
"""Publish canonical lecture slides into docs/; run from any working directory."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

def main():
    for source in sorted((ROOT / 'lectures').glob('*/slides.html')):
        destination = ROOT / 'docs' / 'lectures' / source.parent.name / source.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        print(f'{source.relative_to(ROOT)} -> {destination.relative_to(ROOT)}')

if __name__ == '__main__':
    main()
