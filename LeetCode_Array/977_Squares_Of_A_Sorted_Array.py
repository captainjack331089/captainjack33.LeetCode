"""
977. Squares of a sorted Array
Category: Array
Difficulty: Easy
"""
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

"""

class Solution(object):
    def sortedSquares1(self, A):
        #method 1 Nlog(N) 行数短但是复杂度较高。。显然不是最终答案
        result = []
        for i in A:
            result.append(i**2)
        return sorted(result)
    def sortedSquares2(self,A):
        #利用指针指向一个负值，一个正值
        pos = 0
        N = len(A)
        result = []
        while pos < N and A[pos] < 0:
            pos += 1
        neg = pos - 1

        while neg >= 0 and pos < N:
            if A[neg]**2 < A[pos]**2:
                result.append(A[neg]**2)
                neg -= 1
            else:
                result.append(A[pos]**2)
                pos += 1
        while neg >= 0:
            result.append(A[neg]**2)
            neg -= 1
        while pos < N:
            result.append(A[pos]**2)
            pos += 1
        return result


if __name__ == "__main__":
    print(Solution().sortedSquares1([-4,-1,0,3,10]))
    print(Solution().sortedSquares2([-4, -1, 0, 3, 10]))