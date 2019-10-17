"""
1078. Occurrences after Bigram
Directory: Hash Table
Difficulty: Easy
"""
"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
 

Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""

class Solution():
    def findOccurences(self,text,first,second):
        result = []
        text = text.split(" ")
        L = len(text)
        for i in range(L-2):
            if text[i] == first and text[i+1] == second and text[i+2]:
                result.append(text[i+2])
        return result

text = "we will we will rock you"
first = "we"
second = "will"

if __name__ == "__main__":
    print(Solution().findOccurences(text,first,second))