#!/bin/python3
# UTF-8
# Windwos11

'''
# [ 文件名 参数 ]
import sys, random # 导入模块
n = int(sys.argv[1]) # sys.argv[0]为脚本名,[1], 为第一个参数,..第二个参数.
for i in range(n): # 遍历5次
    print(random.randrange(0,100)) # 0到100的随机数

# 保存该文件, 在cmd 使用python 运行该文件 并在该文件名后面添加参数
'''

# [ 打开文件 ]
import sys # 导入模块
file ='txt.txt' # 文件路径
filename = open(file, 'r' , encoding='utf-8') # 打开文件 w: 表示可写入, r: 表示只读查看, x: 表示可执行文件 创建删除移动重命名之类, encoding 表示打开文件字符格式.
line_no=0 # 设定 行
'''
while True: # 直接循环
    line_no += 1 # 行 加一 
    line = filename.readline() # 读取文件 行
    if line : # 判断 文件行
        print(line_no, ":", line) # 输出字符
    else: # 不存在则退出
        break # 跳出循环
filename.close # 关闭文件
'''

# 使用 with 语句关联上下文, 具体操作请百科
with open(file, 'r' ,encoding='utf-8' ) as file:
    for line in file:
        line_no += 1
        print(line_no, '%', line)
filename.close

