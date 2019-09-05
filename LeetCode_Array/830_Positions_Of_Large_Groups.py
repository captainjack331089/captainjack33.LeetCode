"""
830. Positions of Large Groups
Category: Array
Difficulty: Easy
"""
"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

Note:  1 <= S.length <= 1000
"""

class Solution(object):
    def largeGroupPositions(self,S):
        check_index = 0
        result = []
        for i in range(len(S)-1):
            if S[i] != S[i+1]:
                if i - check_index + 1 >= 3:
                    result.append([check_index,i])
                check_index = i+1
        if len(S)-check_index >= 3:
            result.append([check_index, len(S)-1])
        return result

if __name__ == "__main__":
    print(Solution().largeGroupPositions("abbxxxxzzy"))
