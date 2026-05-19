# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return root 
        visited = set()
        def dfs(node): 
            if not node: 
                return 
            visited.add(node)

            temp = node.left
            node.left = node.right
            node.right = temp 

            if node.left: 
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return root 