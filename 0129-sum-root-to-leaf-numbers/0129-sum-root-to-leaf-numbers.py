# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def helper(root, curnum):
            
            #base   
            if not root:
                return

            curnum = curnum * 10 + root.val
            if not root.left and not root.right:
                print(curnum)
                self.total += curnum
            

            helper(root.left, curnum)
            
            helper(root.right, curnum)
        helper(root, 0)
        return self.total