class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        n = len(s)

        for x in range(n):
            l = r = x

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1
            if len(ans) < (r - l + 1):
                ans = s[l:r+1]

            l = x
            r = x + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1
            if len(ans) < (r - l + 1):
                ans = s[l:r+1]

        return ans