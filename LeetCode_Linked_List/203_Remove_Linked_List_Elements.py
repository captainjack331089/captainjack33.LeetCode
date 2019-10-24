"""
203. Remove Linked Elements
Category: Linked List
Difficulty: Easy
"""
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next= ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
val = 6

class Solution(object):
    def removeElements(self, head, val):

        result = []

        dummy = ListNode(float('-inf'))
        dummy.next = head

        previous, current = dummy, dummy.next

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        while dummy.next:
            result.append(dummy.next.val)
            dummy.next = dummy.next.next
        return result

if __name__ == "__main__":
    print(Solution().removeElements(head,val))