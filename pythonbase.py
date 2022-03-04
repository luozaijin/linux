#!/bin/python3
# -*- coding: UTF-8 -*-
# 以上在Linux系统需要输入

#  第一天学习内容


# 单行注释可以使用井号 ########
'''
多行
注释
上下
使用
三个
单引号
'''

# [ 重定向 ] ########
# 程序 < 输入文件
# 程序 > 保存文件
# 程序 | 程序  (管道)

# 输出与输入  ########
import sys, os
print("你好, Python") # 常规输出
a,b,c = 1,2,3 # 设置多个变量
sys.stdout.write("利用系统API来输出") # 利用系统API来输出字符 和print类似 
# value=sys.stdin 读入标准输入赋值给变量
# value=sys.stderr 读取标准错误赋值给变量

print("a,b,c" ,  sep="#"  ,  end=" Bye \n" , file=sys.stdout , flush=False )
'''
 abc 变量需要逗号分割, sep 表示变量分割的符号, 默认是空格.
 end 表示字符串结束后输出什么, \n 表示换行
 file=sys.stdout 表示输出只屏幕 也称为标准输出, 需要导入sys模块
 flush=False 表示是否输出到流
'''

# 多行输出  ########
duohang='''
1
2
3
4
支持格式化字符\nend
'''
print(duohang)


# 简单数值计算  ########
print("Hello,Python", 9 / 3 , 2 < 1) #  字符输出, 简单算数输出, 对比输出
print("最后的" + str(9*9) + "电影") # 使用str计算括号内数值,也可以填入字符, 如果使用+号这是把字符连接在一起, 没有空格
print("尼伯龙根的", repr(81/9) ,"指环") # 使用repr和str一样的效果, 使用逗号会有格


# 输出格式化  ########
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world")) # 设置指定位置
print("{1} {0} {1}".format("hello", "world")) # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print("%s"%("hello")) #  格式化输出字符, 由于信息较多,了解更多请查看 https://www.runoob.com/python3/python3-string.html 


# 字典迭代  ########
# f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
# f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678} # 建立字典
for name, phone in table.items(): # 遍历字典, items() 是对象的迭代的方法
    print(f'{name:10} ==> {phone:-10}') # 格式化输出. :10 是向后添加10个占位符包括当前字符, :-10 或者:10d 向前添加10个占位符 包括当前字符  


# 格式化遍历 1 
for y in range(1,11): # 设置遍历关键字range
    print("%d %d %d" %(y , y*y, y*y*y) )
# 格式化字典遍历 2 
for x in range(1, 11): # 设置遍历关键字range
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))  # 使用字典来排版输出列表, :2d 可以看做 :-2 就是占用2占位符.



# 通过字典设置输出数 ########
site = {"name": "菜鸟教程", "url": "www.runoob.com"} # 设定字典变量
print("网站名：{name}, 地址 {url}".format(**site)) # 双星号表示加载字典变量
 

# 通过列表索引设置输出 ########
my_list = ['菜鸟教程', 'www.runoob.com'] # 设定列表变量
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的



# 输入字符 ########
import getpass # 密码模块 
a=input("请输入: ")  # 输入字符保存到变量
print(a,"默认为str类型") # 输出变量
b=int(input("请输入数值:" )) # 输入字符转换为int再保存到变量
print(b) # 输出变量
passwd=getpass.getpass("请输出密码:")  # 不显示字符输入, 需要导入getpass 模块
print("你输入的密码是: ",passwd)
