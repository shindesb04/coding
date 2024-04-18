# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        
        while q:
            size = len(q)
            xfound = False
            yfound = False
            
            for i in range(size):
                element = q.popleft()
                if x == element.val:
                    xfound = True
                if y == element.val:
                    yfound = True

                if element.left and element.right:
                    if element.left.val == x and element.right.val == y:
                        return False 
                    if element.left.val == y and element.right.val == x:
                        return False
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            if xfound and yfound:
                return True
            if xfound or yfound:
                return False

        return False
        

        