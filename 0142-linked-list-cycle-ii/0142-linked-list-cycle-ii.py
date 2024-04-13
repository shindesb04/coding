# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        cur = ListNode()
        counter = 0
        # if not head.next:
        #     return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                counter = 1
                break
        if counter == 0:
            return
        slow = head

        while slow:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
