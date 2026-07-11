"""
tools/search.py

Implements the search_campus tool: a general-purpose keyword search
across every category (libraries, buildings, dining, services) —
used when a query doesn't clearly belong to one specific tool.
"""

from utils.data_loader import search_by_keyword


def search_campus(query: str) -> str:
    """
    Search across all campus locations (libraries, buildings, dining,
    and student services) for a keyword.

    Args:
        query: Any keyword, e.g. "printing", "coffee", "quiet study",
               "career".

    Returns:
        A formatted string listing all matches across every category,
        grouped by category.
    """
    matches = search_by_keyword(query)

    if not matches:
        return f"No campus locations found matching '{query}'."

    # Group results by category so the output is easy to scan.
    grouped = {}
    for entry in matches:
        grouped.setdefault(entry["category"], []).append(entry)

    lines = []
    for category, entries in grouped.items():
        label = category.replace("_", " ").title()
        lines.append(f"[{label}]")
        for entry in entries:
            lines.append(f"  {entry['name']} — {entry['address']}")

    return "\n".join(lines)