# Leetcode 25 - Reverse Nodes K Group
# Level: HARD
# O(N) time, O(1) space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to reverse K group of nodes
class Solution:
    # Function to insert a node to the head of linked list
    def push(self, head_ref, new_data):
        new_node = self.ListNode(new_data)
        new_node.val = new_data
        new_node.next = head_ref
        head_ref = new_node
        return head_ref

    # Function to print the linked list
    def printLL(self, node):
        while(node != None):
           print(node.val, end = "")
           node = node.next
           
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
           return head
    
        node = head
        for _ in range(k):
           if not node:
              return head
           node = node.next
    
        prev = self.reverseKGroup(node, k)

        for _ in range(k):
           temp = head.next
           head.next = prev
           prev = head
           head = temp
    
        return prev

# Driver code
if __name__ == '__main__':
    head  = None

    head = push(head, 9) 
    head = push(head, 8) 
    head = push(head, 7) 
    head = push(head, 6) 
    head = push(head, 5) 
    head = push(head, 4) 
    head = push(head, 3) 
    head = push(head, 2) 
    head = push(head, 1)  
  
    k = 3
  
    print("Given linked list ")  
    printLL(head)  
    head = reverseKGroup(head, k)  
  
    print("\nReversed Linked list ")  
    printLL(head)  
