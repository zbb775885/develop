#!/usr/bin/python
#-*- coding:utf-8 *-*


import mysql.connector

global debugMysql
debugMysql = True

#获取当前主机有哪个几个数据库
def getDataBases(cursor):
    cursor.execute('show databases')
    dataBase = cursor.fetchall()
    dataBase = [tmp[0] for tmp in dataBase]
    if (True == debugMysql):
        print (dataBase)
    return dataBase

#使用数据库,注意传入的dataBase参数是tuple
def useDataBases(cursor, dataBase): 
    if (True == debugMysql):
        print ('table:', dataBase)
    sqlCmd = 'use ' + dataBase
    cursor.execute(sqlCmd)
    return 

#获取当前数据库的tables
def getDataTables(cursor, dataBase):
    useDataBases(cursor, dataBase)
    sqlCmd = 'show tables'
    cursor.execute(sqlCmd)
    tables = cursor.fetchall()
    tables = [tmp[0] for tmp in tables]
    if (True == debugMysql):
        print (tables)
    return tables

#获取当前数据表中的列的描述
def getTableDescription(cursor, table):
    sqlCmd = 'describe ' + table
    cursor.execute(sqlCmd)
    descs = cursor.fetchall()
    if (True == debugMysql):
        print ('Table %s descrption: ' %(table))
        for tmp in descs:
             print (' %s  ' %(tmp[0]))
    return descs
    
#获取当前数据表中的某一列的数据
def getDataFiled(cursor, field, table, cond = ''):
    sqlCmd = 'select ' + field + ' from ' + table + ' ' + cond
    cursor.execute(sqlCmd)
    datas = cursor.fetchall()
    if (True == debugMysql):
        print ('Filed %s descrption: ' %(field))
        for tmp in datas:
             print (' %s  ' %(tmp[0]))
    return datas
    
conn = mysql.connector.connect(host = '192.168.2.15', user = 'root', passwd = '123456', database = 'world')
cursor = conn.cursor()

dataBase = getDataBases(cursor)
for strBase in dataBase:
        print('  ')

dataTables = getDataTables(cursor, 'world')
#
for strTable in dataTables:
    print('  ')
    #getTableDescription(cursor, strTable)

getDataFiled(cursor, 'ID', 'city', 'where ID < 750')  
    
cursor.close()
conn.close()




