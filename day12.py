import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            dif = -abs(x-y)
            heapq.heappush(stones, dif)
        return abs(heapq.heappop(stones))