# 二分查找
''' 条件:
    二分查找需要列表从小到大, 从左到右, 无断数.
    步骤:
    1: 有一段顺序列表, 程序会判断列表的 最小数,最大数,和中间数,就是最大和最小的两数之差.
    2: 每一次循环, 都会判断需要猜的数值, 并且根据数值来判断范围, 每次对半除, 而最小数和最大数, 要相应的进位一步
最小值加一 最大值减一, 因为我们都知道, 每次来判断数值范围的时候, 都知道数值的最小值和最大值在这个范围区间来寻找,
所以数值可能等于范围的边际值(范围的最小值和最大值),而不会超过范围的边际值.
也就是1-50,实际要判断的是2和49的值,优先排除边际值,

'''

list = []  # 新建一个列表
for l in range(1, 51):
    list.append(l)
print(list)  # 输出列表


def efcz(list):  # 函数
    low = list[0]  # 列表最小数
    high = list[-1]  # 列表最大数
    mid = (high - low) // 2  # 注意 这是整除,所以商是24
    while True:  # 循环 O(1)
        number = int(input("请输入一个50以内的数: "))  # 提示
        if low == number or mid == number or high == number:  # 如果判断遇到猜中的数则跳出循环
            # 最前的数值和最后的数值, 会直接判定.
            print("Low:", low, "Mid:", mid, "High:", high)
            break
        elif number > high:
            print("你输入大了,请重新输入")
            continue
        else:
            if number < mid:  # 小于
                high = mid  # 重新定位 high
                mid -= (high - low) // 2  # 重新定位 mid
                high -= 1  # 边际值调整
                print("Mid", mid)
            else:  # 否则 则大于
                low = mid  # 重新定位 low
                mid += (high - low) // 2  # 重新定位 mid
                low += 1  # 边际值调整
                print("Mid", mid)

efcz(list)
