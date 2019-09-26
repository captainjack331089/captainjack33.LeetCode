"""
编写一个 Python 函数，用来接收一个数字序列，并判断是否所有数字都互不相同。
"""

def isDifferent(nums):
    return len(nums) == len(set(nums))

nums = [1,2,3,4,5,5]

print(isDifferent(nums))