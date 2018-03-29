"""
Basic PAA
===============================================
Implement of basic Piecewise Aggregation Approximation algorithm

Reference:Keogh E, Chakrabarti K, Pazzani M, et al. Dimensionality
Reduction for Fast Similarity Search in Large Time Series Databases[J].
Knowledge & Information Systems, 2001, 3(3):263-286.

Input: Numpy Array , Reduced Data Piece Num W
Output: Numpy Array

"""

# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0

# import UTData as utd

import numpy as np
import math


def Basic_PAA(data, w):
    n = data.shape[0]
    if w > n:
        print("ERROR: W  bigger than N")
        return
    if w <= 0:
        print("ERROR: W  less than 0")
        return
    output = []
    batch_len = math.ceil(n / w)
    i = 0
    while i <= n - 1:
        s = 0
        num = 0
        j = i
        while j <= i + batch_len - 1 and j <= n - 1:
            s = s + data[j]
            j = j + 1
            num = num + 1
        i = j
        for k in range(1, num + 1):
            output = output + [s / num]
    return np.array(output)
