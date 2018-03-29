"""
UCI Data Class
===============================================
This is a simple UCI Data Class which is appled to the
UCI Time Series DataSet.
"""

# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0

from DataUtils import DataLine


class UTData(DataLine.DataLine):
    def __init__(self, labelField, dataField):
        self.labelField = labelField
        self.dataField = dataField
