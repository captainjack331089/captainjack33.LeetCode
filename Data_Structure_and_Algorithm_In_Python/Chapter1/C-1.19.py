"""
C-1.19 演示如何使用 Python 列表解析语法在不输入所有 26 个英文字母的情况下产生列表 [‘a’, ‘b’, ‘c’,…, ‘z’]。

"""

print([chr(ord('a')+x) for x in range(26)])