"""
509. Fibonacci Number
Category: Array
Difficulty: Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

"""

class Solution(object):
    def fibonacci(self,N):
        if N == 0:
            return 0
        current_value = 1
        previous_value = 0
        for i in range(1, N):
            current_value, previous_value = current_value+previous_value, current_value
        return current_value

if __name__ == "__main__":
    print(Solution().fibonacci(6))