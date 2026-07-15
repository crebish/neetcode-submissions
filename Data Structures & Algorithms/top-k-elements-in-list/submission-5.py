class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                
                if len(ans) == k:
                    return ans
            
        
