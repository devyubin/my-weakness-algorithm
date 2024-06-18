# 퇴사 - 문제 다시 보기

def sol(day, money):
    # 만약 현재 날이 N을 넘었다면
    if day > n:
        return money

    # 현재 날에 상담을 하지 않는 경우
    result = sol(day + 1, money)

    # 현재 날에 상담을 하는 경우 (단, 상담이 가능한지 체크)
    if day + cnsl[day][0] - 1 <= n:
        result = max(result, sol(day + cnsl[day][0], money + cnsl[day][1]))
    return result


import sys

n = int(sys.stdin.readline())
cnsl = [None]  # 상담 일정을 저장할 리스트, 인덱스 1부터 사용
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    cnsl.append((t, p))

# 첫째 날부터 상담 시작, 현재까지의 수익은 0
print(sol(1, 0))
