# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    st = []
    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.dfs(root)

    def dfs(self, root):

        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:

        cur = self.st.pop()
        self.dfs(cur.right)
        return cur.val
        
    def hasNext(self) -> bool:
        if self.st:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()