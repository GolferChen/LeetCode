
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Single List, without sentinel node
# class MyLinkedList:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.header = None
#         self.size = 0
#
#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index < 0 or index >= self.size:
#             return -1
#         cur_node = self.header
#         # while cur_node:
#         #     cur_node = cur_node.next
#         # for i in range(index - 1): // wrong
#         for i in range(index):
#             cur_node = cur_node.next
#         return cur_node.val
#
#
#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         new_node = Node(val)
#         new_node.next = self.header
#         self.header = new_node
#         self.size += 1
#
#
#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         tail_node = self.header
#         for i in range(self.size - 1):
#             tail_node = tail_node.next
#         new_node = Node(val)
#         if tail_node:
#             tail_node.next = new_node
#         else:
#             self.header = new_node
#         self.size += 1
#
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         # if index == self.size:
#         #     self.addAtTail(val)
#         #     return
#         # if index > self.size:
#         #     return
#         # if index < 0:
#         #     self.addAtHead(val)
#         #     return
#         if index <= 0:
#             self.addAtHead(val)
#             return
#         if index == self.size:
#             self.addAtTail(val)
#             return
#         if index > self.size:
#             return
#
#         cur_node = self.header
#         for i in range(index - 1):
#             cur_node = cur_node.next
#         new_node = Node(val)
#         new_node.next = cur_node.next
#         cur_node.next = new_node
#         self.size += 1
#
#
#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index < 0 or index >= self.size:
#             return
#         if index >= 1:
#             cur_node = self.header
#             for i in range(index - 1):
#                 cur_node = cur_node.next
#             cur_node.next = cur_node.next.next
#         else:
#             self.header = self.header.next
#         self.size -= 1

# Single List, with sentinel node
# class MyLinkedList:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.size = 0
#         self.sentinel = Node(0)
#
#
#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index < 0 or index >= self.size:
#             return -1
#         cur_node = self.sentinel
#         for i in range(index + 1):
#             cur_node = cur_node.next
#         return cur_node.val
#
#
#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         self.addAtIndex(0, val)
#
#
#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         self.addAtIndex(self.size, val)
#
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0  # add to head
#         pre_node = self.sentinel
#         for i in range(index):
#             pre_node = pre_node.next
#         new_node = Node(val)
#         new_node.next = pre_node.next
#         pre_node.next = new_node
#         self.size += 1
#
#
#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index < 0 or index >= self.size:
#             return
#         pre_node = self.sentinel
#         for i in range(index):
#             pre_node = pre_node.next
#         pre_node.next = pre_node.next.next
#         self.size -= 1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None

# double List
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.sentinel_head = Node(0)
        self.sentinel_tail = Node(0)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.pre = self.sentinel_head


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        head_step = index + 1
        tail_step = self.size - head_step + 1
        # if index <= self.size // 2:
        if head_step <= tail_step:
            cur_node = self.sentinel_head
            for i in range(head_step):
                cur_node = cur_node.next
            return cur_node.val
        else:
            cur_node = self.sentinel_tail
            for i in range(tail_step):
                cur_node = cur_node.pre
            return cur_node.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        head_step = index - 1 + 1
        tail_step = self.size - head_step + 1
        if head_step <= tail_step:
            pre_node = self.sentinel_head
            for i in range(head_step):
                pre_node = pre_node.next
        else:
            pre_node = self.sentinel_tail
            for i in range(tail_step):
                pre_node = pre_node.pre
        new_node = Node(val)
        new_node.next = pre_node.next
        new_node.pre = pre_node
        pre_node.next.pre = new_node
        pre_node.next = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        head_step = index - 1 + 1
        tail_step = self.size - head_step + 1
        if head_step <= tail_step:
            pre_node = self.sentinel_head
            for i in range(head_step):
                pre_node = pre_node.next
        else:
            pre_node = self.sentinel_tail
            for i in range(tail_step):
                pre_node = pre_node.pre
        pre_node.next.next.pre = pre_node
        pre_node.next = pre_node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# if __name__ == "__main__":
#     # Your MyLinkedList object will be instantiated and called as such:
#     linkedList = MyLinkedList()
#     # linkedList.addAtHead(1)
#     # linkedList.addAtTail(3)
#     linkedList.addAtIndex(0, 10)
#     linkedList.addAtIndex(0, 20)
#     linkedList.addAtIndex(1, 30)
#     linkedList.get(0)
    # linkedList.deleteAtIndex(1)
    # linkedList.get(1)