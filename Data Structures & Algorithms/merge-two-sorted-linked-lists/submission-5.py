# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterative with two ptr, one in list1 and one in list2, and increment the smaller one 
        """
        head = ListNode()
        node = head
        while list1 or list2: 
            if (list1 and list2 and list1.val > list2.val) or (not list1 and list2): 
                node.next = list2 
                list2 = list2.next 
            else: 
                node.next = list1 
                list1 = list1.next 
            node = node.next

        return head.next 
        """
        # recursive 
        if not list1:
            return list2
        if not list2:
            return list1 
        if list1.val < list2.val: # append to next smaller number 
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 
        else: 
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2





