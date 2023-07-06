#!/usr/bin/env python3
'''
Annotate the below function’s parameters
and return values with the appropriate types
def element_length(lst):
    return [(i, len(i)) for i in lst]
'''


from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple
from typing import Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    'Returns a list of tuples'
    return [(i, len(i)) for i in lst]
