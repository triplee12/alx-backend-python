#!/usr/bin/python3
"""Complex types - functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiply a function by another function.

    Args:
        multiplier (float): the number of the function to multiply

    Returns:
        Callable[[float], float]: product of the function
    """

    def multiply(num: float) -> float:
        """
        Multiply a float number by the function

        Args:
            num (float): number to multiply

        Returns:
            float: the result of the multiplication
        """
        return num * multiplier

    return multiply
