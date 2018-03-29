"""
DataLine Class
===============================================
Base Class of data including two class fields which are
labelField and dataField
"""

# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0


class DataLine():
    def __init__(self, labelField, dataField):
        self.labelField = labelField
        self.dataField = dataField

    def get_labelField(self):
        return self.labelField

    def get_dataField(self):
        return self.dataField
