from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heappush(heap, i)
    
    if len(heap) < 2:
        return answer
    
    while heap[0] < K:
        m1 = heappop(heap)
        m2 = heappop(heap)
        heappush(heap, m1 + m2*2)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer