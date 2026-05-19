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
        # dfs 
        stack = []
        stack.append(root)
        while stack: 
            node = stack.pop()
            if node in visited: 
                continue 
            visited.add(node)
            # swap 
            temp = node.left 
            node.left = node.right 
            node.right = temp 
            # add children into stack 
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
        return root 
