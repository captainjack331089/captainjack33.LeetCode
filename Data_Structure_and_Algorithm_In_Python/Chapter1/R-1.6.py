"""
编写一个Python函数，用来接收正整数n，并返回 1 ~ n 中所有的奇数的平方和。
"""
def sumOfOddSquare(n):
    result = 0
    for i in range(n+1):
        if i%2 == 1:
            result += i ** 2
    return result

print(sumOfOddSquare(4))