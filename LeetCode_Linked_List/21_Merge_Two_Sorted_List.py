"""
21. Merge two Sorted List
Category: Linked List
Difficulty: easy
"""
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        l = []
        curr = result = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        while result.next:
            l.append(result.next.val)
            result = result.next
        return l

if __name__ == "__main__":
    print(Solution().mergeTwoLists(l1,l2))