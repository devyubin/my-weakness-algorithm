# 전생슬 - 왜 시간초과인지 모르겠다...
# 곱의 합이 최소. 문제가 잘 이해안됨. -> 풀이 찾아보니 계속 곱하는 거 같음 (3 x 10) x (3 x 10 x 2) x (3 x 10 x 2 x 8) x ... -> 가장 먼저 뽑은 수가 계속 반복되니 작은 수부터 뽑아야 함.
import heapq
import sys

slime_energy = []
t = int(sys.stdin.readline())
sum = 0
ans = 1

for _ in range(t):
    sum = 0
    n = int(sys.stdin.readline())
    slime_energy = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(slime_energy)
    result = 1

    if n != 1:
        for _ in range(n-1):
            # 가장 작은 두 수를 곱함
            num1 = heapq.heappop(slime_energy)
            num2 = heapq.heappop(slime_energy)
            sum = num2 * num1
            heapq.heappush(slime_energy, sum)
            ans *= sum
        print(ans % 1000000007)
    else:
        print(1)