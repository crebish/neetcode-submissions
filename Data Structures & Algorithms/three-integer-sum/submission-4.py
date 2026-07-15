class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i, x in enumerate(nums):
            if x > 0:
                break

            if i > 0 and x == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                threeSum = x + nums[l] + nums[r]
                if threeSum == 0:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif threeSum < 0:
                    l += 1
                else: 
                    r -= 1

        return ans