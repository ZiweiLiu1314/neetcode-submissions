# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force: store all values in the BST in a array, and the sort, and take 0~k-1, O(n log n) time, O(n) space
        # inorder DFS: in a BST always gives values in sorted order, left -> node -> right, O(n) time and O(n) space 
        """
        if not root: 
            return []
        values = []
        def rec(root): 
            nonlocal values 
            if not root: 
                return
            rec(root.left)
            values.append(root.val)
            rec(root.right)
        rec(root)
        # print(values)
        return values[k-1]
        """

        # DFS with early return (recursive), O(n) time, O(h) space for the recursive call stack 
        cnt = k 
        res = root.val
        def rec(root): 
            nonlocal cnt, res
            if not root: 
                return
            rec(root.left)
            if cnt == 0:
                return 
            cnt -= 1 
            if cnt == 0:
                res = root.val 
                return 
            rec(root.right)
        rec(root)
        return res 

        # iterative DFS 
        stack = [root]
        cnt = k 
        while stack:
            stack.add(root.left)
            curr = stack.pop()
            cnt -= 1 
            if cnt == 0:
                return curr.val
            stack.add(root.right)
        
        
        
