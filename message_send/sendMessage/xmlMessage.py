# -*- coding: utf-8 -*-
import os,re,time

workdate = time.strftime( '%Y%m%d', time.localtime() )
worktime = time.strftime( '%H%M%S', time.localtime() )

data = {
'q012':'''
<?xml version="1.0" encoding="UTF-8"?>
<service>
<SYS_HEAD>
<ServiceCode>12003000001</ServiceCode>
<ServiceScene>20</ServiceScene>
<ConsumerId>10100700</ConsumerId>
<TargetId>60100100</TargetId>
<ChannelTyp>67</ChannelTyp>
<OrgConsumerId>10100700</OrgConsumerId>
<OrgConsumerSeqNo>101007002016072702580043</OrgConsumerSeqNo>
<TranMode></TranMode>
<TranDate>%s</TranDate>
<TranTime>%s</TranTime>
<ConsumerSeqNo>%s</ConsumerSeqNo>
<TerminalCode></TerminalCode>
<OrgTerminalCode></OrgTerminalCode>
<ConsumerSvrId></ConsumerSvrId>
<OrgConsumerSvrId>10100700</OrgConsumerSvrId>
<DestSvrId></DestSvrId>
<UserLang></UserLang>
<FilFlg>0</FilFlg>
<FilPath></FilPath>
<BusiSmyCd></BusiSmyCd>
</SYS_HEAD>
<APP_HEAD>
<TellerNo>HS0005651</TellerNo>
<BranchId>10203</BranchId>
<TellerPassword></TellerPassword>
<TellerLevel></TellerLevel>
<TellerType></TellerType>
<ApprFlag></ApprFlag>
<array></array>
<AuthFlag></AuthFlag>
<array></array>
</APP_HEAD>
<BODY>
<InqMode>1</InqMode>
<CusNo>110805054</CusNo>
<SysId>10100700</SysId>
<CusNm></CusNm>
<IdentTyp></IdentTyp>
<IdentNo></IdentNo>
<ActNo></ActNo>
<AgrTyp></AgrTyp>
<BegRcrdCnt>1</BegRcrdCnt>
<InqRcrdCnt>20</InqRcrdCnt>
<Flg1></Flg1>
<VerfLo></VerfLo>
<RsrvInf1></RsrvInf1>
<Amt1></Amt1>
</BODY>
</service>
'''%(workdate,worktime,workdate+worktime),
'q015':'''
<?xml version="1.0" encoding="UTF-8"?>
<service>
<SYS_HEAD>
<ServiceCode>12003000006</ServiceCode>
<ServiceScene>03</ServiceScene>
<ConsumerId>10100700</ConsumerId>
<TargetId>60100100</TargetId>
<ChannelTyp>67</ChannelTyp>
<OrgConsumerId>10100700</OrgConsumerId>
<OrgConsumerSeqNo>101007002016080202439946</OrgConsumerSeqNo>
<TranMode></TranMode>
<TranDate>%s</TranDate>
<TranTime>%s</TranTime>
<ConsumerSeqNo>%s</ConsumerSeqNo>
<TerminalCode></TerminalCode>
<OrgTerminalCode></OrgTerminalCode>
<ConsumerSvrId></ConsumerSvrId>
<OrgConsumerSvrId>10100700</OrgConsumerSvrId>
<DestSvrId></DestSvrId>
<UserLang></UserLang>
<FilFlg>0</FilFlg>
<FilPath></FilPath>
<BusiSmyCd></BusiSmyCd>
</SYS_HEAD>
<APP_HEAD>
<TellerNo>HS0005651</TellerNo>
<BranchId>10203</BranchId>
<TellerPassword></TellerPassword>
<TellerLevel></TellerLevel>
<TellerType></TellerType>
<ApprFlag></ApprFlag>
<array></array>
<AuthFlag></AuthFlag>
<array></array>
</APP_HEAD>
<BODY>
<NtwPntBrNo>10203</NtwPntBrNo>
<BusTyp>s</BusTyp>
<RsrvFld></RsrvFld>
<RsrvFld1></RsrvFld1>
<Flg1></Flg1>
<VerfLo></VerfLo>
<RsrvInf1></RsrvInf1>
<RsrvInf2></RsrvInf2>
<Amt1></Amt1>
<Amt2></Amt2>
</BODY>
</service>
'''%(workdate,worktime,workdate+worktime),
'natp_q016':'''
ServiceCode::inf,
ServiceScene::q016,
ChannelTyp::13,
OrgConsumerSeqNo::101003002016072200790886,
TellerNo::9698,
BranchId::10203,
TransServiceCode::cip.inf.q016.01,
ConsumerId::10020,
TranDate::%s,
TranTime::%s,
ConsumerSeqNo::%s,
OrgConsumerSvrId::PBANK001,
FilFlg::0,
NtwPntBrNo::10203,
QuNo::a101,
IdentTyp::01,
ActNo::6217751010000111884,
InqMode::3
'''%(workdate,worktime,workdate+worktime),
'e009':'''
<?xml version="1.0" encoding="gb2312"?>
<Service>
	<SYS_HEAD>
		<ServiceCode>12002000013</ServiceCode>
		<FilFlg>0</FilFlg>
		<ChannelTyp>13</ChannelTyp>
		<ServiceScene>01</ServiceScene>
		<ConsumerId>01</ConsumerId>
		<RequestDate>20160721</RequestDate>
		<OrgConsumerSvrId>CARDXP01</OrgConsumerSvrId>
		<TranDate>%s</TranDate>
		<TranTime>%s</TranTime>
		<RequestTime>121740</RequestTime>
		<ConsumerSeqNo>%s</ConsumerSeqNo>
		<OrgConsumerSeqNo>121709</OrgConsumerSeqNo>
		<ConsumerIP>127.0.0.1</ConsumerIP>
		<ServerIP>192.168.1.40</ServerIP>
		<TranMode>1</TranMode>
		<MacValue>12</MacValue>
		<Reserve>11</Reserve>
	</SYS_HEAD>
	<APP_HEAD>
		<ApprFlag></ApprFlag>
		<TellerLevel></TellerLevel>
		<TellerPassword></TellerPassword>
		<AuthFlag>0</AuthFlag>
		<TellerType></TellerType>
		<TellerNo>0463</TellerNo>
		<BranchId>10224</BranchId>
		<array>
			<ApprTellerArray>
				<ApprTellerType></ApprTellerType>
				<ApprTellerNo></ApprTellerNo>
				<ApprTellerLevel></ApprTellerLevel>
				<ApprBranchId></ApprBranchId>
			</ApprTellerArray>
		</array>
	</APP_HEAD>
	<BODY>
                <RcrdCnt>1</RcrdCnt>
		<BkgNtwPntBrNo>1217</BkgNtwPntBrNo>        
		<BkgPcsDt>20160726</BkgPcsDt>                   
		<BkgNo>9240</BkgNo>                       
		<AgncFlg>1</AgncFlg>                    
		<CusNm>马亚明</CusNm>                   
		<IdentTyp>01</IdentTyp>									
		<IdentNo>110222198805180888</IdentNo>   
		<MblNum>15652777129</MblNum>            
		<AgNm>栓柱</AgNm>                           
		<AgIdTyp>01</AgIdTyp>          
		<AgIdNo>111111111111111111</AgIdNo>    				 
		<AgMblNum>01234567890</AgMblNum>        
		<RetCnt>1</RetCnt>           
		<array>
			<BkgShdInfo>
				<BusiNm>开户</BusiNm>
				<BsnId>1020001</BsnId>
				<array>	
				      <ShdCntntInfo>
				      	<NAME>渠道协同一</NAME>   
				      	<SEX>3-女性</SEX>         
				      	<DATEOFBIRTH>19880728</DATEOFBIRTH>  
				      	<REASON></REASON>                  
				      	<DOCUMENTTYPE>01</DOCUMENTTYPE>      
				      	<IDNUMBER>340121198807284342</IDNUMBER>   
				      	<TELNUM>15209827067</TELNUM>              
				      	<NATIONALITY>156</NATIONALITY>           
				      	<PROFESSIONAL>00100</PROFESSIONAL>   
				      	<JOB></JOB>                                    
				      	<IDINDATE>2026-04-12</IDINDATE>           
				      	<IDAUTHORITY></IDAUTHORITY>     
				      	<ADRRESS>合肥滨湖</ADRRESS>       
				      	<AGENTNAME></AGENTNAME>  	    
				      	<AGENTSEX></AGENTSEX>         
				      	<RELATIONPEOPLE></RELATIONPEOPLE>  	  
				      	<REASON></REASON>       						  
				      	<AGENTDOCUMENTTYPE></AGENTDOCUMENTTYPE> 
				      	<AGENTIDNUMBER></AGENTIDNUMBER>         
				      	<AGENTTEL></AGENTTEL>                  
				      	<AGENTNATIONALITY></AGENTNATIONALITY>  
				      	<AGENTPROFESSION></AGENTPROFESSION>    
				      	<AGENTWORKPLACE></AGENTWORKPLACE>      
				      	<AGENTIDINDATE></AGENTIDINDATE>        
				      	<AGENTIDAUTHORITY></AGENTIDAUTHORITY>  
				      	<AGENTADDRESS></AGENTADDRESS>          
				      	<CONTRACTSIGN>85214563</CONTRACTSIGN>  
				      	<QYTELNUM>15652777129</QYTELNUM>       
				      	<REVNAME></REVNAME>                    
				      	<ACCTNO></ACCTNO>                      
				      	<CCY></CCY>                            
				      	<AMT></AMT>                            
				      </ShdCntntInfo>
				</array>      
			</BkgShdInfo>
		</array>
		<Amt1/>
		<Flg1/>
		<VerfLo/>
		<RsrvInf1/>
	</BODY>
</Service>
'''%(workdate,worktime,workdate+worktime),
}
