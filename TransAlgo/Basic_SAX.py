"""
Basic SAX
===============================================
Implement of basic Symbolic Aggregation approXimation algorithm

Reference:

Input: Numpy Array, Reduced Data Piece Num W, Num of Symbol A 
Output: Numpy Array

"""

# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0

import numpy as np
import math
from TransAlgo import Basic_PAA as bpaa


def Divide(a):
    return {
        3: [-0.43, 0.43],
        4: [-0.67, 0, 0.67],
        5: [-0.84, -0.25, 0.25, 0.84]
    }.get(a)


def getSymbol(divide, num):
    sym = 'a'
    for i in divide:
        if num <= i:
            break
        sym = chr(ord(sym) + 1)
    return sym


def Basic_SAX(data, w, a):
    PAAdata = bpaa.Basic_PAA(data, w)
    divide = Divide(a)
    res = []
    for i in PAAdata:
        res.append(getSymbol(divide, i))
    return res


