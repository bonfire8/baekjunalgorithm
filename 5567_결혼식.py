from collections import deque

def bfs(x):
    cnt = 0
    visited = [False for _ in range(N+1)]
    visited[x] = True
    q = deque()
    q.append((x, 0))

    while q:
        a, b = q.popleft()
        #2명까지 초대가능
        if b <= 2:
            cnt += 1
        for i in G[a]:
            if not visited[i]:
                visited[i] = True
                q.append((i, b+1))
    return cnt-1

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

print(bfs(1))