"""
Main
===============================================
Piece of shit
"""
# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0

from DataUtils import UCIFileReader as ur
import matplotlib.pyplot as plt
from TransAlgo import Basic_PAA as bpaa
from TransAlgo import Basic_SAX as bsax

utdata = ur.UCIFileReader('UCIData/Beef/Beef_TRAIN')
for utd in utdata:
    print(utd.get_labelField(), utd.get_dataField())
    data = utd.get_dataField()
    # paa_data = bpaa.Basic_PAA(data, 10)
    sax_data = bsax.Basic_SAX(data, 10, 3)
    print(sax_data)
    # plt.plot(range(data.shape[0]), utd.get_dataField())
    # plt.plot(range(paa_data.shape[0]), paa_data)
    # plt.show()
    break
