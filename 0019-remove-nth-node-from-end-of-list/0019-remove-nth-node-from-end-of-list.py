# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 Pass
        length = 0

        if not head.next:
            return
        
        cur = head
        while cur:
            length += 1
            cur = cur.next
        length = length - n
        dummy = ListNode(-1)
        cur = dummy
        cur.next = head

        while length:
            cur = cur.next
            length -= 1
        cur.next = cur.next.next
        return dummy.next