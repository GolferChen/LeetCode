# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Version One, self implemented
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         p1 = headA
#         p2 = headB
#         while p1 and p2:
#             if p1 == p2:
#                 return p1
#             if p1.next is None and p2.next is None:
#                 return None
#             if p1.next:
#                 p1 = p1.next
#             else:
#                 p1 = headB
#             if p2.next:
#                 p2 = p2.next
#             else:
#                 p2 = headA
#         return None

# Official Version
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

