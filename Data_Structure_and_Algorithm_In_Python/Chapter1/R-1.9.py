"""
要生成一个值为 50， 60， 70， 80 的排列，求 range构造函数的参数.
"""

for x in range(5,9):
    print(x*10,end="")

print(list(range(50,90,10)))
