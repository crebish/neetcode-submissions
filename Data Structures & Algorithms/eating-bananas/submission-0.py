class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        ans = r

        while l <= r:
            m = (r + l) // 2

            hours = 0
            for x in piles:
                hours += math.ceil(float(x) / m)

            if hours <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1


        return ans