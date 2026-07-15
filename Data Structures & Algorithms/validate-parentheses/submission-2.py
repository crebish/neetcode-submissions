class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)

            elif x == ")":
                if not stack or stack.pop(-1) != "(":
                    return False

            elif x == "]":
                if not stack or stack.pop(-1) != "[":
                    return False

            elif x == "}":
                if not stack or stack.pop(-1) != "{":
                    return False

        if stack:
            return False

        return True