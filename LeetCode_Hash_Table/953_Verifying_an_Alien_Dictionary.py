"""
953. Verifying an Alien Dictionary
Category: Hash Table
Difficulty: Easy
"""
"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""

class Solution():
    def isAlienSorted(self, words, order):
        lookup = {}
        for i,c in enumerate(order):
            lookup[c] = i

        result = sorted(words, key=lambda x: [lookup[c] for c in x])
        return result == words

words1 = ["word","world","row"]
order1 = "worldabcefghijkmnpqstuvxyz"

words2 = ["apple", "app"]
order2 = "abcdefghijklmnopqrstuvwxyz"

words3 = ["hello","leetcode"]
order3 = "hlabcdefgijkmnopqrstuvwxyz"

if __name__ == "__main__":
    print(Solution().isAlienSorted(words1,order1))
    print(Solution().isAlienSorted(words2,order2))
    print(Solution().isAlienSorted(words3, order3))
