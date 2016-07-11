#!/usr/bin/python
#-*- coding:utf-8 *-*


from msTest import *
from tkinter import *
from tkinter.ttk import *
import types
import string
            
class MainFrame(Frame, OperMysql):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.grid(row=0, column=0, sticky="nsew")  
        self.createFrame() 
    
    def createFrame(self):
        ############################初始化输入框##########################
        #初始化IP输入框的Label
        self.IpLabel = Label(self, text = 'IP Addr', justify = 'left')
        self.IpLabel.grid(row = 0, column = 0, sticky='w')
        #初始化IP输入框的Text
        self.IpText = Text(self, width = 20, height = 1)
        self.IpText.insert(INSERT, '请输入主机IP地址')
        self.IpText.grid(row = 1, column = 0, sticky='w')
        
        #初始化用户输入框的Label
        self.UserLabel = Label(self, text = 'user', justify = 'left')
        self.UserLabel.grid(row = 2, column = 0, sticky='w')
        #初始化用户输入框的Text
        self.UserText = Text(self, width = 20, height = 1)
        self.UserText.insert(INSERT, '请输入登录用户')
        self.UserText.grid(row = 3, column = 0, sticky='w')
        
        #初始化密码输入框的Label
        self.PasswdLabel = Label(self, text = 'passwd', justify = 'left')
        self.PasswdLabel.grid(row = 4, column = 0, sticky='w')
        #初始化密码输入框的Text
        self.PasswdText = Text(self, width = 20, height = 1)
        self.PasswdText.insert(INSERT, '请输入登录密码')
        self.PasswdText.grid(row = 5, column = 0, sticky='w')
        
        #初始化Database输入框的Label
        self.DbLabel = Label(self, text = 'Database', justify = 'left')
        self.DbLabel.grid(row = 6, column = 0, sticky='w')
        #初始化Database输入框的Text
        self.DbText = Text(self, width = 20, height = 1)
        self.DbText.insert(INSERT, '请输入需使用的数据库')
        self.DbText.grid(row = 7, column = 0, sticky='w')
        
        #初始化表格输入框的Label
        self.TbLabel = Label(self, text = 'Table', justify = 'left')
        self.TbLabel.grid(row = 8, column = 0, sticky='w')
        #初始化表格输入框的Text
        self.TbText = Text(self, width = 20, height = 1)
        self.TbText.insert(INSERT, '请输入需使用的表格')
        self.TbText.grid(row = 9, column = 0, sticky='w')
        
        #初始化列输入框的Label
        self.ColLabel = Label(self, text = 'Column Item', justify = 'left')
        self.ColLabel.grid(row = 10, column = 0, sticky='w')
        #初始化列输入框的Text
        self.ColText = Text(self, width = 20, height = 1)
        self.ColText.insert(INSERT, '请输入操作的列表项')
        self.ColText.grid(row = 11, column = 0, sticky='w')
        
        #初始化显示区输入框的Label
        self.DisLabel = Label(self, text = 'Output', justify = 'left')
        self.DisLabel.grid(row = 12, column = 0, sticky='w')
        #初始化显示区输入框的Text
        self.DisText = Text(self, width = 90, height = 20)
        self.DisText.grid(row = 13, column = 0, sticky='w')
        
        ############################初始化按钮##########################
        self.GetDbsButton = Button(self, text = "GetDataBases", command = self.GetDbs)
        self.GetDbsButton.grid(row = 0, column = 1, sticky='w', in_ = self)      
        self.grid()
    def GetDbs(self):
        print('')
        
def main():
    root = Tk()
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.geometry('640x360')#设置主窗口的大小为640*360
    
    mFrame = MainFrame(root)
    mFrame.master.title('mysql 小工具')
    mFrame.mainloop()
    
if __name__== '__main__':
    #oper =  OperMysql(host = '192.168.2.15', user = 'root', passwd = '123456', database = 'world')     
    #oper.connectHost()
    #dataBase = oper.getDataBases(oper.cursor)
    #for strBase in dataBase:
    #        print('  ')
    #
    #dataTables = oper.getDataTables(oper.cursor, 'world')
    ##
    #for strTable in dataTables:
    #    print('  ')
    #    #getTableDescription(cursor, strTable)
    #
    #oper.getDataFiled(oper.cursor, 'ID', 'city', 'where ID < 750')  
    #oper.disconnectHost()
    main()
    
    
    
    
    
    
    
    
    
        
    
       
        
