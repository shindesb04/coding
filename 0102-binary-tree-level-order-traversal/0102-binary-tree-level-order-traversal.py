# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []

        def dfs(root, height):

            if not root:
                return
            if len(self.result) == height:
                self.result.append(list())
            self.result[height].append(root.val)
            dfs(root.left, height + 1)
            dfs(root.right, height + 1)
        dfs(root, 0)
        return self.result
        