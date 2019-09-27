"""
给出一个 Python 代码片段的例子，编写一个索引可能越界的元素列表。
如果索引越界，
程序应该捕获异常结果并打印以下错误消息：“Don’t try buffer overflow attacks in Python!”

"""

def abnormal(data,i):
    try:
        return data[i]
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
data = [1,2,3]
i = 3
abnormal(data,i)
print(abnormal(data,i))