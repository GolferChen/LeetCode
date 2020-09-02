from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if head is None:
#             return head
#         p_fast = head
#         p_slow = head
#         move_count = 0
#         while p_fast and p_fast.next:
#             p_slow = p_slow.next
#             p_fast = p_fast.next.next
#             move_count += 1
#         if p_fast.next is None: # p_fast is at the end of the list
#
#         else: # p_fast is None

# Time: O(L), one recursion; Space: O(L); Not using sentinel node
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if head is None:
#             return head
#         store = deque()
#         p = head
#         while p:
#             store.append(p)
#             p = p.next
#         size = len(store)
#         if size - n - 1 < 0:
#             return head.next
#         pre = store[size - n - 1]
#         after = store[size - n + 1] if size - n + 1 < size else None
#         pre.next = after
#         return head

# Time: O(L), one recursion; Space: O(L); Using sentinel node
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if head is None:
#             return head
#         store = deque()
#         sentinel = ListNode(0)
#         sentinel.next = head
#         p = sentinel
#         while p:
#             store.append(p)
#             p = p.next
#         size = len(store) - 1
#         # if size - n - 1 + 1< 0:
#         #     return head.next
#         pre = store[size - n - 1 + 1]
#         after = store[size - n + 1 + 1] if size - n + 1 + 1 < size + 1 else None
#         pre.next = after
#         return sentinel.next

# Double Pointer, One recursion, O(1) space; Using sentinel node
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        p_slow = sentinel
        p_fast = sentinel
        for i in range(n):
            p_fast = p_fast.next
        while p_fast.next:
            p_fast = p_fast.next
            p_slow = p_slow.next
        p_slow.next = p_slow.next.next
        return sentinel.next 