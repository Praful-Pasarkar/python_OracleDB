import cx_Oracle
import os

def dwdb():
    os.environ['TNS_ADMIN']=r"C:\instantclient_19_6\network\admin_dw"
    connection1 = cx_Oracle.connect('username', 'password', 'devdwdb_low')
    mysql1= """select sysdate from dual"""
    cursor = connection1.cursor()
    cursor.execute(mysql1)
    result = cursor.fetchone()
    print(result)
    connection1.close()

def trxdb():
    os.environ['TNS_ADMIN']=r"C:\instantclient_19_6\network\admin_trx"
    connection2 = cx_Oracle.connect('username', 'password', 'devtrxdb_low')
    mysql1= """select sysdate from dual"""
    cursor = connection2.cursor()
    cursor.execute(mysql1)
    result = cursor.fetchone()
    print(result)
    connection2.close()

dwdb()
trxdb()
