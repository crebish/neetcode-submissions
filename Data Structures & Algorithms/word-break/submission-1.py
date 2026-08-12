class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sett = set(wordDict)
        memo = {}
        n = len(s)
        t = 0
        for w in sett:
            t = max(t, len(w))
        
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return True
            
            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in sett:
                    if dfs(j + 1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        
        return dfs(0)