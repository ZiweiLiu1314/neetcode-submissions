# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove the n-th node, counting from the end of the linked list 
        # return head 
        # how do we find a node counting from the end? 
        # two pointers would come in handy 
        # slow pointer would increment from the start of the linked list, 
        # fast pointer would be n steps ahead of the slow 
        # so that when fast reaches the end, slow is at the n-th nodee from the end 
        # we can use the "dummy" node as the sudo head, to cover the case where the node 
        # to remove is the original head 
        dummy = ListNode(0)
        dummy.next = head 
        slow, fast = dummy, dummy 
        for i in range(n): 
            fast = fast.next 
        while fast.next: 
            slow = slow.next 
            fast = fast.next 
        # removal step 
        slow.next = slow.next.next 
        return dummy.next 
