#!/usr/bin/python
#-*- coding:utf-8 -*-


class AnalysisMem():
    def __init__(self, file):
        self.file = open(file, 'r')
        self.totalMallocSize = 0
        self.totalMallocCnt = 0
        self.totalFreeSize = 0
        self.totalFreeCnt = 0
        self.MemInUseSize = 0
        self.list = {}
    
    def getTotalMallocSize(self, size):
        self.totalMallocSize += size
        print("total malloc size:%d" %(self.totalMallocSize))
        
    def readFile (self, lineCnt = 0):
        file = self.file
        lineIdx = 0
        lineData = []
        while (lineIdx < lineCnt) or (lineCnt == 0):
            line = file.realine()
            if (line == ''):
                break;
            print(line.strip())
            lineData.append(line.strip())
            lineIdx += 1
        return lineData
    
    def filterKeyVal(self, *key):
        file = self.file
        file.seek(0, 0)
        for key in keys:
            self.list[key] = {'str':[]}
        while True:
            line = file.readline()
            if (line == ''):
                break;
            for key in keys:
                if key in line:
                    str = line.split(key)[1].replace('\r', '')
                    str = line.split(key)[1].replace('\n', '')
                    str = line.split(key)[1].replace(' ', '')
                    self.list[key]['str'].append(str)
            
            for key in keys:
                print("%s:%s" %(key, self.list[key]['str'][20]))

    def assignKeyVal(self, *keys):
        for key in keys:
            if key in self.list.keys():
                for list in self.list[key]['str']:
                    strList = list.split(',')
                    for listTmp in strList:
                        val = listTmp.split(':')
                        if False == (val[0] in self.list[key].keys()):
                            self.list[key][val[0]] = []
                        self.list[key][val[0]].append(val[1])
                if 'Size' in self.list[key].keys():
                    print("%s" %(self.list[key]['Size'][1]))
            else:
                print("%s is not in dict" %(key))
        
    def analysis(self):
        #for i in self.list['malloc']['Size']:
        #    self.totMallocSize += int(i)
        #    self.totalMallocCnt += 1
        #
        #for i in self.list['free']['Size']:
        #    self.totalFreeSize += int(i)
        #    self.totalFreeCnt += 1
        #    
        #print ("MallocSize:%d Cnt %d FreeSize:%d Cnt:%d" %(self.totMallocSize, self.totalMallocCnt,
        #                                                   self.totalFreeSize, self.totalFreeCnt))  
        index  = 0
        self.lostFree=[]
        for data1 in self.list['malloc']['Addr']:
            addr1 = int(data1, 16)
            Size1 = int(self.list['malloc']['Size'][index])
            realSize1 = int(self.list['malloc']['realSize'][index])
            for data2 in self.list['free']['Addr']:
                addr2 = int(data2, 16)
                Size2 = int(self.list['free']['Size'][index])
                realSize2 = int(self.list['free']['realSize'][index])
                if (addr1 == addr2) and (Size1 == Size2) and (realSize1 == realSize2):
                    self.lostFree.append(index)   
            index += 1
            
        for i in self.lostFree:
            print ("Lost Free:%s" %(self.list['malloc']['str'][i]))
    def close(self):    
        self.file.close()
            
            
if __name__ == '__main__':
    method = AnalysisMem("path")
    method = filterKeyVal('malloc', 'free')
    method = assignKeyVal('malloc', 'free')
    method.analysis()
    method.close()
    input()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        













