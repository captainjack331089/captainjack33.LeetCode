"""
167. Two Sum II---Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""

class Solution(object):
    def twoSum(self,numbers,target):
        d = {}
        for i,j in enumerate(numbers):
            remain_numbers = target - j
            if remain_numbers not in d:
                d[j] = i
            else:
                return ([d[remain_numbers]+1,i+1])


##Method2:
class Solution2(object):
    def twoSum(self,numbers,target):
        start = 0
        end = len(numbers)-1
        sum = 0
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                return ([start+1,end+1])

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15],9))
    print(Solution2().twoSum([2, 7, 11, 15], 18))