import heapq

sv_list = []
scoville = [1, 1, 1, 1, 1, 1, 1, 6, 6]

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) >= 2:
            cnt += 1
            ans = heapq.heappop(scoville)
            ans += heapq.heappop(scoville)*2

            heapq.heappush(scoville, ans)
        else:
            return -1
    return cnt

print(solution(scoville, 7))
