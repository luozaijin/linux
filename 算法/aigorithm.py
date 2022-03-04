# win11
# utf-8
# 22-1-30

''' 算法的核心
1. 逻辑性: 内容复杂而又清晰
2. 针对关键问题的处理
3. 运行开销(速度), 内存占用量(消耗)和CPU占用量
4. 网上学习更多
'''

''' 编程的目的?
编程最终是模拟并解决问题.
1. 编程语言只是一种工具, 使用工具有使用说明和使用步骤, 所以对于使用说明这一块只需要工具的作用即可,使用的方式如何就行. 不必要自己重新再制造一个工具.
2. 数据类型则是计算机系统管理系统数据的一种分类, 使用编程语言来设计管理电脑数据可得到你要的结果.
3. 算法 是在编程语言的框架下, 来设计软件功能, 一般算法都是对问题进行针对性的处理, 因为算法是通过编程语言来操作系统的数据类型来设计实现的.
'''


# 查找算法
# 顺序查找
# def search(list, item):
#     pos = 0
#     found = False
#     while pos < len(list) and not found:
#         if list[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# def main():
#     test1 = [1, 2, 4, 59, 5, 6, 12, 16, 33]
#     print(search(test1, 3))
#     print(search(test1, 12))
#     print()
#
#
# if __name__=='__main__':
#     main()


# 顺序寻找最大值和最小值
# def max(list):
#     pos = 0
#     max1 = list[0]
#     while pos < len(list):
#         if list[pos] > max1:
#             max1 = list[pos]
#         pos += 1
#     return max1
#
#
# def mini(list):
#     mini1 = list[0]
#     for item in list:
#         if item < mini1:
#             mini1 = item
#     return mini1
#
#
# def main():
#     print("mini: ", mini(show))
#     show = [1, 2, 4, 59, 5, 6, 12, 16, 33]
#     print("max: ", max(show))
#
#
# if __name__ == '__main__':
#     main()


# 二分找查发
# TODO: 
def _dobelfind(key, a, low, high):
    if high <= low:
        return -1
    mid = (low + high) // 2
    if a[mid] > key:
        return _dobelfind(key, a, low, high)
    elif a[mid] < key:
        return _dobelfind(key, a, mid+1, high)
    else:
        return mid


def dobelfind(key, a):
    return _dobelfind(key, a, 0, len(a))


def main():
    a = [1, 2, 4, 59, 5, 6, 12, 16, 33]
    print("关键字列表: ", dobelfind(33, a))
    print("关键字列表: ", dobelfind(99, a))


if __name__ == '__main__':
    main()
