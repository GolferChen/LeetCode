from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for char in tokens:
            if not (char in operators):
                stack.append(int(char))
            else:
                if len(stack) < 2:
                    return
                else:
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    c = self.calculate(a, char, b)
                    stack.append(c)
        return stack[-1]

    def calculate(self, a, operator, b):
        if operator == '+':
            return a + b
        if operator == '-':
            return a - b
        if operator == '*':
            return a * b
        if operator == '/':
            return int(a // b)
        return
