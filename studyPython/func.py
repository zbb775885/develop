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

#var = input("please input any key to enter function's parameter")
#定义函数时，需要确定函数名和参数个数；

#如果有必要，可以先对参数的数据类型做检查；

#函数体内部可以用return随时返回函数结果；

#函数执行完毕也没有return语句时，自动return None。

#函数可以同时返回多个值，但其实就是一个tuple。


##########################################################################


#########################函数参数#################################################
#位置参数
#添加默认参数，可以不用输入y。且默认参数必须在非默认参数后，或者都没有
def my_pow(x = 3, y = 2): 
    tmp = 1
    while y > 0:
        tmp = tmp * (x)
        y -= 1
    return tmp

print("val:%d" %(my_pow(5,4)))

print("val:%d" %(my_pow()))
#默认参数好的好处就是可以降低函数调用的复杂度。
#一年级小学生注册的函数，需要传入name和gender，但如果要继续传入年龄等会增加复杂度，设置默认参数后可不用传入参数即可解决
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
#如上，如需不按顺序提供默认参数，则需要将默认参数名写上。 
enroll("12", "fds", city='Beijing')
#需要记住默认参数必须指向不变参数，如list参数不建议使用
def add_end(l = []):#l的指针指向[]，如果[]增加了参数则l指向的值会变化
    l.append('end')
    return l
print(add_end())
print(add_end())
print(add_end())
#如要解决该问题可如下修改
def add_end1(l = None):
    if l == None:
        l = []
    l.append('end')
    return l
print(add_end1())
print(add_end1())
print(add_end1())


#############################可变参数##########################################
#可变参数会把传入的参数元组（tuple）化，定义方式为在参数前增加*，如下
def my_sum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum
print("my_sum:%d" %(my_sum(10,12,343)))
#可以把传入的参数可变参数化
data = (10, 12, 343)
print("variable sum:%d" %(my_sum(*data)))

#############################关键字参数##########################################
#关键字参数会把传入的参数字典化dict,定义方式为在参数前增加**,关键字可为0个或任意个
def person(name, age, **kw):
    print('name' , name, 'age', age, 'kw:' , kw)

person('Adam', 45, gender='M', job='Engineer')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Adam', 45, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra


############################命名关键字参数############################################################
#跟字典类似，但是必须有名字，定义方法如下
def func1(a, b , *, test1, test2):
    print(a, b, test1, test2)
func1(1, 2 ,test1 = 3, test2= 4)#调用时必须写上test1=... test2=...

def func2(a, b , *args, test1, test2):#如果定义时有可变参数则命名关键字的*可不需要
    print(a, b, args, test1, test2)
func2(1, 2 ,45, 4543, 453, test1 = 3, test2= 4)#调用时必须写上test1=... test2=...

#############################################参数组合#################################
#python中的参数可以用必选参数，默认参数，可变参数，关键字参数和命名关键字参数
#但是顺序必须是必选参数，默认参数，可变参数，命名关键字参数，关键字参数
def func3(a, b = 2, *args, d, **kw):
    print(a, b, args, d, kw)
    
func3(9, 5, 1, 2, 3, d = 0, e = 'a', f = 'b')
#对于所有的函数都已以func(*args, **kw)来调用

#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

#要注意定义可变参数和关键字参数的语法：

#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

input("please input any key to ending")






























































