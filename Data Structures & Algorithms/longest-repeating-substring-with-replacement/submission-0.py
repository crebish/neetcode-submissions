class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        l = r = 0
        count = {}
        count[s[l]] = 1
        maxx = 1
        maxChar = 0
        while r < n - 1:
            r += 1
            count[s[r]] = 1 + count.get(s[r], 0)

            maxChar = max(maxChar, count[s[r]])

            if (r - l + 1) - maxChar <= k:
                maxx = max(maxx, r - l + 1)

            else:
                count[s[l]] -= 1
                l += 1
        

        return maxx