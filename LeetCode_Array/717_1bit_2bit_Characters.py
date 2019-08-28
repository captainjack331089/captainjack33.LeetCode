"""
717. 1 Bit and 2 Bit Characters
Category: Array
Difficulty: Easy

"""
"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        i,j = 0, len(bits)-1
        while i < j:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        if i == j:
            return True
        return False

if __name__ == "__main__":
    print(Solution().isOneBitCharacter([1,0,0]))
    print(Solution().isOneBitCharacter([1, 0, 1,0]))