"""
data_loader.py

Loads campus.json once into memory and exposes small helper functions
that every tool in tools/ can reuse. Keeping this logic in one place
means the JSON is only read from disk a single time per server run.
"""

import json
from pathlib import Path

# Path to the dataset, relative to this file so it works no matter
# where the server is launched from.
DATA_PATH = Path(__file__).parent.parent / "data" / "campus.json"

# Module-level cache. Populated the first time load_campus_data() runs.
_campus_data = None


def load_campus_data():
    """Load campus.json into memory once and cache it for reuse."""
    global _campus_data
    if _campus_data is None:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            _campus_data = json.load(f)
    return _campus_data


def filter_by_category(category: str):
    """Return all entries matching a given category (case-insensitive)."""
    data = load_campus_data()
    category = category.lower()
    return [entry for entry in data if entry["category"].lower() == category]


def search_by_keyword(keyword: str):
    """
    Return all entries where the keyword appears in the name, address,
    or tags. Simple substring match — no fuzzy search in this MVP.
    """
    data = load_campus_data()
    keyword = keyword.lower()
    results = []
    for entry in data:
        haystack = " ".join(
            [entry["name"], entry["address"]] + entry.get("tags", [])
        ).lower()
        if keyword in haystack:
            results.append(entry)
    return results


def find_by_name(name: str):
    """Return the single best name match, or None if nothing matches."""
    data = load_campus_data()
    name = name.lower()
    # Exact match first
    for entry in data:
        if entry["name"].lower() == name:
            return entry
    # Fall back to substring match
    for entry in data:
        if name in entry["name"].lower():
            return entry
    return None