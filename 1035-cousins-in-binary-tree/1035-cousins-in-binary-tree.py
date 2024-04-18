# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        p = deque([None])
        
        while q:
            size = len(q)
            xfound = False
            yfound = False
            xpar = None
            ypar = None
            for i in range(size):
                element = q.popleft()
                parent = p.popleft()
                if x == element.val:
                    xfound = True
                    xpar = parent
                if y == element.val:
                    yfound = True
                    ypar = parent
                if element.left:
                    q.append(element.left)
                    p.append(element)
                if element.right:
                    q.append(element.right)
                    p.append(element)
            if xfound and yfound:
                return xpar != ypar
            if xfound or yfound:
                return False

        return True
        

        