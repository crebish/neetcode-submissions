class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            cooldown = dfs(i+1, buy)
            curr = 0
            if buy:
                curr = dfs(i+1, False) - prices[i]
                dp[(i, buy)] = max(curr, cooldown)
            else:
                curr = dfs(i+2, True) + prices[i]
                dp[(i, buy)] = max(curr, cooldown)

            return dp[(i, buy)]




        return dfs(0, True)

        
