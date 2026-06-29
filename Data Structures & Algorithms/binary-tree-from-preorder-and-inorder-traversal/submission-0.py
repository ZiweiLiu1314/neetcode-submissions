# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first thoughts 
        # preorder: parent before children (not level by level!)
        # inorder: from left to right 
        # no relevant position is assumed 
        # pop a node from the preorder list, append it to this / next level 
        # max # nodes we can have on each level 

        # correct: split using the first node in preorder 
        if not preorder or not inorder: 
            return None 
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # the length of the left subTree 
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # excluding the 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root