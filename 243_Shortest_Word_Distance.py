"""
243. Shortest Word Distance
Category: Array
Difficulty: Easy

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

list = ["practice", "makes", "perfect", "coding", "makes"]
a = "coding"
b = "practice"

c = "makes"
d = "coding"


class Solution(object):
    def shortestWordDistance(self,words,word1,word2):
        distance = float("inf")
        i,index1,index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                distance = min(distance, abs(index1-index2))
            i += 1

        return distance

if __name__ == "__main__":
    print(Solution().shortestWordDistance(list,a,b))
    print(Solution().shortestWordDistance(list, c, d))