# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None 
        nxt = None 
        node = head 
        while node: 
            """
            if not prv: 
                prv = node 
                node = node.next 
                continue 
            """
            nxt = node.next
            node.next = prv
            prv = node 
            node = nxt 
        return prv 
        
            