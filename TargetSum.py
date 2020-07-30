from typing import List

# DP Version, bottom to top
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        max_sum = sum(nums)
        dp = [[-1 for j in range(-1 * max_sum, max_sum+1)] for i in range(len(nums) + 1)]
        for i in range(-1 * max_sum, max_sum+1):
            dp[len(nums)][i + max_sum] = 1 if i == S else 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(-1 * max_sum, max_sum+1):
                if j + nums[i] < -1 * max_sum or j + nums[i] > max_sum or j - nums[i] < -1 * max_sum or j - nums[i] > max_sum:
                    continue
                dp[i][j + max_sum] = dp[i + 1][j + nums[i] + max_sum] + dp[i + 1][j - nums[i] + max_sum]
        return dp[0][0 + max_sum]



# # DP Version, top to bottom
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         max_sum = sum(nums)
#         dp = [[-1 for j in range(-1 * max_sum, max_sum+1)] for i in range(len(nums))]
#         def update_dp(current_sum, index):
#             if index == len(nums):
#                 if current_sum == S:
#                     return 1
#                 else:
#                     return 0
#             if dp[index][current_sum+max_sum] != -1:
#                 return dp[index][current_sum+max_sum]
#             cnt_left = update_dp(current_sum+nums[index], index+1)
#             cnt_right = update_dp(current_sum-nums[index], index+1)
#             dp[index][current_sum+max_sum] = cnt_left + cnt_right
#             return dp[index][current_sum+max_sum]
#         update_dp(0, 0)
#         return dp[0][0+max_sum]


# Memorization Right
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         max_sum = sum(nums)
#         # memory = [[-1 for j in range(max_sum+1)] for i in range(len(nums))] # wrong since current_sum may be negative
#         memory = [dict() for i in range(len(nums))]
#         # print(memory)
#         def dfs(current_sum, index):
#             if index == len(nums):
#                 if current_sum == S:
#                     return 1
#                 else:
#                     return 0
#             # if memory[index][current_sum] != -1:
#             #     return memory[index][current_sum]
#             if current_sum in list(memory[index].keys()):
#                 return memory[index][current_sum]
#             else:
#                 cnt_left = dfs(current_sum + nums[index], index + 1)
#                 cnt_right = dfs(current_sum - nums[index], index + 1)
#                 # memory[index][current_sum] = cnt_left + cnt_right
#                 memory[index][current_sum] = cnt_left + cnt_right
#                 return memory[index][current_sum]
#
#         count = dfs(0, 0)
#         return count

# Memorization Wrong
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         # max_sum = sum(nums)
#         memory = dict()
#         # self.count = 0
#         def dfs(current_sum, index):
#             # print(current_sum, index)
#             if index == len(nums):
#                 if current_sum == S:
#                     # self.count += 1
#                     return 1
#                 else:
#                     return 0
#             if (current_sum, index) in list(memory.keys()):
#                 return memory[(current_sum, index)]
#             else:
#                 cnt_left = dfs(current_sum + nums[index], index + 1)
#                 cnt_right = dfs(current_sum - nums[index], index + 1)
#                 memory[(current_sum, index)] = cnt_left + cnt_right
#             return memory[(current_sum, index)]
#
#         count = dfs(0, 0)
#         return count

if __name__ == "__main__":
    # nums = [27, 33, 4, 43, 31, 44, 47, 6, 6, 11, 39, 37, 15, 16, 8, 19, 48, 17, 18, 39]
    nums = [1, 1, 1, 1, 1]
    S = 3
    solution = Solution()
    count = solution.findTargetSumWays(nums, S)
    print(count)