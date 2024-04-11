# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        #base case 
        if len(preorder) == 0:
            return
        rootval = preorder[0]
        root = TreeNode(rootval)
        #logic
        rootidx = -1
        for i in range(len(inorder)):
            if inorder[i] == rootval:
                rootidx = i
        
        inleft = inorder[0 : rootidx]
        inright = inorder[rootidx + 1 : len(inorder)]
        preleft = preorder[1: len(inleft) + 1]
        preright = preorder[len(inleft) + 1 : len(preorder)]

        root.left = self.buildTree(preleft, inleft)
        root.right = self.buildTree(preright, inright)
        return root
        