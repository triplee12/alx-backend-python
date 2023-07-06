#!/usr/bin/python3
"""More involved type annotations."""

from types import NoneType
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any,
    default: Union[T, NoneType] = None
) -> Union[Any, T]:
    """
    Get the value of the given key.

    Args:
        dct (Mapping): dictionary mapping
        key (Any): key to get value
        default (Union[T, None], optional): Defaults to None.

    Returns:
        Union[Any, T]: Union[Any, T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
