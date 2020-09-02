# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_intersect(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        return None
    def detectCycle(self, head: ListNode) -> ListNode:
        intersect = self.get_intersect(head)
        if intersect is None:
            return None
        p1 = head
        p2 = intersect
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
