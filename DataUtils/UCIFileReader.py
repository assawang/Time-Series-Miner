"""
UCI File Reader
===============================================
This is a simple UCI File Reader which is appled to the
UCI Time Series DataSet.

Each dataset has two files of which names are XXX_TRAIN and XXX_TEST.
Each line of file represent one time series data which is split by ','.
The first integer of the line represents label and the rest are data.

The URL of DataSet is http://www.cs.ucr.edu/~eamonn/time_series_data/.
If you use this dataset please reference as:
Yanping Chen, Eamonn Keogh, Bing Hu, Nurjahan Begum, Anthony Bagnall,
Abdullah Mueen and Gustavo Batista (2015).
The UCR Time Series Classification Archive.
URL www.cs.ucr.edu/~eamonn/time_series_data/
"""
# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0

import numpy as np
from DataUtils import UTData as utd
import fileinput


def UCIFileReader(filePath):
    for line in fileinput.input(filePath):
        eachnum = line.split(',')
        label = int(eachnum[0])
        data = []
        for each in eachnum[1:]:
            data = data + [float(each)]
        utdata = utd.UTData(label, np.array(data))
        yield utdata
