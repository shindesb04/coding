# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = []
    stack = []
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = [root.val]
        self.stack = []
        if not root:
            return

        if not root.right and not root.left:
            return self.answer
        
        def leftB(root):
            if not root:
                return
            if not root.left and not root.right:
                return
            self.answer.append(root.val)
            if root.left:
                leftB(root.left)
            else:
                leftB(root.right)
        
        def leaf(root):
            if not root:
                return
            if not root.right and not root.left:
                self.answer.append(root.val)
            
            leaf(root.left)
            leaf(root.right)

        def rightside(root):
            if not root:
                return
            if not root.right and not root.left:
                return
            
            self.stack.append(root.val)

            if root.right:
                rightside(root.right)
            else:
                rightside(root.left)

        leftB(root.left)
        leaf(root)
        rightside(root.right)
        while self.stack:
            ele = self.stack.pop()
            self.answer.append(ele)
        return self.answer
        
            

        