class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)

        longest = 0
        
        for x in nums:
            if (x - 1) not in sett:
                add = 1
                curr = 1
                while (x + add) in sett:
                    curr += 1
                    add += 1
                
                longest = max(longest, curr)

        return longest