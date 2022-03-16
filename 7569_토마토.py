import sys
input = sys.stdin.readline
#deque 안썼더니 시간초과
from collections import deque

#너비 우선 탐색
def bfs():
    while st:
        z, x, y = st.popleft()

        for i in range(6):
            newx = x + dx[i]
            newy = y + dy[i]
            newz = z + dz[i]

            if 0 <= newx < N and 0<= newy <M and 0<= newz <H and arr[newz][newx][newy] == 0:
                #이미 익은 토마토 주위를 찾는 것이므로 익은 토마토 주위에 안익은 토마토가 있으면 그 토마토를 익게 해준다.
                #하루 추가
                arr[newz][newx][newy] = arr[z][x][y]+1
                #하루가 지나면 토마토가 익으니까 스택에 추가한다.
                st.append([newz, newx, newy])

M, N, H = map(int, input().split())
#3차원배열만들기
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

#상하좌우 위아래
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

st = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            # 익은 토마토, 스택에 추가
            if arr[h][n][m] == 1:
                st.append([h, n, m])

bfs()
#최대 날짜 찾기
z = 1
result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            #토마토가 안익었을때
            if arr[h][n][m] == 0:
                z = 0
            result = max(result, arr[h][n][m])

#모두 안 익은 상태
if z == 0:
    print(-1)
#모두 익어있던 상태였으면 1-1=0을 출력하게 되고 모두 익으면 result-1을 출력한다.
else:
    print(result-1)
