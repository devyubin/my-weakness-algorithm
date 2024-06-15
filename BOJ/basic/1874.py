# 스택 수열
# [1,2,3,4,5,6,7,8] -> [4, 3, 6, 8, 7, 5, 2, 1]
from collections import deque

n = int(input())
q = deque()
op = []
cnt = 1

for i in range(n):
    num = int(input())
    # 첫 수까지 push
    while cnt <= num:
        q.append(cnt)
        op.append("+")
        cnt += 1
    # 가장 위 수가 같다면
    if q[-1] == num:
        q.pop()
        op.append("-")
    # 안 같으면 NO
    else:
        print("NO")
        exit()

for i in range(len(op)):
    print(op[i])
