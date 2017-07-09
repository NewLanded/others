# -*- coding: utf-8 -*-

import xmlMessage


def basicInfo():
    allXmlData = {}
    allNatpData = {}
    for key,value in xmlMessage.data.items():
        if key.startswith('natp_'):
            allNatpData[key] = value
        else:
            allXmlData[key] = value
    return allXmlData,allNatpData
