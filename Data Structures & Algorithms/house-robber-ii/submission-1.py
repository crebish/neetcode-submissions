class Solution:
    def rob(self, nums: List[int]) -> int:
        ans1 = ans2 = 0

        n = len(nums)

        if n < 3:
            if n < 2:
                return nums[0]

            return max(nums[0], nums[1])

        l = nums[0]
        r = max(nums[0], nums[1])
        for x in range(2, n - 1):
            temp = nums[x] + l

            l = r
            r = max(r, temp)

        ans1 = r

        l = nums[1]
        r = max(nums[1], nums[2])
        for x in range(3, n):
            temp = nums[x] + l
            l = r
            r = max(r, temp)

        ans2 = r


        return max(ans1, ans2)