"""
605. Can Place Flowers
Category: Array
Difficulty: Easy
"""
"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

"""

class Solution(object):
    def flowerbed(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        count = 0

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1

        if count >= n:
            return True
        return False

if __name__ == "__main__":
    print (Solution().flowerbed([1,0,0,0,1], 2))

