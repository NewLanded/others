# -*- coding: utf-8 -*-
'''
功    能：    用Python的Socket实现的Natp通讯客户端
作    者：    陈 显 明
修改时间：    20071113 by 刘宇英
修改时间：    20090112  刘宇英重写
全局变量：
        self.gRequestData 存储请求数据
        self.response     存储响应数据
'''
import struct, socket, array
class MyNatpClient(object):
    def __init__(self):
        self.gRequestData = None
        self.response = None
    
        self.crc32_tab = array.array( 'L', [
            0x00000000, 0x77073096, 0xee0e612c, 0x990951ba, 0x076dc419, 0x706af48f, 0xe963a535, 0x9e6495a3,
            0x0edb8832, 0x79dcb8a4, 0xe0d5e91e, 0x97d2d988, 0x09b64c2b, 0x7eb17cbd, 0xe7b82d07, 0x90bf1d91,
            0x1db71064, 0x6ab020f2, 0xf3b97148, 0x84be41de, 0x1adad47d, 0x6ddde4eb, 0xf4d4b551, 0x83d385c7,
            0x136c9856, 0x646ba8c0, 0xfd62f97a, 0x8a65c9ec, 0x14015c4f, 0x63066cd9, 0xfa0f3d63, 0x8d080df5,
            0x3b6e20c8, 0x4c69105e, 0xd56041e4, 0xa2677172, 0x3c03e4d1, 0x4b04d447, 0xd20d85fd, 0xa50ab56b,
            0x35b5a8fa, 0x42b2986c, 0xdbbbc9d6, 0xacbcf940, 0x32d86ce3, 0x45df5c75, 0xdcd60dcf, 0xabd13d59,
            0x26d930ac, 0x51de003a, 0xc8d75180, 0xbfd06116, 0x21b4f4b5, 0x56b3c423, 0xcfba9599, 0xb8bda50f,
            0x2802b89e, 0x5f058808, 0xc60cd9b2, 0xb10be924, 0x2f6f7c87, 0x58684c11, 0xc1611dab, 0xb6662d3d,
            0x76dc4190, 0x01db7106, 0x98d220bc, 0xefd5102a, 0x71b18589, 0x06b6b51f, 0x9fbfe4a5, 0xe8b8d433,
            0x7807c9a2, 0x0f00f934, 0x9609a88e, 0xe10e9818, 0x7f6a0dbb, 0x086d3d2d, 0x91646c97, 0xe6635c01,
            0x6b6b51f4, 0x1c6c6162, 0x856530d8, 0xf262004e, 0x6c0695ed, 0x1b01a57b, 0x8208f4c1, 0xf50fc457,
            0x65b0d9c6, 0x12b7e950, 0x8bbeb8ea, 0xfcb9887c, 0x62dd1ddf, 0x15da2d49, 0x8cd37cf3, 0xfbd44c65,
            0x4db26158, 0x3ab551ce, 0xa3bc0074, 0xd4bb30e2, 0x4adfa541, 0x3dd895d7, 0xa4d1c46d, 0xd3d6f4fb,
            0x4369e96a, 0x346ed9fc, 0xad678846, 0xda60b8d0, 0x44042d73, 0x33031de5, 0xaa0a4c5f, 0xdd0d7cc9,
            0x5005713c, 0x270241aa, 0xbe0b1010, 0xc90c2086, 0x5768b525, 0x206f85b3, 0xb966d409, 0xce61e49f,
            0x5edef90e, 0x29d9c998, 0xb0d09822, 0xc7d7a8b4, 0x59b33d17, 0x2eb40d81, 0xb7bd5c3b, 0xc0ba6cad,
            0xedb88320, 0x9abfb3b6, 0x03b6e20c, 0x74b1d29a, 0xead54739, 0x9dd277af, 0x04db2615, 0x73dc1683,
            0xe3630b12, 0x94643b84, 0x0d6d6a3e, 0x7a6a5aa8, 0xe40ecf0b, 0x9309ff9d, 0x0a00ae27, 0x7d079eb1,
            0xf00f9344, 0x8708a3d2, 0x1e01f268, 0x6906c2fe, 0xf762575d, 0x806567cb, 0x196c3671, 0x6e6b06e7,
            0xfed41b76, 0x89d32be0, 0x10da7a5a, 0x67dd4acc, 0xf9b9df6f, 0x8ebeeff9, 0x17b7be43, 0x60b08ed5,
            0xd6d6a3e8, 0xa1d1937e, 0x38d8c2c4, 0x4fdff252, 0xd1bb67f1, 0xa6bc5767, 0x3fb506dd, 0x48b2364b,
            0xd80d2bda, 0xaf0a1b4c, 0x36034af6, 0x41047a60, 0xdf60efc3, 0xa867df55, 0x316e8eef, 0x4669be79,
            0xcb61b38c, 0xbc66831a, 0x256fd2a0, 0x5268e236, 0xcc0c7795, 0xbb0b4703, 0x220216b9, 0x5505262f,
            0xc5ba3bbe, 0xb2bd0b28, 0x2bb45a92, 0x5cb36a04, 0xc2d7ffa7, 0xb5d0cf31, 0x2cd99e8b, 0x5bdeae1d,
            0x9b64c2b0, 0xec63f226, 0x756aa39c, 0x026d930a, 0x9c0906a9, 0xeb0e363f, 0x72076785, 0x05005713,
            0x95bf4a82, 0xe2b87a14, 0x7bb12bae, 0x0cb61b38, 0x92d28e9b, 0xe5d5be0d, 0x7cdcefb7, 0x0bdbdf21,
            0x86d3d2d4, 0xf1d4e242, 0x68ddb3f8, 0x1fda836e, 0x81be16cd, 0xf6b9265b, 0x6fb077e1, 0x18b74777,
            0x88085ae6, 0xff0f6a70, 0x66063bca, 0x11010b5c, 0x8f659eff, 0xf862ae69, 0x616bffd3, 0x166ccf45,
            0xa00ae278, 0xd70dd2ee, 0x4e048354, 0x3903b3c2, 0xa7672661, 0xd06016f7, 0x4969474d, 0x3e6e77db,
            0xaed16a4a, 0xd9d65adc, 0x40df0b66, 0x37d83bf0, 0xa9bcae53, 0xdebb9ec5, 0x47b2cf7f, 0x30b5ffe9,
            0xbdbdf21c, 0xcabac28a, 0x53b39330, 0x24b4a3a6, 0xbad03605, 0xcdd70693, 0x54de5729, 0x23d967bf,
            0xb3667a2e, 0xc4614ab8, 0x5d681b02, 0x2a6f2b94, 0xb40bbe37, 0xc30c8ea1, 0x5a05df1b, 0x2d02ef8d
        ] )
    
    def setHead(self,Transcode, TemplateCode, ReservedCode = '00000'):
        '''
        Transcode     交易代码
        TemplateCode  模版代码
        ReservedCode  保留代码
        参数规格：右补空格到20字节
        功   能：组织natp报文头
        '''
        
        #====数据打包2进制16+20字节交易代码＋20字节模板代码＋20字节保留代码
        self.gRequestData = struct.pack('>B', 16) + self.rFillWithBlank(Transcode, 20) + self.rFillWithBlank(TemplateCode, 20) + self.rFillWithBlank(ReservedCode, 20)
    
    def addField(self,fieldName, fieldValue):
        '''
        添加自定义数据域到Natp报文中
        fieldName  字段名称
        fieldValue 字段值
        '''
        #====定义全局变量存储请求数据
        
        #====判断是否存在请求数据
        if(self.gRequestData is None):
            print '没有设置NATP报文协议头!'
            return
        #====判断单包大小是否超过4k
        if((len(self.gRequestData) + len(fieldName) + len(fieldValue) + 4) > 4086):
            print '待发送数据量超出缓冲区允许的大小'
            return
        #====报文头＋报文字段名称长度（16进制编码）＋报文名称＋报文字段值长度（16进制编码）＋报文字段值
        self.gRequestData = self.gRequestData + struct.pack('>H', len(fieldName)) + fieldName \
                + struct.pack('>H', len(fieldValue)) + fieldValue
    
    def sendReqData(self,connection, reqdata):
        '''
        发送请求数据
        connection 连接
        reqdata    请求数据
        '''
        try:
            #====判断数据发送模式
            if hasattr(connection, "sendall"):
                #====发送所有数据
                connection.sendall(reqdata)
            else:
                #====已经发送的数据长度
                sentsofar = 0
                #====获取待发数据长度
                left = len(reqdata)
    
                #====判断数据是否发送完毕
                while left > 0:
                    #====发送所有数据
                    sent = connection.send(reqdata[sentsofar:])
                    #====标识已经发送的数据
                    sentsofar = sentsofar + sent
                    #====获取待发数据长度
                    left = left - sent
        #====处理发送异常
        except socket.error:
            print '发送NATP请求数据(' + reqdata + ')失败.'
    
    def sendRequest(self,ipAddress, port, timeout, respflag = 'True'):
        '''
        发送给定的数据到Natp服务端,并拆分返回的结果
        ipAddress  ip地址
        port       目标机端口
        timeout    超时时间
        '''
        
        
        #====判断是否存在请求数据
        if(self.gRequestData is None):
            print '没有待发送数据!'
            return None
        #====创建socket连接
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(timeout)
        connection.connect((ipAddress, port))
    
        #====通讯报文头规格
        #===dataIndex      数据位置
        #===reqdata        请求数据
        #===reqSeq         请求队列
        #===nextPacketFlag 多包数据标识
        dataIndex, reqdata, reqSeq, nextPacketFlag  = 0, None, 1, 1
        #===判断是否存在多包数据
        while(nextPacketFlag == 1):
            #====发送数据包
            if(dataIndex + 4086 < len(self.gRequestData)):
                #====reqdata取所有数据
                reqdata = struct.pack('>BBBBH', 1, 0, nextPacketFlag, 0, reqSeq) + self.gRequestData[dataIndex : dataIndex+4086]
                #====数据标识改为4082开始
                dataIndex = dataIndex + 4086
            #====如果请求数据大于4k
            else:
                #====设定下包标识为0
                nextPacketFlag = 0
                #====将新数据组合成格式化请求数据头
                reqdata = struct.pack('>BBBBH', 1, 0, nextPacketFlag, 0, reqSeq) + self.gRequestData[dataIndex : len(self.gRequestData) - dataIndex]
                #====数据标识为请求数据总长度
                dataIndex = len(self.gRequestData)
            #====数据加押
            reqdata = reqdata + struct.pack('>L', self.getCrc32(reqdata))
            #====数据长度(包含8位数据押)＋数据＋数据押
            reqdata = struct.pack('>L', len(reqdata)) + reqdata
            #====发送数据
            self.sendReqData(connection, reqdata)
            #====请求队列申请
            reqSeq = reqSeq + 1
            #====单包数据的情况
            if(nextPacketFlag == 1):
                #====接收到的数据为空
                if(self.recvRespData(connection) == None):
                    connection.close()
                    return []
    
        if respflag == 'True':
            #====接收响应数据
            nextPacketFlag, self.responseData = 1, ""
            #===单包数据
            while(nextPacketFlag == 1):
                #====接收数据包
                respdata = self.recvRespData(connection)
                #====接收到的数据为空
                if(respdata == None):
                    connection.close()
                    return []
                #====实际返回结果数据，前4字节为返回报文长度
                self.responseData = self.responseData + respdata[10:len(respdata)-4]
                #====获取多包标识
                nextPacketFlag = struct.unpack('>B', respdata[6])[0]
                #====数据接收完毕
                if(nextPacketFlag == 1):
                    #====返回接收确认
                    protodata = struct.pack('>BBBBHBBBB', 1, 1, 0, 0, struct.unpack('>H', respdata[8:10])[0] + 1, 0, 0, 0, 0)
                    #====CRC校验
                    protodata = protodata + struct.pack('>L', self.getCrc32(protodata))
                    #====包长度
                    protodata = struct.pack('>L', len(protodata)) + protodata
                    self.sendReqData(connection, protodata)
            #====关闭连接
            connection.close()
    
            #====处理返回结果
            self.response=[]
            #====替换前60字节交易代码，模版代码，备用字段信息
            self.response.append(['TransCode', self.rStripBlank(self.responseData[1 : 21])])
            self.response.append(['TemplateCode', self.rStripBlank(self.responseData[21 : 41])])
            self.response.append(['ReservedCode', self.rStripBlank(self.responseData[41 : 61])])
            #====获取返回结果数据
            fileds = self.responseData[61 : len(self.responseData)]
            #====将返回数据进行拆包添加到self.response列表中
            while(len(fileds)>0):
                #====取字段名称长度
                fieldNameLen = struct.unpack('>H', fileds[0:2])[0]
                #====取字段名称
                fieldName = fileds[2 : 2 + fieldNameLen]
                #====截取剩余字段
                fileds = fileds[2 + fieldNameLen :]
                fieldValueLen = struct.unpack('>H', fileds[0:2])[0]
                fieldValue = fileds[2 : 2 + fieldValueLen]
                fileds = fileds[2 + fieldValueLen :]
                self.response.append([fieldName, fieldValue])
            return self.response
        else:
            #====关闭连接
            connection.close()
            return True
    
    
    def receiveBytes(self,connection, num):
        '''
        判断接收数据长度
        connection 连接
        num        数据长度
        '''
        #====定义全局变量存储接收次数
        retries = 0
        #====接收指定长度的数据
        try:
            lenChunk = connection.recv(num)
        except socket.timeout:
            return None
        #====接收次数小于5，接收数据小于设置的num长度时，进行数据接收
        while((retries < 5) and (len(lenChunk) < num)):
            #====接收定长数据
            retries = retries + 1
            print 'retries=', retries, len(lenChunk)
            #====接收其余数据
            lenChunk = lenChunk + connection.recv(num - len(lenChunk))
        #====接收的数据小于num的长度
        if(len(lenChunk) != num):
            print '接收数据异常:  (', len(lenChunk), "<", num, ")"
            return None
        return lenChunk
    
    def recvRespData(self,connection):
        '''
        接收响应数据
        connection 连接
        '''
        #====按4字节接收定长数据,标识返回结果长度
        lenChunk = self.receiveBytes(connection, 4)
        if(len(lenChunk) != 4):
            print '接收数据长度异常.', len(lenChunk)
            return None
        #====获取字符串长度(长整形)
        slen = struct.unpack('>L', lenChunk)[0]
        #====接收定长字节数据
        dataChunk = self.receiveBytes(connection, slen)
        if(len(dataChunk) != slen):
            print '接收数据内容异常.'
            return None
        #====对收到的数据进行8位crc校验
        if(self.getCrc32(dataChunk[0 : slen-4]) != struct.unpack('>L', dataChunk[slen-4 : slen])[0]):
            print "接收数据CRC校验异常"
            return None
        #====返回接收到的定长数据的字节数和字节数据
        return lenChunk + dataChunk
    
    
    def getField(self,fieldName, iPos=0):
        '''
        获取返回字段变量值
        fieldName 字段名称
        iPos      变量出现次数
        '''
        #=====定义全局变量存储返回数据
        
        #=====初始化返回数据列表
        retData=[]
        #=====判断返回数据是否为空
        if(self.response is None):
            print '返回报文非法!'
            return ''
        #=====拆分返回变量
        i=1
        for fields in self.response:
            if fields[0]==fieldName:
                if iPos>0 :
                    if i==iPos:
                        return fields[1]
                    i=i+1
                else:
                    #====如果字段值的序号小于0，直接返回第一个值
                    retData.append(fields[1])
        #====如果字段值的序号大于结果值的最大序号，直接返回空
        if iPos>0 :
            return ''
        return retData
    
    def getCrc32(self,srcStr ):
        '''
        获取8位crc32校验码的值
        '''
        i = 0
        crc = 0xFFFFFFFFL
        while( i < len( srcStr ) ):
            temp1 = ( crc >> 8 ) & 0x00FFFFFFL;
            temp2 = self.crc32_tab[( crc ^ ( struct.unpack( 'B', srcStr[i] )[0] ) ) & 0xFF]
            crc = temp1 ^ temp2
            i = i + 1
        return crc
    
    def rFillWithChar(self, srcString, totalLength, fillChar ):
        '''
        用指定的字符从右边填充字符串到指定的长度
        '''
        srcLen = len( srcString )
        if( srcLen > totalLength ):
            print "Error: string too long,can't fill(", srcLen, ">", totalLength, ")!"
            return None
        if( srcLen == totalLength ):
            return srcString
    
        if( srcLen < totalLength ):
            result = srcString
            while( srcLen < totalLength ):
                result = result + fillChar
                srcLen = srcLen + 1
            return result
    
    def rFillWithBlank(self, srcString, totalLength ):
        '''
        字符串右填充空格
        '''
        return self.rFillWithChar(srcString, totalLength, ' ' )
    
    def rStripBlank(self, srcString ):
        '''
        字符串右删除空格
        '''
        return self.rStripChar( srcString , ' ' )
    
    def rStripChar(self, srcString , stripChar ):
        index = len( srcString )
        while( srcString[index - 1] == stripChar ):
            index = index - 1
        return srcString[:index]


