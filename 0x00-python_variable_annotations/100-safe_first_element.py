#!/usr/bin/env python3
"""add duck-typed annotated """
from typing import Any, sequence, Union


def safe_first_element(lst:  Sequence[Any]) -> Union[Any, None]:
    """add duck-typed annotated """
    if lst:
        return lst[0]
    else:
        return None
