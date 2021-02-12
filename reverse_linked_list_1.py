# Leetcode 206 - Reverse Linked List
# Level: Easy
# O(N) time, O(1) space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1, p2 = None, head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1