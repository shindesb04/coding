# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque()
        q.append(root.left)
        q.append(root.right)

        while q:
            left = q.popleft()
            right = q.popleft()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True