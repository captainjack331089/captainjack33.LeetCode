"""
500. Keyboard Row
Category: Hash Table
Difficulty: Easy
"""
"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

import time

class Solution(object):
    def findWords1(self,words):
        lookup = {}

        for i in "qwertyuiop":
            lookup[i] = 1
        for i in "asdfghjkl":
            lookup[i] = 2
        for i in "zxcvbnm":
            lookup[i] = 3
        result = []
        for word in words:
            l_word = word.lower()
            if len(set(lookup[i] for i in l_word)) == 1:
                result.append(word)
        return result

    def findWords2(self,words):

        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            for key in keyboard:
                l_word = word.lower()
                if set(l_word).issubset(set(key)):
                    result.append(word)
        return result


words = ["Hello", "Alaska", "Dad", "Peace"]
if __name__ == "__main__":
    start0 = time.time()
    print(Solution().findWords1(words))
    end0 = time.time()
    print('code1 time cost',end0-start0,'s')

    start1 = time.time()
    print(Solution().findWords2(words))
    end1 = time.time()
    print('code2 time cost', end1 - start1, 's')