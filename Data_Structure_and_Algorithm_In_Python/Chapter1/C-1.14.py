"""
编写一个 Python 函数，用来接收一个整数序列，并判断该序列中是否存在一对乘积是奇数的互不相同的数
"""
def isOddsum(nums):
    pair = []
    for i in nums:
        if i not in pair and i % 2 == 1:
            pair.append(i)

    if len(pair) >= 2:
            return True
    return False

nums = [1,2,4,6,8,3]
print(isOddsum(nums))