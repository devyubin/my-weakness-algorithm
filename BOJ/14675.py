# 단절점과 단절선
n = int(input())

tree=[[] for _ in range(n+1) ]

for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = int(input())

for i in range(q):
    x, y = map(int, input().split())

    if x == 2:
        print("yes")
    else:
        if len(tree[y]) >= 2:
            print("yes")
        else:
            print("no")

