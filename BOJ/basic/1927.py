# 최소 힙
import heapq
n = int(input())
cnt = 0
least_heap = []
ans = []

for _ in range(n):
    num = int(input())
    if num == 0:
        # 배열이 빈 경우
        if len(least_heap) == 0:
            ans.append(0)
        else:
            answer = heapq.heappop(least_heap)
            ans.append(answer)
    else:
        heapq.heappush(least_heap, num)

for i in range(len(ans)):
    print(ans[i])