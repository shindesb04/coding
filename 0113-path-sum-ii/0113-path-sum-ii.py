# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []

        def helper(root, targetSum, cursum, curlist):

            if not root:
                return
            cursum += root.val
            curlist.append(root.val)
            if not root.right and not root.left:
                if cursum == targetSum:
                    self.answer.append(curlist)
            
            #logic
            helper(root.left, targetSum, cursum, list(curlist))
            helper(root.right, targetSum, cursum, list(curlist))
        
        helper(root, targetSum, 0, [])
        return self.answer
