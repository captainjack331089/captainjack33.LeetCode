"""
编写一个Python函数 minmax(data)，
用来在数的序列中找出最小数和最大数，
并以一个长度为 2 的元组的形式返回。
注意：不能通过内置函数 min 和 max 来实现。
"""

def minmax(data):

    tempmin = data[0]
    tempmax = data[0]

    for i in data:
        if tempmin > i:
            tempmin = i
        if tempmax < i:
            tempmax = i
    return tempmin,tempmax

data = [1,2,3,4,5,6]
print(minmax(data))