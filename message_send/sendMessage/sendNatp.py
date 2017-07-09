# -*- coding:utf-8 -*-

from natpClient import MyNatpClient
import time,re


def sendNatp(natpData):
    natpDict = natpDataHandle(natpData)
    mynatpclient = MyNatpClient()
    mynatpclient.setHead( 'PRDTUPCHNATP', 'PUB', '00000' )
    for key,value in natpDict.items():
        mynatpclient.addField(key,value)
    result = mynatpclient.sendRequest( '38.63.131.113', 9901, 120 )
    return result
    


def natpDataHandle(natpData):
    natpData = natpData.replace(' ','')
    natpData = natpData.replace('\n','')
    natpDict = {}
    cycleData = natpData.split(',')
    for fieldData in cycleData:
        if fieldData != '':
            fieldItem = fieldData.split('::')
            natpDict[fieldItem[0]] = fieldItem[1]
    natpDict['TranDate'] = str(time.strftime( '%Y%m%d', time.localtime()))
    natpDict['TranTime'] = str(time.strftime( '%H%M%S', time.localtime()))
    natpDict['ConsumerSeqNo'] = str(time.strftime( '%Y%m%d', time.localtime())) + str(time.strftime( '%H%M%S', time.localtime()))
    return natpDict
    


