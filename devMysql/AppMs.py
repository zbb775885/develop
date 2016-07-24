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
        self.sqlBase = None
    def createFrame(self):
        ############################初始化输入框##########################
        #初始化IP输入框的Label
        self.IpLabel = Label(self, text = 'IP Addr', justify = 'left')
        self.IpLabel.grid(row = 0, column = 0, sticky=W)
        #初始化IP输入框的Text
        self.IpText = Text(self, width = 20, height = 1)
        self.IpText.insert(INSERT, '192.168.2.210')
        self.IpText.grid(row = 1, column = 0, sticky=W)
        
        #初始化用户输入框的Label
        self.UserLabel = Label(self, text = 'user', justify = 'left')
        self.UserLabel.grid(row = 2, column = 0, sticky=W)
        #初始化用户输入框的Text
        self.UserText = Text(self, width = 20, height = 1)
        self.UserText.insert(INSERT, 'root')
        self.UserText.grid(row = 3, column = 0, sticky=W)
        
        #初始化密码输入框的Label
        self.PasswdLabel = Label(self, text = 'passwd', justify = 'left')
        self.PasswdLabel.grid(row = 4, column = 0, sticky=W)
        #初始化密码输入框的Text
        self.PasswdText = Text(self, width = 20, height = 1)
        self.PasswdText.insert(INSERT, '123456')
        self.PasswdText.grid(row = 5, column = 0, sticky=W)
        
        #初始化Database输入框的Label
        self.DbLabel = Label(self, text = 'Database', justify = 'left')
        self.DbLabel.grid(row = 6, column = 0, sticky=W)
        #初始化Database输入框的Text
        self.DbText = Text(self, width = 20, height = 1)
        self.DbText.insert(INSERT, 'mysql')
        self.DbText.grid(row = 7, column = 0, sticky=W)
        
        #初始化表格输入框的Label
        self.TbLabel = Label(self, text = 'Table', justify = 'left')
        self.TbLabel.grid(row = 8, column = 0, sticky=W)
        #初始化表格输入框的Text
        self.TbText = Text(self, width = 20, height = 1)
        self.TbText.insert(INSERT, 'db')
        self.TbText.grid(row = 9, column = 0, sticky=W)
        
        #初始化列输入框的Label
        self.ColLabel = Label(self, text = 'Column Item', justify = 'left')
        self.ColLabel.grid(row = 10, column = 0, sticky=W)
        #初始化列输入框的Text
        self.ColText = Text(self, width = 20, height = 1)
        self.ColText.insert(INSERT, 'Db')
        self.ColText.grid(row = 11, column = 0, sticky=W)
        
        #初始化显示区输入框的Label
        self.DisLabel = Label(self, text = 'Output', justify = 'left')
        self.DisLabel.grid(row = 0, column = 1, sticky=W)
        #初始化显示区输入框的Text
        self.DisText = Text(self,width=50, height = 16)
        self.DisText.grid(row = 1, column = 2, columnspan = 50, rowspan=16, sticky=NW)

        
        ############################初始化按钮##########################
        self.GetDbsButton = Button(self, text = "登录", command = self.Login)
        self.GetDbsButton.grid(row = 1, column =1, sticky=W) 
        
        self.GetDbsButton = Button(self, text = "GetDataBases", command = self.DisDataBases)
        self.GetDbsButton.grid(row = 16, column = 0, sticky=W)  
        
        self.GetDbsButton = Button(self, text = "SetDataBases", command = self.setDataBases)
        self.GetDbsButton.grid(row = 16, column = 1, sticky=W)         

        self.GetTblButton = Button(self, text = "GetTables", command = self.DisTables)
        self.GetTblButton.grid(row = 17, column = 0, sticky=W)  
                      
        self.GetDbsButton = Button(self, text = "SetTable", command = self.setTable)
        self.GetDbsButton.grid(row = 17, column = 1, sticky=W) 
        
        self.GetItemButton = Button(self, text = "GetItems", command = self.DisTableDesc)
        self.GetItemButton.grid(row = 18, column = 0, sticky=W) 
        
        self.GetDbsButton = Button(self, text = "SetItem", command = self.setItem)
        self.GetDbsButton.grid(row = 18, column = 1, sticky=W)
        
        self.GetItemButton = Button(self, text = "Start", command = self.DisItems)
        self.GetItemButton.grid(row = 19, column = 0, sticky=W) 
        #############################初始化下拉框##########################
        self.cmbEditComboList = ['1：和','2：乘积']
        self.cmbEditCombo = Combobox(values=self.cmbEditComboList)
        self.cmbEditCombo.set('请选择转换类型')
        self.cmbEditCombo['state'] = 'readonly'
        self.cmbEditCombo.grid(row=1, column=0, sticky=W)
        
        self.grid()
    def Login(self):
        ip = self.IpText.get(0.0, END).replace('\r', '').replace('\n', '')
        inUser = self.UserText.get(0.0, END).replace('\r', '').replace('\n', '')
        inPasswd = self.PasswdText.get(0.0, END).replace('\r', '').replace('\n', '')
        self.DisText.insert(INSERT, 'IP:' + ip)
        self.DisText.insert(INSERT, '用户名:' + inUser)
        self.DisText.insert(INSERT, '密码:' + inPasswd)
        try:
            sqlBase = OperMysql(host = ip, user = inUser, passwd = inPasswd)
            sqlBase.connectHost()
        except:
            messagebox.showinfo('Error', 'IP,用户名或密码错误')
            return
        self.sqlBase = sqlBase
        
    def EnsureLogin(self):
        if None == self.sqlBase:
            messagebox.showinfo('Error', 'please login first')
            
    def setDataBases(self):
        self.EnsureLogin()
        dataBase = self.DbText.get(0.0, END).replace('\r', '').replace('\n', '')
        sqlBase = self.sqlBase
        sqlBase.useDataBases(sqlBase.cursor, dataBase)
        
    def DisDataBases(self):
        self.EnsureLogin()
        sqlBase = self.sqlBase
        dataBase = sqlBase.getDataBases(sqlBase.cursor)
        for strBase in dataBase:
            self.DisText.insert(INSERT, '\n' + 'dataBase:' + strBase)
            
    def setTable(self):
        self.EnsureLogin()
        table = self.TbText.get(0.0, END).replace('\r', '').replace('\n', '')
        sqlBase = self.sqlBase
        sqlBase.useTable(table)
        
    def DisTables(self):
        self.EnsureLogin()
        sqlBase = self.sqlBase
        
        dataTables = sqlBase.getDataTables(sqlBase.cursor, sqlBase.database)
        for strTable in dataTables:
             self.DisText.insert(INSERT, '\n' + 'Table:' + strTable)
             
    def DisTableDesc(self):
        self.EnsureLogin()
        sqlBase = self.sqlBase       
        tableDescs = sqlBase.getTableDescription(sqlBase.cursor, sqlBase.table)
        for strDesc in tableDescs:
             self.DisText.insert(INSERT, '\n' + 'strDesc:' + strDesc)
    
    def setItem(self):
        self.EnsureLogin()
        item = self.ColText.get(0.0, END).replace('\r', '').replace('\n', '')
        sqlBase = self.sqlBase
        sqlBase.useItem(item)
            
    def DisItems(self):
        self.EnsureLogin()
        sqlBase = self.sqlBase       
        datas = sqlBase.getDataFiled(sqlBase.cursor, sqlBase.item, sqlBase.table)
        for strData in datas:
            self.DisText.insert(INSERT, '\n' + 'data:' + strData)
            
    def GetDbs(self):
        print(self.IpText.get(0.0, END))
     
        
def main():
    root = Tk()
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.geometry('640x400')#设置主窗口的大小为640*360
    
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
    
    
    
    
    
    
    
    
    
        
    
       
        
