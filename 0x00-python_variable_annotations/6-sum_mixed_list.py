#!/usr/bin/env python3
'''
type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
'''

from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    'sums mxd_lst and returns a float'
    total: float = sum(mxd_lst)
    return float(total)
