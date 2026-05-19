# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs, using a queue 
        q = deque()
        q.append(root)
        while q: 
            node = q.popleft()
            if not node:
                continue 
            if node.left or node.right: 
                temp = node.right 
                node.right = node.left
                node.left = temp 
            if node.left: 
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root 