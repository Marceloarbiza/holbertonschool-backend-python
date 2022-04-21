#!/usr/bin/env python3
"""
    Module with typing Python
"""


from typing import List, Union


type_union = Union[int, float]


def sum_mixed_list(mxd_lst: List[type_union]) -> float:
    return sum(mxd_lst)
