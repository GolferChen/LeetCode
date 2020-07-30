class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n_brackets = len(s)
        if n_brackets == 0:
            return True
        for i in range(n_brackets):
            char = s[i]
            if len(stack) == 0:
                stack.append(char)
            else:
                match_flag = self.is_match(stack[-1], char)
                if match_flag:
                    stack.pop(-1)
                else:
                    stack.append(char)

        return len(stack) == 0

    def is_match(self, a, b):
        if a == '(':
            return b == ')'
        if a == '[':
            return b == ']'
        if a == '{':
            return b == '}'
