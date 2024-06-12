# 중앙값 구하기 - 다시보기
import heapq

T = int(input())
for _ in range(T):
    M = int(input())
    nums = []
    for _ in range(M // 10 + 1):
        nums += list(map(int, input().split()))

    left, right, ans = [], [], [nums[0]]
    mid = nums[0]

    for i, num in enumerate(nums[1:], 1):
        if num < mid:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        if i % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            ans.append(mid)

    print(M // 2 + 1)
    for i, num in enumerate(ans):
        if i != 0 and i % 10 == 0:
            print()
        print(num, end=' ')
    print()