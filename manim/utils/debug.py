"""Debugging utilities."""


from __future__ import annotations

__all__ = ["print_family", "index_labels"]


from ..mobject.numbers import Integer
from ..mobject.types.vectorized_mobject import VGroup
from .color import BLACK


def print_family(mobject, n_tabs=0):
    """For debugging purposes"""
    print("\t" * n_tabs, mobject, id(mobject))
    for submob in mobject.submobjects:
        print_family(submob, n_tabs + 1)


def index_labels(mobject, label_height=0.15):
    labels = VGroup()
    for n, submob in enumerate(mobject):
        label = Integer(n)
        label.height = label_height
        label.move_to(submob)
        label.set_stroke(BLACK, 5, background=True)
        labels.add(label)
    return labels
