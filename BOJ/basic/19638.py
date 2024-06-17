# 센티와 마법의 뽕망치
# 모든 거인이 센티보다 키가 작도록 할 수 있는 경우 YES
# 가장 키가 큰 거인 가운데 하나 - 뿅망치에 맞은 사람의 키 / 2

import sys
import heapq
n, h, t = map(int, sys.stdin.readline().split())
people = []
cnt = 0

for i in range(n):
    p = int(sys.stdin.readline()) * -1
    heapq.heappush(people, p)

for i in range(t):
    if -people[0] == 1 or -people[0] < h:
        break
    else:
        heapq.heapreplace(people, -(-people[0] // 2))
        cnt += 1

if -people[0] >= h:
    print('NO', -people[0], sep="\n")
else:
    print("YES", cnt, sep="\n")
