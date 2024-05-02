#!/usr/bin/env python3
"""add duck-typed annotated """
from typing import Any


def safe_first_element(lst: list) -> Any:
    """add duck-typed annotated """
    if lst:
        return lst[0]
    else:
        return None
