"""
1010.Partition Array into Three Parts with Equal Sum
Category: Array
Difficulty: Easy
"""''
"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""

class Solution(object):
    def canThreePartsEqualSum(self, A):
        sumA = sum(A)
        if sumA % 3 != 0:
            return False
        onePart = int(sumA / 3)

        index  = 0
        temp  = 0
        for i in range(len(A)):
            temp += A[i]
            if temp == onePart:
                index += 1
                temp = 0
        if index == 3 and temp == 0:
            return True
        return False

if __name__ == "__main__":
    print(Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
    print(Solution().canThreePartsEqualSum([3,3,6,6,0,1]))