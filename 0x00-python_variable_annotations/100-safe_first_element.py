#!/usr/bin/env python3
"""Duck typing - first element of a sequence."""

from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of the input.

    Args:
        lst (Sequence[Any]): Input sequence

    Returns:
        Union[Any, NoneType]: Union[Any, NoneType]
    """
    if lst:
        return lst[0]
    else:
        return None
