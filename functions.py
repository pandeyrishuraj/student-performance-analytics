"""Reusable functions for Student Performance Analytics System.

The main.py file currently contains its own functions so the project can run
as a single entry point. This optional module provides the core grade function
for learning/reuse and can be used when refactoring the project.
"""


def calculate_grade(average):
    """Assign a grade using the project grading rule."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"
