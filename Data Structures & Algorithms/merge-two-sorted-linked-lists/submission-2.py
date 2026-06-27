# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two ptr, one in list1 and one in list2, and increment the smaller one 
        node1 = list1
        node2 = list2
        i = 0
        head = ListNode()
        node = head
        while node1 or node2: 
            if (node1 and node2 and node1.val > node2.val) or (not node1 and node2): 
                node.next = node2 
                node2 = node2.next 
            else: 
                node.next = node1 
                node1 = node1.next 
            node = node.next

        return head.next 