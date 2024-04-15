# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return
            
        result = []
        q = deque([root])
        

        while q:
            size = len(q)
            li = []
            for i in range(size):
                ele = q.popleft()
                li.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            result.append(li)
        return result[::-1]
        