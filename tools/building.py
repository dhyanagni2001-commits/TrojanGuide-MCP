"""
tools/building.py

Implements the find_building tool: look up a specific academic
building or landmark by name and return its address and details.
"""

from utils.data_loader import find_by_name, filter_by_category


def find_building(name: str) -> str:
    """
    Find an academic building or campus landmark by name.

    Args:
        name: The building name to search for (e.g. "Leavey Library",
              "Ronald Tutor Hall"). Partial names work too.

    Returns:
        A formatted string with the building's address and tags,
        or a helpful message if nothing matches.
    """
    entry = find_by_name(name)

    if entry is None:
        # Nothing matched by name — suggest nearby academic buildings
        # so the user isn't left with a dead end.
        buildings = filter_by_category("academic_building")
        suggestions = ", ".join(b["name"] for b in buildings[:5])
        return (
            f"I couldn't find a building matching '{name}'. "
            f"Some buildings I do know about: {suggestions}"
        )

    lines = [f"{entry['name']} ({entry['category'].replace('_', ' ')})"]
    lines.append(f"Address: {entry['address']}")
    lines.append(f"Hours: {entry['hours']}")
    if entry.get("tags"):
        lines.append(f"Features: {', '.join(entry['tags'])}")

    return "\n".join(lines)