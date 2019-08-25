"""
624. Maximum Distance In Arrays
Category: Array(lock)
Difficulty: Easy

"""
"""
Given m arrays, and each array is sorted in ascending order. 
Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. 
We define the distance between two integers a and b to be their absolute difference |a-b|. 
Your task is to find the maximum distance.

Example 1:

Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
 

Note:

Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""
class Solution(object):
    def maxDistance(self,arrays):
        length = len(arrays)
        min_arrays = arrays[0][0]
        max_arrays = arrays[0][len(arrays[0])-1]
        result = 0
        for i in range(1,length):
            new_array = arrays[i]
            result = max(abs(new_array[len(new_array)-1] - min_arrays), abs(max_arrays - new_array[0]), result)
            max_arrays = max(new_array[len(new_array)-1], max_arrays)
            min_arrays = min(new_array[0], min_arrays)

        return result



print(Solution().maxDistance([[1,2,3],[4,5],[1,2,3]]))
