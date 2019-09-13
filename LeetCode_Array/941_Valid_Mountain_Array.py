"""
941. Valid Mountain Array
Category: Array
Difficulty: Easy
"""
"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000 

"""

class Solution(object):
    def validMountainArray(self,A):
        start = 0
        #walk up
        while start+1 < len(A) and A[start] < A[start+1]:
            start += 1
        #check the increasing point should not be the first and the last
        if start == 0 and start == len(A)-1:
            return False
        #walk down
        while start+1 < len(A) and A[start] > A[start+1]:
            start += 1
        #check the last decreasing point is the last index
        return (start == len(A)-1)

if __name__ == "__main__":
    print(Solution().validMountainArray([3,5,4]))
    print(Solution().validMountainArray([3, 5, 5]))