# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # first of all, search for the subroot in the tree of root 
        # then if it's contained, we use dfs/bfs to check if children (...) are the same 
        # bfs for looking for Subroot 
        q = deque()
        q.append(root)
        node = None 
        roots = deque()
        while q: 
            node = q.popleft()
            if node.val == subRoot.val: 
                roots.append(node)
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
        # node is the 'subroot' in the first binary tree 
        if not node: 
            return False 
        while roots: 
            root1 = roots.pop()
            print('checking root1')
            res = self.check_trees(root1, subRoot)
            if res: 
                return True 
        return False 


    def check_trees(self, root1, root2): 
        #bfs 
        q1 = deque() # the bfs queue for traversing through the first binary tree, starting from root1 
        q2 = deque() 
        q1.append(root1)
        q2.append(root2)
        while q1 and q2: 
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1 and node2: 
                if node1.val != node2.val:
                    print(f'different values, {node1.val} and {node2.val}')
                    return False 
            elif node1 or node2:
                print('different structure')
                return False 
            else:
                continue 
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
        if q1 or q2: 
            print('queues not empty in the end')
            return False 
        return True 

