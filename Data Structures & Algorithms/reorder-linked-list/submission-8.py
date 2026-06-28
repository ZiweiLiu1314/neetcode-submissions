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
        # O(n) time, O(n) space 
        """
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
        """

        # reverse and merge, O(n) time, O(1) space 
        # 1. find the middle node using slow and fast pointer technique, 
        slow, fast = head, head.next   
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        mid = slow.next 
        slow.next = None 
        prv = None 
        # 2. reverse the latter half, 
        while mid: 
            nxt = mid.next 
            mid.next = prv 
            prv = mid 
            mid = nxt 
        # 3. merge them one by one 
        first, second = head, prv 
        while first and second: 
            tmp1 = first.next 
            tmp2 = second.next
            first.next = second 
            second.next = tmp1 
            first = tmp1 
            second = tmp2 



        # recursive (quite unnatural for this problem) 
        # walking root forward from the head while cur unwinds backward from the tail
        # stimulating two pointers walking toward each other 
        """
        def rec(root: ListNode, cur: ListNode) -> ListNode: 
            if not cur: # have reached the end of the list, 
            # in which case we don't need to change the root 
                return root 
            root = rec(root, cur.next)
            if not root: 
                return None # the "we are done signal"
            tmp = None 
            if root == cur or root.next == cur: 
                # the base case where the two pointers have met in the middle (even-length list)
                cur.next = None 
            else: 
                tmp = root.next 
                root.next = cur 
                cur.next = tmp
            return tmp 
        rec(head, head.next)
        """

            



