# 과제
# 하루에 한 과제를 끝낼 수 있다.
# 3 30 -> 2 50 -> 4 40 -> 4 60 -> 6 5
# 현재 단계에서 가장 높은 효율을 어떻게 구할까? -> 도출 못해서 블로그 참조..
# 최대 힙, d w
import heapq
n = int(input().strip())
ans = 0
score = []
day = [0] * (n+1)

for _ in range(n):
    d, w = map(int, input().strip().split())
    heapq.heappush(score, (-w, d))

while score:
    w, d = heapq.heappop(score)
    w = -w

    # (***중요***) d 값이 n을 초과하지 않도록 조정
    d = min(d, n)

    for i in range(d, 0, -1):
        if day[i]:
            continue
        day[i] = 1
        ans += w
        break

print(ans)