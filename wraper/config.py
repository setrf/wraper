import os
from pathlib import Path

# Default storage directory is 'data' in the current working directory
DEFAULT_STORAGE_DIR = Path.cwd() / "data"

def get_storage_dir():
    """Returns the configured storage directory."""
    # In the future, this could read from a config file or env var
    return DEFAULT_STORAGE_DIR
