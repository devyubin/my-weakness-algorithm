# 중앙값 RE
import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    # 숫자들을 입력받아 nums 리스트에 저장 - 한 줄에 10개씩 나누어져있고
    for _ in range(m // 10 + 1):
        nums += list(map(int, input().split()))
    l, r, ans = [], [], [nums[0]]
    mid = nums[0]

    # nums 리스트의 첫 번째 숫자를 제외한 나머지 숫자들을 순회
    for i, num in enumerate(nums[1:], 1):
        if num < mid:
            heapq.heappush(l, -num)
        else:
            heapq.heappush(r, num)

        if i % 2 == 0:
            if len(l) > len(r):
                heapq.heappush(r, mid)
                mid = -heapq.heappop(l)
            elif len(l) < len(r):
                heapq.heappush(l, -mid)
                mid = heapq.heappop(r)
            ans.append(mid)

    print(m // 2 + 1)
    for i, num in enumerate(ans):
        if i != 0 and i % 10 == 0:
            print()
        print(num, end=' ')
    print()
