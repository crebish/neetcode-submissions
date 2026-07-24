class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def pythag(x, y):

            return math.sqrt(x ** 2 + y ** 2)

        heap = []

        for point in points:
            dis = pythag(point[0], point[1])

            heapq.heappush(heap, (dis, point))

        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans