#!/usr/bin/env python3
"""
    Module with typing Python
"""


from typing import List, Union


type_union = Union[int, float]


def sum_mixed_list(mxd_lst: List[type_union]) -> float:
    """
    Write a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and floats
    and returns their sum as a float.
    """
    return sum(mxd_lst)
