# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        prev = head

        if not head or not head.next:
            return

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        a = head
        b = prev
        aprev = None
        while a:
            aprev = b
            tempa = a.next
            tempb = b.next
            a.next = b
            a.next.next = tempa
            a = tempa
            b = tempb
        if tempb:
            aprev.next = tempb

        

        