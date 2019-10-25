"""
206. Reversed Linked List
Category: Linked List
Difficulty: Easy
"""
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self,x):
        self.val  = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next= ListNode(5)

class Solution(object):
    def reverseList(self,head):
        result = []
        current = head
        previous = None
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        while previous:
            result.append(previous.val)
            previous = previous.next
        return result

    def reverseList2(self,head):
        result = []
        dummy = ListNode(float('-inf'))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        while dummy.next:
            result.append(dummy.next.val)
            dummy.next = dummy.next.next
        return result

if __name__ == "__main__":
    print(Solution().reverseList(head))
    print(Solution().reverseList2(head))