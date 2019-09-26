"""
编写一个Python函数 is_even(k)，
用来接收一个整数 k,
如果 k 是偶数返回 True，
否则返回 False。
但是，函数中不能使用乘法、除法或取余操作.

"""

def is_even(k):
    while k > 0:
        k = k - 2
    return (k == 0)

print(is_even(5))