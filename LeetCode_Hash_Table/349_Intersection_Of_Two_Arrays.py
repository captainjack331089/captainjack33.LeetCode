"""
349. Intersection of two arrays
Category: Hash-table
Difficulty: Easy
"""
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
class Solution(object):
    def intersection(self,nums1,nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        return (list(nums1&nums2))

if __name__ == "__main__":
    print(Solution().intersection([1,2,2,1],[2,2]))