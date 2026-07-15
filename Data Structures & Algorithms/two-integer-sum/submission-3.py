class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i in range(len(nums)):
            myDict[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in myDict and myDict[target - nums[i]] != i:
                return [i, myDict[target - nums[i]]]
