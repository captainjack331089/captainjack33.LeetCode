"""
204. Count Primes
Category: Hash Table
Difficulty: Easy
"""
"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution(object):
    def countPrimes(self,n):

        if n <= 1:
            return 0

        primes = [None]*n
        primes[0] = primes[1] = False

        for i in range(n):
            if primes[i] == None:
                primes[i] = True

                for j in range(i+i, n, i):
                    primes[j] = False
        print(primes)
        return sum(primes)

if __name__ == "__main__":
    print(Solution().countPrimes(10))