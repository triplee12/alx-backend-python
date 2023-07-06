#!/usr/bin/env python3
"""Let's duck type an iterable object."""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get the length of the elements of list.

    Args:
        lst (Iterable[Sequence]): list of elements

    Returns:
        List[Tuple[Sequence, int]]: length of element in list
    """
    return [(i, len(i)) for i in lst]
