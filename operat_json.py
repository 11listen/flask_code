#coding: utf-8

import MySQLdb
import json

#connect db
db = MySQLdb.connect("192.168.0.107", "admin_zone", "xxxxxx", "detection")

#get vernier
cursor = db.cursor()

#sql statement
db_sql = """
        CREATE TABLE iptable (
        user char(20) not null,
        job char(20) not null,
        mac char(48) not null,
        ip char(64) not null,
        description char(128)
        )
        """
#execute sql
data = cursor.execute( """
show tables like 'iptable'
""")

#if db not exists, create db, else, insert sql statement
try:
    if data == 0:
        cursor.execute(db_sql)
        print "db is create"
except:
        print "db is exist, the data will insert db"

#dynamically inserted into the datebase
def operate(operation):
    operate_json = operation
    json_str = json.dumps(operate_json)
    date_encode = json_str.encode('utf-8')
    value = eval(date_encode)
    sql = """INSERT INTO iptable VALUES (%(mac)s, %(ip)s)"""
    try:
        cursor.execute(sql, value)
        db.commit()
        print 'success json has been insert db'
    except:
        db.rollback()
        print 'error, please check your operat'
