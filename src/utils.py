from pathlib import Path


def get_project_root() -> Path:
    """Returns the root directory of the project."""
    parent = Path(__file__).parent
    if parent.name == "src":
        return parent.parent
    return parent
