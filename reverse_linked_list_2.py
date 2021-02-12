# Leetcode 92 - Reverse Linked List II
# Level: Medium
# O(N) time, O(1) space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        before, p1, p2 = ListNode(None), head, head
        
        for i in range(1, n+1, 1):
            if i < m:
                before.next = p1
                p1 = p1.next
                before = before.next
            p2 = p2.next
        
        diff = n - m
        while diff >= 0:
            p3 = p1.next
            p1.next = p2
            p2 = p1
            p1 = p3
            diff -= 1
            
        before.next = p2
        before = head
        if m == 1:
            return p2
        return before
        