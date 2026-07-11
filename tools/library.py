"""
tools/library.py

Implements the find_library tool: list USC libraries, optionally
filtered by a feature like printing or 24-hour access.
"""

from utils.data_loader import filter_by_category


def find_library(filter_tag: str = "") -> str:
    """
    List USC libraries, optionally filtered by a feature.

    Args:
        filter_tag: Optional feature to filter by, e.g. "printing",
                    "24 hour", "study rooms", "quiet". Leave empty to
                    list all libraries.

    Returns:
        A formatted string listing matching libraries with their
        address and hours.
    """
    libraries = filter_by_category("library")

    if filter_tag:
        filter_tag = filter_tag.lower()
        libraries = [
            lib for lib in libraries
            if any(filter_tag in tag.lower() for tag in lib.get("tags", []))
        ]
        if not libraries:
            return f"No libraries found matching '{filter_tag}'."

    lines = []
    for lib in libraries:
        lines.append(f"{lib['name']}\n  Address: {lib['address']}\n  Hours: {lib['hours']}")

    return "\n\n".join(lines)