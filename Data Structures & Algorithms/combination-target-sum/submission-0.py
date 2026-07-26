class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(i, summ):
            if i >= len(nums):
                if summ == target:
                    ans.append(curr.copy())
                    
                return

            if summ > target:
                return

            curr.append(nums[i])
            backtrack(i, summ + nums[i])
            curr.pop()
            backtrack(i + 1, summ)

        backtrack(0, 0)
        return ans