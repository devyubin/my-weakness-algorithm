# 요세푸스 문제 - RE
# 7명 -> 3번째 / 1234567 -> 12[3]4567 -> 12[3]45[6]7 -> 1[2][3]45[6]7 -> ...
from collections import deque

n, k = map(int, input().split())
list = []
q = deque([i + 1 for i in range(n)])

while len(q) != 0:
    q.rotate(-k)
    list.append(q.pop())

print("<" + ", ".join(map(str, list)) + ">")
