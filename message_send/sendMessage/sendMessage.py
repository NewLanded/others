#coding:utf-8

from bottle import Bottle, run,request
from bottle import static_file
from bottle import template
from function import basicInfo
from sendXml import sendXml,dataHandle
from sendNatp import sendNatp

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/')
def index():
    allData = basicInfo()
    allXmlData = allData[0]
    allNatpData = allData[1]
    return template('all',xmlInfo=allXmlData,natpInfo=allNatpData)

@app.route('/sendOneXml/',method = 'POST')
def sendOneXml():
    xmlData = request.forms.get('xml',0)
    xmlData = xmlData.decode('utf-8').encode('gbk')
    xmlData = dataHandle(xmlData)
    returnXmlData = sendXml(xmlData)
    return returnXmlData

@app.route('/sendOneNatp/',method = 'POST')
def sendOneNatp():
    natpData = request.forms.get('natp',0)
    result = sendNatp(natpData)
    returnNatpData = ''
    for i in result:
        returnNatpData = returnNatpData + "字段:" + str(i[0]).decode('gb18030').encode('utf-8') + ", 值 : " + str(i[1]).decode('gb18030').encode('utf-8') + "\n"
    return returnNatpData

@app.route('/static/jquery-3.0.0.js')
def getJquery():
    return static_file('jquery-3.0.0.js', root='./static')

@app.route('/static/xml.js')
def getJquery():
    return static_file('xml.js', root='./static')

run(app ,host='', port=8888)
