# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return
        
        q = deque([root])
        result = []

        while q:
            size = len(q)
            li = []
            for i in range(size):
                element = q.popleft()
                li.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
                
            result.append(li)
        return result
        