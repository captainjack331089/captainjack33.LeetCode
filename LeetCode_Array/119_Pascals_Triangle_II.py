"""
119. Pascals Triangle II
Category: Array
Difficulty: Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

"""
class Solution(object):
    def getRow(self, rowIndex):
        result = [1] + [0]*rowIndex
        #[1,0,0,0]
        for i in range(rowIndex):
            result[0] = 1
            for j in range(i+1, 0, -1):
                result[j] = result[j] + result[j-1]

        return result

if __name__ == "__main__":
    print(Solution().getRow(5))