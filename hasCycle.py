
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Self Version
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if head is None:
#             return False
#         fast_pointer = head
#         slow_pointer = head
#         # while fast_pointer and fast_pointer.next and slow_pointer:
#         while fast_pointer and fast_pointer.next:
#             fast_pointer = fast_pointer.next.next
#             slow_pointer = slow_pointer.next
#             if fast_pointer == slow_pointer:
#                 return True
#         return False

# Official Version
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        fast_pointer = head.next
        slow_pointer = head
        while fast_pointer != slow_pointer:
            if fast_pointer is None or fast_pointer.next is None:
                return False
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        return True


