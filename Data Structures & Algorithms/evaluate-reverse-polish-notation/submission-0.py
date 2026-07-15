class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:

            if x == '+':
                r = stack.pop(-1)
                l = stack.pop(-1)
                stack.append(l + r)
            elif x == '-':
                r = stack.pop(-1)
                l = stack.pop(-1)
                stack.append(l - r)
            elif x == '*':
                r = stack.pop(-1)
                l = stack.pop(-1)
                stack.append(l * r)
            elif x == '/':
                r = stack.pop(-1)
                l = stack.pop(-1)
                stack.append(int(float(l / r)))
            else:
                stack.append(int(x))


        return stack[0]