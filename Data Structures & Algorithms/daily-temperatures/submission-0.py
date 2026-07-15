class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = []

        for i, x in enumerate(temperatures):
            while stack and x > stack[-1][0]:
                temp, idx = stack.pop()
                ans[idx] = i - idx
            
            
            stack.append((x, i))




        return ans