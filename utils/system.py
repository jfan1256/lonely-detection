import os

from pathlib import Path

# Get root directory
def get_root_dir() -> Path:
    return Path(os.getcwd()).resolve().parent

# Get data directory
def get_data():
    return get_root_dir() / 'data'
