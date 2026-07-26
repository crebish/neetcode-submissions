class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr, i):

            if i >= len(nums):
                ans.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)


        backtrack([], 0)


        return ans
