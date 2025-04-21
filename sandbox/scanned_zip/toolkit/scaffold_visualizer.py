from pathlib import Path
import os

def visualize_structure(zip_path: Path) -> str:
    def build_tree(path, prefix=""):
        tree = ""
        entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        for i, entry in enumerate(entries):
            connector = "└── " if i == len(entries) - 1 else "├── "
            tree += f"{prefix}{connector}{entry.name}\n"
            if entry.is_dir():
                extension = "    " if i == len(entries) - 1 else "│   "
                tree += build_tree(entry, prefix + extension)
        return tree

    tree = build_tree(zip_path)
    return f"<pre>{tree}</pre>"