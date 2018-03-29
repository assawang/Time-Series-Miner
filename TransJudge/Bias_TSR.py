"""
Bias of Time Series Represent
===============================================
Bias of Time Series Represent
"""

import math


def Bias_RMSE(arr1, arr2):
    """
    Implement of Bias Root Mean Square Error
    =========================================================
    Input: Numpy Array 1, Numpy Array 2 with the same length
    Output: Float
    """
    if arr1.shape[0] != arr2.shape[0]:
        print("Error: two array must have same length")
        return
    s = 0
    for i in range(0, arr1.shape[0]):
        s = s + (arr1[i] - arr2[i]) * (arr1[i] - arr2[i])
    s = s / arr1.shape[0]
    output = math.sqrt(s)
    return output
