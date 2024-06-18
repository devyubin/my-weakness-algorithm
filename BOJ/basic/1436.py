# 영화감독 숌
# 완전 탐색 풀이로 진행.
"""
아래 처럼 숫자로 안풀고
 while cnt != n:
     idx += 1
     if '666' in str(idx)
        cnt += 1
 print(idx)
 로 풀면 더 간단.
"""

def count_num(num):
    count = 0
    while num > 0:
        tmp = 0
        # 수를 다 나눔
        tmp = num % 10
        num //= 10
        # 666이 연속으로 있는지 확인
        if tmp == 6:
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


import sys

n = int(sys.stdin.readline())
num = 666
cnt = 0
while cnt != n:
    # 666 이 있는가?
    if count_num(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1
