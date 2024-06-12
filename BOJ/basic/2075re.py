# n번째 다시 짜기
import heapq
n = int(input())
num_list = []
for i in range(n):
    nums = list(map(int, input().split()))
    if not num_list: # 처음에만 이거 실행
        for num in nums:
            heapq.heappush(num_list, num)
    else:
        for num in nums:
            if num_list[0] < num:
                heapq.heappush(num_list, num)
                heapq.heappop(num_list)
print(num_list[0])