#coding:gb18030

import pymongo
import MySQLdb

#�������ݿ�
def insertDb(query):
    conn = pymongo.MongoClient('192.168.1.5',27017)
    db = conn.lgw
    jobInfo = db.jobInfo
    jobInfo.insert(query)
    conn.close()
    
#��ѯ����
def insertMySQLDb(sql):
    try:
        conn = MySQLdb.connect(host='192.168.1.107', port=3306, user='root', passwd='123456', db='BBS')
#    except MySQLdb.Error, e:
#        return 0,e,None,None
#    try:
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
        return 1,'Success',None,None
#returnֵ������״̬��0��ʧ�ܣ�1���ɹ���2��δ��ѯ�����ݣ�
    except MySQLdb.Error, e:
        return 0,'e',None,None



'''
create table jobinfo(
   id INT NOT NULL AUTO_INCREMENT,
   companyName VARCHAR(30),
   jobBasicInformation VARCHAR(100),
   jobAttract VARCHAR(1000),
   jobDescription VARCHAR(2000),
   PRIMARY KEY ( id )
);
'''