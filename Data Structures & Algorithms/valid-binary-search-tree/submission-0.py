# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS 
        # each of left child of a node: < node.val, > node's left boundary (if the node is the right child 
        # of another node, it would have a left boundary) 
        # each of the right child a node: > node.val, < node's right boundary (if the node is the left child 
        # of another node, it would have a right boundary) 
        def rec(root, left, right):
            if not root: 
                return True 
            if not (root.val > left and root.val < right): 
                return False 
            return rec(root.left, left, root.val) and rec(root.right, root.val, right)
        return rec(root, float("-inf"), float("inf"))