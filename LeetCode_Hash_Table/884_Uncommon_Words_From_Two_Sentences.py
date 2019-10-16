"""
884. Uncommon words from two sentences
Category: Hash table
Difficulty: Easy
"""
"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""
import collections
class Solution():
    def uncommonFromSentences(self,A,B):
        result = []
        countA = collections.Counter(A.split(" "))
        countB = collections.Counter(B.split(" "))
        words = list((countA.keys() | countB.keys()) - (countA.keys() & countB.keys()))
        for word in words:
            if countA[word] == 1 or countB[word] == 1:
                result.append(word)

        return result

A = "apple apple"
B = "this apple is sour"

if __name__ == "__main__":
    print(Solution().uncommonFromSentences(A,B))