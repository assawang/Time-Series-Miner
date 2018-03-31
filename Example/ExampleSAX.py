"""
Example of SAX
===============================================
Example of Basic SAX
"""
# Author: Zhongyu Wang
# License: BSD 3-Clause or CC-0

from DataUtils import UCIFileReader as ur
from TransAlgo import Basic_SAX as bsax

utdata = ur.UCIFileReader('UCIData/Beef/Beef_TRAIN')
for utd in utdata:
    print(utd.get_labelField(), utd.get_dataField())
    data = utd.get_dataField()
    sax_data = bsax.Basic_SAX(data, 10, 3)
    print(sax_data)
    break