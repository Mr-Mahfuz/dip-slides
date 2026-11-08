"""Compatibility entry point: build the revised study room."""
import runpy
from pathlib import Path

runpy.run_path(str(Path(__file__).with_name('build_study.py')), run_name='__main__')
