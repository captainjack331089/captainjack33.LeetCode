"""
989. Add to Array-Form of Integer
Category: Array
Difficulty: Easy
"""
"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
 

Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0
思路1： 把数组转化成数字，加上数字，再把数字转化成数组
思路2： 直接把数字加上数组最后一个数字，往前递归。
"""
class Solution(object):
    def addToArrayForm1(self,A,K):
        a = 0
        result = []
        for i in A:
            a = a*10 + i
        temp = a + K
        if temp == 0:
            return [0]
        while temp:
            result.insert(0,temp%10)
            temp //= 10
        return result

    def addToArrayForm2(self,A,K):
        for i in range(len(A))[::-1]:
            A[i],K = (A[i]+K)%10, (A[i]+K)//10
        return ([int(i) for i in str(K)] + A if K else A)
if __name__ == "__main__":
    print(Solution().addToArrayForm1([1,2,0,0],34))
    print(Solution().addToArrayForm1([9,9,9,9], 1))

    print(Solution().addToArrayForm2([1, 2, 0, 0], 34))
    print(Solution().addToArrayForm2([9, 9, 9, 9], 1))