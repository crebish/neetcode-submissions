class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i, total, curr):
            if total == target:
                ans.append(curr.copy())
                return
            if i >= len(candidates):
                return
            if target < total:
                return

            curr.append(candidates[i])
            dfs(i+1, total + candidates[i], curr)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, total, curr)


        dfs(0, 0, [])
        return ans