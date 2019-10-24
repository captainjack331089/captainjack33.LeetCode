"""
141. Linked List Cycle
Category: Linked List
Difficulty: Easy
"""
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(1)


head2 = ListNode(1)
head2.next = ListNode(2)

class Solution():
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    print(Solution().hasCycle(head1))
    print(Solution().hasCycle(head2))