#!/usr/bin/python
#-*- coding:utf-8 -*-

##################slice切片#######################################
#列表和元组可用切片方式
l = [1, 2, 3, 4, 5, 6]

a = l[:3]
print(a)
a = l[-3:-1]
print(a)
a = l[-1:1]#切片可以全正或全负，不能不半一半
print(a)

#间隔取值
a = l[0:4:2]#在0-4范围内间隔2取值
print(a)

#复制
a = l[:]
print(a)

#tuple其实也是一种list，因此也可以切片，操作方式和list一致
#字符串也可以看成是list，操作与list类似
Str = 'abcdefg'
a = Str[2:4]
print(a)

##################迭代#######################################
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#dict迭代
def itre_example_dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    for i in d.items(): #迭代key用d,迭代values用d.values(),迭代key和value则用d.items()
        print(i)

itre_example_dict()

#如何判断对象是否是可以迭代对象，可通过collections的Iterable来判断
from collections import Iterable
print(isinstance('abc', Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, values in enumerate({1:1, 2:2, 3:3}.items()):
    print(i, values)
    
    
###########################列表生成器#######################################
def GenerateList():
    #第一种
    l = list(range(1, 11))
    print(l)
    #第二种
    l = []
    for x in range(1, 11):
        l.append(x * x)
    print(l) 
    #第三种
    l = [x * x for x in range(1, 11) if x % 2 == 0] #可使用两层for
    print(l) 
GenerateList()    

import os
def List_CurDir():
    szDirs = [d for d in os.listdir('.')]
    print(szDirs)

List_CurDir()
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

###########################生成器#######################################
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的,由于内存空间有限
#生成器Generator是将列表元素按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢

#创建一个generator方法有多种
#方法1, 用for迭代
l= (x * x for x in range(10))
for a, n in enumerate(l):
    print(a, n)

#使用yield来生成generator函数
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
o = odd()#此时返回一个generator变量赋值给o
print(next(o))

#尝试编写杨辉三角输出
def triangles():
    out = [1]
    while True:
        yield out
        out.append(0)
        out = [out[x-1] + out[x] for x in range(len(out))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
input("please input any key to ending")

######################迭代器######################################
#可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable





























































