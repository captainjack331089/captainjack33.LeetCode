"""
350. Intersection of two arrays II
Category: Hash Table
Difficulty: Easy
"""

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
import collections
class Solution(object):
    def intersectionII(self,nums1,nums2):
        result = []
        lookup1 = collections.Counter(nums1)
        lookup2 = collections.Counter(nums2)
        for num,count in lookup1.items():
            if num in lookup2:
                result += [num]*(min(count,lookup2[num]))
        return result

if __name__ == "__main__":
    print(Solution().intersectionII([1,2,2,1], [2,2]))