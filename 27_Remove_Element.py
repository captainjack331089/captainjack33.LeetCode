
"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""



"""
Here are two ways to solve this solution
"""

nums = [2,2,2,3,4,5,6,2]
val = 2

class Solution(object):
    ##Method 1:
    def removeElement1(self, nums, val):
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return nums,length

    ##Method 2:
    """
    Eg. a = [2,3,3,2] ---> 1. Check if a[0] = val, if true: a[0] = a[3], a[3] = a[0]
                           2. Check if a[0] = val, if true: a[0] = a[2], a[2] = a[0]
                           3. Check a[0] = val, if false: check a[i]
                           4. break when check a[i] is a[n-i]
                           5: return n-i
    """
    def removeElement2(self, nums, val):
        i, length = 0, len(nums)-1
        while i <= length:
            if nums[i] == val:
                nums[i], nums[length] = nums[length], nums[i]
                length -= 1
            else:
                i += 1
        return nums, length +1


if __name__ == "__main__":
    solution = Solution()
    #print(solution.removeElement1(nums, val))
    print(solution.removeElement2(nums, val))