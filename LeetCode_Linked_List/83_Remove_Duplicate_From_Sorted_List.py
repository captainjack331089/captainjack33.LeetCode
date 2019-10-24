
"""
83. Remove Duplicate from sorted list
Category: Linked list
Difficulty: Easy
"""
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

class Solution(object):
    def deleteDuplicates(self,head):
        result = []
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        while head:
            #print(head.val)
            result.append(head.val)
            head = head.next
        return result

if __name__ == "__main__":
    print(Solution().deleteDuplicates(head))
