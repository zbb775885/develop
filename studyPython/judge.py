#!/usr/bin/python
#-*- coding:utf-8 -*-


###################条件判断语句if#######################
age = 20
if age > 10:
	print('your age is %d' %age)
elif age > 5:
    print("age is between 5-10")
else:
    print("age is too small")

##########################################

###################input介绍#######################
#input返回的数据时str类型，不能用于与整数比较大小等操作，但是可以用int来转换
tmp = input("please input num:")
tmp = int(tmp)

print("val:%d" %tmp)

##########################################

var = input("please input any key to ending")





