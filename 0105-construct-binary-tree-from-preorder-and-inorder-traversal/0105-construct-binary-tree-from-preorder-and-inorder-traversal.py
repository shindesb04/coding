# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rootmap = {}
    idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.rootmap = {}
        self.idx = 0

        for i in range(len(inorder)):
            self.rootmap[inorder[i]] = i

        def helper(inorder, preorder, start, end, rootidx):
            #base
            if start > end:
                return
            
            #logic
            rootval = preorder[self.idx]
            self.idx += 1

            rootidx = self.rootmap[rootval]
            root = TreeNode(rootval)

            root.left = helper(inorder, preorder, start, rootidx - 1, rootidx)
            root.right = helper(inorder, preorder, rootidx + 1, end, rootidx)

            return root

        return helper(inorder, preorder, 0, len(inorder) - 1, 0)