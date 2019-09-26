"""
基于Python的解析语法和内置函数 sum，写一个单独的命令来计算练习R-1.4:
编写一个Python函数，用来接收正整数 n，返回 1 ~ n 的平方和。中的和。
"""
def posn(n):

    return (sum(i**2 for i in range(n+1) if i > 0))

print(posn(4))