# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        # BFS, using queue, traverse each level and append all values in each level to the list 
        queue = deque([[root, 0]]) # fifo 
        sublist = []
        reslist = []
        level = 0 
        while queue: 
            curr, curr_level = queue.popleft()
            if curr_level == level: 
                sublist.append(curr.val)
            else: 
                reslist.append(sublist) 
                level += 1 
                sublist = []
                sublist.append(curr.val)
            if curr.left:
                queue.append([curr.left, curr_level + 1])
            if curr.right:
                queue.append([curr.right, curr_level + 1])
        reslist.append(sublist) 
        return reslist 


