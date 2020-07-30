# from typing import List
#
#
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         days = [0] * len(T)
#         # stack_t = [] // no need to use this stack
#         stack_index = []
#         for index, t in enumerate(T):
#             # if len(stack_t) == 0:
#             #     stack_t.append(t)
#             #     stack_index.append(index)
#             # else:
#             #     if t <= stack_t[-1]:
#             #         stack_t.append(t)
#             #         stack_index.append(index)
#             #     else:
#             #         while len(stack_t) != 0 and t > stack_t[-1]:
#             #             index_top = stack_index[-1]
#             #             stack_t.pop(-1)
#             #             stack_index.pop(-1)
#             #             days[index_top] = index - index_top
#             #         stack_t.append(t)
#             #         stack_index.append(index)
#
#             # combine to a single case
#             while len(stack_index) != 0 and t > T[stack_index[-1]]:
#                 index_top = stack_index[-1]
#                 stack_index.pop(-1)
#                 days[index_top] = index - index_top
#             stack_index.append(index)
#         return days

# Version Two, from tail to head
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        days = [0] * len(T)
        stack_index = []
        for index in range(len(T) - 1, -1, -1): # from tail to head
            t = T[index]
            while len(stack_index) != 0 and t >= T[stack_index[-1]]: # pop those elements which are no larger than t
                stack_index.pop(-1)
            if len(stack_index) != 0:
                days[index] = stack_index[-1] - index
            stack_index.append(index)
        return days