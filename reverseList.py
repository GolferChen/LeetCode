# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Iterative Verison, self implemented
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return head
#         p = head.next
#         head_new = head
#         while p:
#             p_next = p.next
#             p.next = head_new
#             head_new = p
#             p = p_next
#         head.next = None
#         return head_new

# Iteration Version, Official Version
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         p = head
#         prev = None
#         while p:
#             p_next = p.next
#             p.next = prev
#             prev = p
#             p = p_next
#         return prev

# Recursion Version, self Version
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def recursion(current_node):
#             if current_node.next is None:
#                 return current_node
#             head_new = recursion(current_node.next)
#             current_node.next.next = current_node
#             return head_new
#         if head is None:
#             return head
#         head_new = recursion(head)
#         head.next = None
#         return head_new


# Recursion Version, Official Version
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head_new = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return head_new

