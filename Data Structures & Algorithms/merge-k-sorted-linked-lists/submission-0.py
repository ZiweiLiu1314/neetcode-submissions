# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force: scan the head of all lists each time we proceed 
        # and append the smallest one, O(n * k) time, O(1) space 
        # find smallest head 
        res = ListNode(None)
        cur = res 
        
        while True:
            minNode = -1
            for i in range(len(lists)): 
                if not lists[i]:
                    continue 
                    idx = i 
                if minNode == -1 or lists[i].val < lists[minNode].val: 
                    minNode = i 
                
            if minNode == -1:
                break 
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next 
            cur = cur.next 
        return res.next 



