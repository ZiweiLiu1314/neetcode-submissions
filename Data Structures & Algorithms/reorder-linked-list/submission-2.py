# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the nodes in a singly linked list, to [0, n-1, 1, n-2, 2, n-3, ...]
        # brute force: traverse through the list to find out the length n 
        # travers through the linked list to find each value and put them in the right place, starting from the node 0 
        # O(n^2) time 
        # optimized: do one go and insert the nodes at the right places 
        # determine the length of the list in one go, and as we do so we build a hash map val2node O(n)
        # construct the new linked list using the hash map, O(n)
        # O(n) time 
        n = 0 
        idx2node = defaultdict(ListNode)
        node = head
        while node:
            idx2node[n] = node 
            n = n + 1 
            node = node.next 
        node = head
        for i in range(1, n):
            if i % 2 == 0: # even idx 
                node.next = idx2node[i//2]
            else: 
                node.next = idx2node[n - (i // 2) - 1] 
            node = node.next 
        node.next = None 