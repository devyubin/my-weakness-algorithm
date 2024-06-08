# 비밀번호 찾기
import sys
n, m = map(int, input().split())

linkDic = {}

for _ in range(n):
    site, pwd = map(str, sys.stdin.readline().strip().split())
    linkDic[site] = pwd

for _ in range(m):
    site = sys.stdin.readline().strip()
    print(linkDic[site])