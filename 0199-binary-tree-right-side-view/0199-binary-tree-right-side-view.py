# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        def dfs(root, height):

            #base
            if not root:
                return
            #logic
            if height == len(self.answer):
                self.answer.append(root.val)
            dfs(root.right, height + 1)
            dfs(root.left, height + 1)
        dfs(root,0)
        return self.answer