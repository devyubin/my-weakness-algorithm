# 회사에 있는 사람
import sys
n = int(input())
compLog = {}
for _ in range(n):
    name, log = map(str, sys.stdin.readline().strip().split())
    compLog[name] = log

sorted_dict = {k: compLog[k] for k in sorted(compLog.keys(), reverse=True)}

for n, l in sorted_dict.items():
    if l == "enter":
        print(n)