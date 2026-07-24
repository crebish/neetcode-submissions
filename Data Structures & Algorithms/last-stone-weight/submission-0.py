class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1: 
            big = -(heapq.heappop(max_heap))
            small = -(heapq.heappop(max_heap))

            if big > small:
                heapq.heappush(max_heap, -(big - small))

        if max_heap:
            return -(max_heap[0])

        return 0
