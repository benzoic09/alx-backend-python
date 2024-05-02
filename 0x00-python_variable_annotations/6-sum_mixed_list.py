#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
     """Return the sum of integers and floats in the input list."""
     return sum(mxd_lst)