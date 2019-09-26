"""
Python 的 random 模块包括一个函数 choice(data)，
可以从一个非空序列返回一个随机元素。
Random模块还包含一个更基本的 randrange 函数，
参数化类似于内置的 range 函数，
可以在给定范围内返回一个随机数。
只使用 randrange 函数，实现自己的 choice 函数

"""

def myChoice(data):
    import random
    radiant = random.randrange(len(data))
    return data[radiant]

data = [1,2,3,4,5]

print(myChoice(data))