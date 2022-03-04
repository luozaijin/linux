# 函数循环  函数递归
# 需要有两个条件: 1. 终止判断, 2. 递归步骤

def function1(n):
    if n == 1: return 1  # 需要将判断条件作为函数的前提
    print(n,  end=" ") # 输出 不换行
    return n * function1(n - 1)  # 用函数的返回值作为函数的参数.


print(function1(5))  # 输出函数
