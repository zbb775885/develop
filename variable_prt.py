#!/usr/bin/python
#-*- coding: utf-8 -*-


n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
print('s4 = r\'\'\'Hello, \nLisa!\'\'\'')


#字符转数字 ord
print(ord('a'))
#数字转字符 chr
print(chr(67))

###########打印print相关################
#打印变量,%s永远起作用，它会把任何数据类型转换为字符串
print( 'Age: %s. Gender: %s' %(n, True), "test")
#print打印函数要打印参数在""后不能加逗号，加了就是在原先基础上增加空格
print( 'test', "test")
#############################################

##################list列表####################
#定义
classmate = ['Bob', 'helen', 'james', '小王']
print("classmate:%s" %classmate)
#索引参数可以为元素个数(-n)到(n-1)
#list列表是可变的有序表，可追加
classmate.append('tom')
print("classmate:%s" %classmate)
#list列表是可变的有序表，可插入
classmate.insert(1,'jerry')
print("classmate:%s" %classmate)
#list列表是可变的有序表，可删除pop删除末尾元素，pop(i)删除固定位置元素
classmate.pop()
classmate.pop(3)
#list列表是可变的有序表，可直接赋值修改元素
classmate[2] = 'list'
print("classmate:%s" %classmate)
#############################################

##################tuple,元组###########################
#tuple与list类似，但是初始化之后不能修改,比较像C里面的const变量.但是如果tuple的元素是指针，则其指针指向的数据是可变的
classmate = ('bob', 'james', 'tom')
print("classmate:%s %d" %(classmate[0],len(classmate)))#print无法将元组力的所有元素字符串化
#只有1个元素的tuple定义时必须加一个逗号，否则会与(1)产生歧义
tmp = (1)#代表数字1
print("tmp:%s" %(tmp))
tmp = (1,)#代表tuple
print("tmp:%s" %(tmp))

#############################################

var = input("please input")


































