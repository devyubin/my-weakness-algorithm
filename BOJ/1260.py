# DFS BFS
n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited1 = [0]*(n+1)
visited2 = visited1.copy()

def dfs(v):
    visited1[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(v):
    queue = [v]
    visited2[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if (visited2[i] == 0 and graph[v][i] == 1):
                queue.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)