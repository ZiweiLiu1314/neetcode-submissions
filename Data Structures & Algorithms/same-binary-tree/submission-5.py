# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def append_children(self, node: Optional[TreeNode], stack):
        if node.left: 
            stack.append(node.left)
        if node.right: 
            stack.append(node.right)
        return stack 

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs checking 
        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if node_p and node_q: 
                if node_p.val != node_q.val:
                    return False 
            elif node_p or node_q: 
                return False 
            else: 
                continue 
            # check if values are the same for both parent node and children node 
            """
            if node_p.left and node_q.left: 
                if node_p.left.val != node_q.left.val:
                    return False 
            elif node_p.left or node_q.left: 
                return False 
            if node_p.right and node_q.right: 
                if node_p.right.val != node_q.right.val:
                    return False 
            elif node_p.right or node_q.right: 
                return False 
            stack_p = self.append_children(node_p, stack_p)
            stack_q = self.append_children(node_q, stack_q)
            """
            stack_p.append(node_p.left)
            stack_p.append(node_p.right)
            stack_q.append(node_q.left)
            stack_q.append(node_q.right)
        if stack_p or stack_q:
            return False 
        return True 
        