#python3

# list # 学习列表

list=[]  # 新建一个空列表
list.append("ok") # 往后添加一个新元素
 
print(list[:]) # 显示输出


list1=[]
list2=[]
list3=[]
list4=[]
list5=[list1,list2,list3,list4]

x=int(input("输入一个数: "))
s=str(input("字符串列表2变量: "))
c=int(input("列表3数值相加: "))
p=c+c # 语句
o=(3,6)
# 列表的嵌套
for i in range(x) : # 设置 range函数
	list1.append(i) # 嵌套数值遍历
	list2.append(s) # 嵌套字符串
	list3.append(p)	# 嵌套数值相加
	list4.append(o) # 嵌套元组
	print(list5[:]) # 显示输出

