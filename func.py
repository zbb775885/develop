#!/usr/bin/python
#-*- coding:utf-8 -*-

import math#math 这个包可以让我们使用其中的数学函数

###################函数定义#######################

#pass可以用来作为占位，打桩作用
def nop():
    pass
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad opened type')#出错后会打印这句话
    if x > 0:
        return x
    else:
        return -x
    
print(my_abs(-23))
#print(my_abs('''fsfds'''))

#返回多个值

def move(x, y , step, angle= 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 20, 60, math.pi / 6)#多值返回其实返回的是一个tuple，多变量接受时按顺序接受，如果写一个值则返回一个元组值    
print(x, y)

var = input("please input any key to ending")

#定义函数时，需要确定函数名和参数个数；

#如果有必要，可以先对参数的数据类型做检查；

#函数体内部可以用return随时返回函数结果；

#函数执行完毕也没有return语句时，自动return None。

#函数可以同时返回多个值，但其实就是一个tuple。


##########################################################################


#########################函数参数#################################################




































































