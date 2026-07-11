"""
tools/services.py

Implements the find_student_service tool: look up student support
offices like Career Center, Financial Aid, Health Center, etc.
"""

from utils.data_loader import filter_by_category, search_by_keyword


def find_student_service(query: str = "") -> str:
    """
    Find a student service office on campus.

    Args:
        query: A service name or keyword, e.g. "career", "financial aid",
               "health", "counseling", "usc id". Leave empty to list all
               student services.

    Returns:
        A formatted string listing matching services with their
        address and hours.
    """
    if query:
        matches = [
            entry for entry in search_by_keyword(query)
            if entry["category"] == "student_service"
        ]
        if not matches:
            return f"No student services found matching '{query}'."
    else:
        matches = filter_by_category("student_service")

    lines = []
    for entry in matches:
        lines.append(f"{entry['name']}\n  Address: {entry['address']}\n  Hours: {entry['hours']}")

    return "\n\n".join(lines)