# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def helper(root, lnode, rnode):
            if not root:
                return
            if lnode >= root.val or rnode <= root.val:
                self.flag = False
            
            helper(root.left, lnode, root.val)
            helper(root.right, root.val, rnode)
        
        helper(root, float('-inf'), float('inf'))
        return self.flag