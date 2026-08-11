class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n = len(s)
        def dfs(i):
            if i >= n:
                return 1
            if i in memo:
                return memo[i]

            if s[i] == "0":
                return 0

            ans = 0
            if i < (n - 1) and (s[i] == "1" or 
                (s[i] == "2" and s[i+1] in "0123456")):
                ans = dfs(i+2)


            ans += dfs(i+1)
            memo[i] = ans
            return ans

        return dfs(0)