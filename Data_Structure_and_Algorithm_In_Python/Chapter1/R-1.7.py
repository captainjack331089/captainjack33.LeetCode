"""
基于Python的解析语法和内置函数 sum，写一个单独的命令来计算练习R-1.6中的和。
"""
def sumOfOddSquare(n):
    return (sum(i ** 2 for i in range(n+1) if i % 2 == 1))

print(sumOfOddSquare(4))