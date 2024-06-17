# 최대 힙
# 0 1 2 0 0 3 2 1 0 0 0 0 0 -> 0 2 1 3 2 1 0 0
# 0일떄 가장 큰 값을 출력, 그값 배열에서 제거
import heapq
import sys
n = int(input())
lst = []
for i in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(lst, num * -1)
    if num == 0:
        print(heapq.heappop(lst) * -1)