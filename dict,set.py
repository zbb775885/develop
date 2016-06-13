#!/usr/bin/python
#-*- coding:utf-8 -*-



###################dict字典，也称为map,key-value存储#######################
d = {'tom':100, 'james':99, 'jerry':95}
print(d['tom'])
#字典的值可以通过key来存入
d['tom'] = 75
#字典的值可以通过新key来增加 
d['paul'] = 98
print(d)
#访问不存在的字典的key，那么就异常。不过可以先通过in来查询一下，或者用get查询一下
if 'mike' in d:
    print('mike is in dict')
else:
    print('mike is not in dict')



var = input("please input any key to ending")


































