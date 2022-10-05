def lastStoneWeight(self, stones=[2,7,4,1,8,1]):
    heap = []
    for stone in stones:
        heapq.heappush(heap, -stone)
    while len(heap) >= 2:
        x1 = heapq.heappop(heap)
        x2 = heapq.heappop(heap)
        if x1 != x2:
            heapq.heappush(heap, (x1 - x2))
    print(-heap[-1] if heap else 0)
    return -heap[-1] if heap else 0


