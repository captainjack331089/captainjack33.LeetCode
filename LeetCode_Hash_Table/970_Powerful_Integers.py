"""
970. Powerful Integers
Category: Hash Table
Difficulty: Easy
"""
"""

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
 
Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
Accepted
14,871
Submissions
37,582
"""
import math
class Solution(object):
    def powerfulIntegers(self,x,y,bound):
        result = set()
        xlog = int(math.log(bound,x)) if x > 1 else 1
        ylog = int(math.log(bound,y)) if y > 1 else 1

        for i in range(xlog+1):
            for j in range(ylog+1):
                temp = x ** i + y ** j
                if temp <= bound:
                    result.add(temp)

        return list(result)



x = 2
y = 3
bound = 10

if __name__ == "__main__":
    print(Solution().powerfulIntegers(x,y,bound))
