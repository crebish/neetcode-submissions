class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            temp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num, num * curMin, temp)
            ans = max(ans, curMax)

        return ans