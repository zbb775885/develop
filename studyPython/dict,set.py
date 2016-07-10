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

print(d.get('fds')) #返回none，如果修改为d.get('Thomas', -1)则返回-1

#pop()可以删除dict中的值
d.pop('paul')
print(len(d))
#字典与list比较优缺点
#字典
#耗费内存大，但是查找和插入块，不会随key增加而变慢
#list
#list耗费内存小,但是查找和插入数据会随key增加而变慢

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
#正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象,字符串、整数不可变，list可变因此不能作为key
tmp = 'fdsf'
d[tmp] = 3
print(d)
tmp = 6
d[tmp] = 3
print(d)
tmp = (1,2)
d[tmp] = 3
print(d)
#tmp = [1,2] 出错
#d[tmp] = 3
#print(d)

###################set 无序且无重复元素的集合#######################
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#字典，list，tuple均可作为输入参数，但是其中的元素不能是列表
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 3])
print(s)#该打印结果和上一个一样，因为set没有重复
#add(key)可以用来增加set值
s.add(9)
print(s)
#remove(key)删除元素
s.remove(1)
print(s)
#set可以做交集，并集
s1 = set((1,2,3))
s2 = set((4,2,5))
print(s1 | s2)
print(s1 & s2)
print(s1 == s2)
print(s1 ^ s2)
#print(s1[0] > s2[0]) 集合不支持索引，会出错
var = input("please input any key to ending")












































































