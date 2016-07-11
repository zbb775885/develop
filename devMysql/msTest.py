#!/usr/bin/python
#-*- coding:utf-8 -*-


import mysql.connector

global debugMysql
debugMysql = True

#操作mysql列表
class OperMysql(object):
    def __init__(self, host = '192.168.2.15', user = 'root', passwd = '123456', database = 'world'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
    
    #获取当前主机有哪个几个数据库
    def getDataBases(self, cursor):
        cursor.execute('show databases')
        dataBase = cursor.fetchall()
        dataBase = [tmp[0] for tmp in dataBase]
        if (True == debugMysql):
            print (dataBase)
        return dataBase

    #使用数据库,注意传入的dataBase参数是tuple
    def useDataBases(self, cursor, dataBase): 
        if (True == debugMysql):
            print ('table:', dataBase)
        sqlCmd = 'use ' + dataBase
        cursor.execute(sqlCmd)
        return 

    #获取当前数据库的tables
    def getDataTables(self, cursor, dataBase):
        self.useDataBases(cursor, dataBase)
        sqlCmd = 'show tables'
        cursor.execute(sqlCmd)
        tables = cursor.fetchall()
        tables = [tmp[0] for tmp in tables]
        if (True == debugMysql):
            print (tables)
        return tables

    #获取当前数据表中的列的描述
    def getTableDescription(self, cursor, table):
        sqlCmd = 'describe ' + table
        cursor.execute(sqlCmd)
        descs = cursor.fetchall()
        if (True == debugMysql):
            print ('Table %s descrption: ' %(table)) 
            for tmp in descs:
                 print (' %s  ' %(tmp[0]))
        return descs
        
    #获取当前数据表中的某一列的数据
    def getDataFiled(self, cursor, field, table, cond = ''):
        sqlCmd = 'select ' + field + ' from ' + table + ' ' + cond
        cursor.execute(sqlCmd)
        datas = cursor.fetchall()
        if (True == debugMysql):
            print ('Filed %s descrption: ' %(field))
            for tmp in datas:
                 print (' %s  ' %(tmp[0]))
        return datas

    def connectHost(self):
        self.conn = mysql.connector.connect(host = self.host , user = self.user, passwd = self.passwd, database = self.database)
        self.cursor = self.conn.cursor()
        
    def disconnectHost(self):           
        self.cursor.close()
        self.conn.close()
       
                
            
            
if __name__=='__main__':
    oper =  OperMysql(host = '192.168.2.15', user = 'root', passwd = '123456', database = 'world')     
    oper.connectHost()
    dataBase = oper.getDataBases(oper.cursor)
    for strBase in dataBase:
            print('  ')

    dataTables = oper.getDataTables(oper.cursor, 'world')
    #
    for strTable in dataTables:
        print('  ')
        #getTableDescription(cursor, strTable)

    oper.getDataFiled(oper.cursor, 'ID', 'city', 'where ID < 750')  
    oper.disconnectHost()
    
    
    
    
    
    
    
    
    
        
    
       
        