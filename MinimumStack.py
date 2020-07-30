# from math import inf
#
#
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.min = inf
#         self.min_location = inf
#
#
#     def push(self, x: int) -> None:
#         self.data.append(x)
#         if x < self.min:
#             self.min = x
#             self.min_location = len(self.data) - 1
#
#
#     def pop(self) -> None:
#         if len(self.data) == 0:
#             exit(0)
#         self.data.pop(len(self.data) - 1)
#         # if self.min_location == len(self.data) - 1: # re-locate the min
#         if self.min_location == len(self.data): # re-locate the min
#             if len(self.data) == 0:
#                 self.min = inf
#                 self.min_location = inf
#             else:
#                 self.min = min(self.data)
#                 for index, item in enumerate(self.data):
#                     if item == self.min:
#                         self.min_location = index
#                         break
#
#
#     def top(self) -> int:
#         if len(self.data) == 0:
#             exit(0)
#         return self.data[len(self.data) - 1]
#
#
#     def getMin(self) -> int:
#         if len(self.data) == 0:
#             exit(0)
#         return self.min


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            if x < self.min[-1]:
                self.min.append(x)
            else:
                self.min.append(self.min[-1])


    def pop(self) -> None:
        if len(self.data) == 0:
            return
        self.data.pop(-1)
        self.min.pop(-1)


    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.min[-1]
