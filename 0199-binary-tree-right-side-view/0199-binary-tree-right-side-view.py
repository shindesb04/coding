# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return
        q = deque([root])
        answer = [root.val]

        while q:
            size = len(q)
            temp = []
            for i in range(size):
                ele = q.popleft()
                if ele.left:
                    q.append(ele.left)
                    temp.append(ele.left.val)

                if ele.right:
                    q.append(ele.right)
                    temp.append(ele.right.val)
            if q:
                answer.append(temp[len(temp) - 1])
            
        return answer
        