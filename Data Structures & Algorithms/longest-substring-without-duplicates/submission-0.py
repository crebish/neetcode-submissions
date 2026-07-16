class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        maxx = 1
        sett = set()
        l = 0
        r = 0
        sett.add(s[l])
        while r < n - 1:
            r += 1
            if s[r] in sett:
                while True:
                    if s[l] == s[r]:
                        l += 1
                        break
                    else:
                        sett.remove(s[l])
                        l += 1

            else:
                sett.add(s[r])
                maxx = max(maxx, r - l + 1)



        return maxx