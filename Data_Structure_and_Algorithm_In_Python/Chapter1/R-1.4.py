"""
R-1.4 编写一个Python函数，用来接收正整数 n，返回 1 ~ n 的平方和。
"""

def sumOfSquare(n):
    result = 0
    for i in range(n+1):
        result += i**2
    return result

print(sumOfSquare(4))