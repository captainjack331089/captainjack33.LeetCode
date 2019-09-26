"""
Python 允许负整数作为序列的索引值，如一个长度为 n 的字符串 s，
当索引值 -n ≤ k < 0 时，所指的元素为 s[k]，
那么求一个正整数索引值 j ⩾ 0，使得 s[j] 指向的也是相同的元素

"""

#nums = [1,2,3,4,5], nums[-1] = nums[4], nums[-2]=nums[3]

def index(nums,k):
    N = len(nums)
    return N - (-(k))

nums = [1,2,3,4,5,6,7,8,9,10]
k = -4

print(index(nums,k))