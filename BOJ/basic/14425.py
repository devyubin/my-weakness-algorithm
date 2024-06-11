# 문자열 집합
n, m = map(int, input().split())
str_set = set()
cnt = 0

for _ in range(n):
    str = input()
    str_set.add(str)

for _ in range(m):
    test_str = input()
    if test_str in str_set:
        cnt += 1
print(cnt)