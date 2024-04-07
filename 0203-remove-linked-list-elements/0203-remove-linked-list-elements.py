# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = ListNode(-1)
        prev.next = head
        start = prev

        while cur:
            if cur.val == val:
                temp = cur.next
                prev.next = cur.next
                cur = temp
            else:
                prev = cur
                cur = cur.next
        return start.next