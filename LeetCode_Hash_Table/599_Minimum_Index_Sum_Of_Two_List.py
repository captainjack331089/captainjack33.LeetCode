"""
599. Minimum index sum of tow list
Category: Hash Table
Difficulty: Easy
"""
"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        lookup = {}
        result = []
        min_range = float('inf')
        for index1,res1 in enumerate(list1):
            lookup[res1] = index1
        for index2,res2 in enumerate(list2):
            if res2 in lookup:
                if lookup[res2] + index2 < min_range:
                    min_range = index2 + lookup[res2]
                    result = [res2]
                elif lookup[res2] + index2 == min_range:
                    result.append(res2)
        return result



list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]

if __name__ == "__main__":
    print(Solution().findRestaurant(list1,list2))