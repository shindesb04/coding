# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    li = []
    index = 0
    def __init__(self, root: Optional[TreeNode]):
        self.li = []
        self.index = 0
        self.inorder(root)
    def inorder(self, root):
        #base
        if not root:
            return
        #logic
        self.inorder(root.left)
        self.li.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        result = self.li[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        if self.index != len(self.li):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()