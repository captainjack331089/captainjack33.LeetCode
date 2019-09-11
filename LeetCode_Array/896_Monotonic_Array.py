"""
896. Monotonic Array
Category: Array
Difficulty: Easy
"""
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

"""
class Solution(object):
    #Method 1: One Pass
    def isMonotonic(self,A):

        isIncreasing = True
        isDecreasing = False

        for i in range(1,len(A)-1):
            if A[i-1] > A[i]:
                isIncreasing = False
            if A[i-1] < A[i]:
                isDecreasing = False
        return (isIncreasing or isDecreasing)
    #Method 2: brutual
    def isMonotonic2(self,A):
        index1 = 0
        index2 = 0
        for i in range(1,len(A)-1):
            if A[i-1] <= A[i]:
                index1 += 1
            if A[i-1] >= A[i]:
                index2 += 1
        if index1 == len(A)-1 or index2 == len(A)-1:
            return True
        return False

if __name__ == "__main__":
    print(Solution().isMonotonic([6,5,4,4]))
    print(Solution().isMonotonic2([6, 5, 4, 4]))