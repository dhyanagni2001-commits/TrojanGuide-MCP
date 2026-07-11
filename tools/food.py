"""
tools/food.py

Implements the find_food tool: search dining venues by cuisine type,
craving, or keyword (e.g. "coffee", "vegetarian", "tacos").
"""

from utils.data_loader import filter_by_category, search_by_keyword


def find_food(query: str = "") -> str:
    """
    Find dining venues on campus, optionally filtered by a keyword.

    Args:
        query: A cuisine, craving, or keyword, e.g. "coffee", "tacos",
               "vegetarian", "village". Leave empty to list all dining
               venues.

    Returns:
        A formatted string listing matching dining venues with their
        location.
    """
    if query:
        # search_by_keyword already checks name/address/tags, but we
        # also want to make sure we only return dining entries.
        matches = [
            entry for entry in search_by_keyword(query)
            if entry["category"] == "dining"
        ]
        if not matches:
            return f"No dining spots found matching '{query}'."
    else:
        matches = filter_by_category("dining")

    lines = []
    for entry in matches:
        lines.append(f"{entry['name']} — {entry['address']}")

    return "\n".join(lines)     