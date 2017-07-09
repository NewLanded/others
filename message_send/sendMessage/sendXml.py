# -*- coding: utf-8 -*-
import socket
import xmlMessage
import re
import time

def sendXml(MsgPack):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(( '38.63.131.113', 9902))
        s.sendall(str(int(len(MsgPack.replace(" ",""))+2)).rjust(8,"0")+MsgPack)
        data = ''
        while True:
            data1 = s.recv(8192)
            if not len(data1):
                break
            data = data + data1
        data = re.sub(r'(<BODY>)',r'\n\1\n',data)
        data = re.sub(r'(</BODY>)',r'\n\1',data)
        data = re.sub(r'(</.*?>)',r'\1\n',data)
        s.close()
        return data
    except Exception,e:
        s.close()
        return e

def dataHandle(MsgPack):
    MsgPack = re.sub(r'<TranDate>.*?</TranDate>','<TranDate>'+time.strftime( '%Y%m%d', time.localtime() )+'</TranDate>',MsgPack)
    MsgPack = re.sub(r'<TranTime>.*?</TranTime>','<TranTime>'+time.strftime( '%H%M%S', time.localtime() )+'</TranTime>',MsgPack)
    MsgPack = re.sub(r'<ConsumerSeqNo>.*?</ConsumerSeqNo>','<ConsumerSeqNo>'+time.strftime( '%Y%m%d', time.localtime() )+time.strftime( '%H%M%S', time.localtime() )+'</ConsumerSeqNo>',MsgPack)
    MsgPack = MsgPack.replace(" ","").replace("xml","xml ").replace("encoding"," encoding")
    return MsgPack

