# 두 수의 합
n = int(input())
list = list(map(int, input().split()))
ans = int(input())
cnt = 0
list.sort()

left = 0
right = n - 1

while left < right:
    temp = list[left] + list[right]
    if temp == ans:
        cnt += 1
        left += 1
    elif temp < ans:
        left += 1
    else:
        right -= 1
print(cnt)