# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        self.answer = False

        def helper(root, targetSum, cursum):
            #base Condition
            if not root:
                return
            cursum += root.val
            if not root.left and not root.right:
                if cursum == targetSum:
                    self.answer = True
            #Logic
            helper(root.left,targetSum, cursum)
            helper(root.right,targetSum, cursum)
        helper(root, targetSum, 0)
        return self.answer
