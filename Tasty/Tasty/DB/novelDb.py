#coding:utf-8
import MySQLdb


#查询操作
def queryDb(sql,fetchNum='fetchall',host='115.28.6.1', port=3306, user='root', passwd='123456', db='tasty'):
    try:
        conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db,charset='utf8')
    except MySQLdb.Error, e:
        return 0,e,None,None
    cur = conn.cursor()
    dataCount = cur.execute(sql)
    if fetchNum == 'fetchall':
        info = cur.fetchall()
    else:
        info = cur.fetchmany(fetchNum)
    cur.close()
    conn.close()
#return值：返回状态（0：失败，1：成功，2：未查询到数据），返回信息，查询到数据总数，查询到数据
    if dataCount == 0:
        return 2,'Success',0,None
    else:
        return 1,'Success',dataCount,info
#插入操作
def insertMySQLDb(sql):
    try:
        conn = MySQLdb.connect(host='115.28.6.1', port=3306, user='root', passwd='123456', db='tasty',charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
        return 1,'Success',None,None
#return值：返回状态（0：失败，1：成功，2：未查询到数据）
    except MySQLdb.Error, e:
        return 0,'e',None,None

'''#插入一条数据
sqli="insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

cur.close()
conn.commit()
conn.close()

'''
'''
create table novel_novel(
   id INT NOT NULL AUTO_INCREMENT,
   novelname VARCHAR(60),
   author varchar(100),
   workdate VARCHAR(8),
   worktime varchar(6),
   url varchar(200),
   ext1 varchar(200),
   ext2 varchar(200),
   PRIMARY KEY ( id )
);


create table novel_noveldetail(
   id INT NOT NULL AUTO_INCREMENT,
   novel_id INT,
   chapter_name varchar(200),
   chapter_text MEDIUMTEXT,
   PRIMARY KEY ( id )
);
'''

