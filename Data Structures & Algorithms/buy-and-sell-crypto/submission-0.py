class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        l = 0
        for r in range(len(prices)):

            while prices[l] > prices[r]:
                l += 1

            ans = max(ans, prices[r] - prices[l])


        return ans