class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        maxL = height[0]

        r = n - 1
        maxR = height[n-1]

        area = 0
        while l < r:
            if maxL < maxR:
                l += 1 
                maxL = max(maxL, height[l])

                if maxL <= maxR:
                    area += maxL - height[l]
            else: 
                r -= 1
                maxR = max(maxR, height[r])
                if maxR <= maxL:
                    area += maxR - height[r]

        

        return area