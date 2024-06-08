# 두 수의 합
num = int(input())
for i in range(num):
    ans = 0
    n, K = map(int, input().split())
    numList = list(map(int, input().split()))
    l, r = 0, n - 1
    min = 10000000000
    numList.sort()
    while l < r:
        temp = numList[l] + numList[r]
        if min > (abs(K - temp)):
            min = (abs(K - temp))
            ans = 0 # 초기화
        if temp < K:
            if (abs(K - temp)) == min : ans += 1
            l += 1
        elif temp > K:
            if (abs(K - temp)) == min: ans += 1
            r -= 1
        else:
            ans += 1
            r -= 1

    print(ans)
