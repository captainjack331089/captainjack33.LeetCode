"""
234. Palindrome Linked list
Category: Linked List
Difficulty: Easy
"""
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

class ListNode:
    def __init__(self,x):
        self.val  = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next= ListNode(1)

class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next
        if fast:
            slow = slow.next
        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome(head))