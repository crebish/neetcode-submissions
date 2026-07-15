class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()

        for x in nums:
            if x in sett:
                return True

            sett.add(x)

        return False