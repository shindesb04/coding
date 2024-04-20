# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            size = len(q)
            temp = []
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    temp.append(cur.left.val)
                else:
                    temp.append(101)
                if cur.right:
                    q.append(cur.right)
                    temp.append(cur.right.val)
                else:
                    temp.append(101)
            temp2 = temp[::-1]
            if temp != temp2:
                return False
        return True

        