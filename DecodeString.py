
# Version 3, recrusive
class Solution:
    def decodeString(self, s: str) -> str:
        return self.dfs(s, 0)
    def dfs(self, s, i):
        result = ""
        number = 0
        while i < len(s):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif s[i].isalpha():
                result += s[i]
            elif s[i] == '[':
                i, tmp = self.dfs(s, i + 1)
                result += tmp * number
                number = 0
            else:
                return i, result
            i += 1
        return result

        
# Version 2, stack
# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         num = 0
#         string = ""
#         for char in s:
#             if char.isdigit():
#                 num = 10 * num + int(char)
#             elif char.isalpha():
#                 string += char
#             elif char == '[':
#                 stack.append((string, num))
#                 num = 0
#                 string = ""
#             else:
#                 last_str, last_num = stack.pop(-1)
#                 # string += last_str * last_num
#                 string = last_str + string * last_num
#         return string


# Version 1, stack
# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         # print(s)
#         for char in s:
#             if char != ']':
#                 stack.append(char)
#             else:
#                 sub_string = ""
#                 while len(stack) > 0 and stack[-1] != '[':
#                     sub_char = stack[-1]
#                     stack.pop(-1)
#                     sub_string = sub_char + sub_string
#                 if len(stack) > 0:
#                     stack.pop(-1) # pop '['
#                 # deal with number
#                 number = ""
#                 while len(stack) > 0 and stack[-1] in [str(i) for i in range(10)]:
#                     sub_char = stack[-1]
#                     stack.pop(-1)
#                     number = sub_char + number
#                 # print(number)
#                 number = int(number)
#                 for i in range(number):
#                     stack.append(sub_string)
#         final_string = ""
#         while len(stack) > 0:
#             sub_string = stack[-1]
#             stack.pop(-1)
#             final_string = sub_string + final_string
#         return final_string

if __name__ == "__main__":

    solution = Solution()
    # s = "3[a]2[bc]"
    s = "abc3[cd]xyz"
    decode_s = solution.decodeString(s)
    print(decode_s)


