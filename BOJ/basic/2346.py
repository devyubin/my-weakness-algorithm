# 풍선 터뜨리기
# 3, 2, 1, -3, -1 -> 3 -3 -1 1 2
from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while len(q) > 0:
    ans_idx, idx = q.popleft()
    ans.append(ans_idx + 1)

    if idx > 0:
        q.rotate(-(idx - 1))
    elif idx < 0:
        q.rotate(-idx)

print(' '.join(map(str, ans)))
