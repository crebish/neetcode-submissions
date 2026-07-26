class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, l, r):
            if r == n:
                ans.append(s)
                return

            if r < l:
                backtrack(s + ')', l, r + 1)

            if l < n:
                backtrack(s +'(', l + 1, r)
            

        backtrack("", 0, 0)

        return ans