#!/usr/bin/env python3
"""
    Module with typing Python
"""


from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    The function element_length takes a list of sequences
    """
    return [(i, len(i)) for i in lst]
