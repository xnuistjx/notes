"""A place for notes, snippets and half-finished experiments."""

from __future__ import annotations

__all__ = ["notes"]


def notes(value):
    """A place for notes, snippets and half-finished experiments."""
    if value is None:
        raise ValueError("value must not be None")
    return value
