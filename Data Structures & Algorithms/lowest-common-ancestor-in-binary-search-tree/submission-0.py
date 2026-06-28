# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check each of the node, if p or q is its children, we've found it 
        # BFS 
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        # print(f"val1={val1}, val2={val2}")
        while root:
            # print(f"roor.val = {root.val}")
            if val1 <= root.val and root.val <= val2: 
                return root
            elif root.val < val1: 
                root = root.right
            else: 
                root = root.left
        raise Exception("p and q not found")
