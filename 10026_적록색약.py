#런타임 에러방지 재귀 최대깊이 정하기
import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    #지나간 자리니까 True로 바꿔주기
    visited[x][y] = True
    #현재색깔 지정
    color = arr[x][y]

    for d in range(4):
        newx = x + dx[d]
        newy = y + dy[d]

        if 0 <= newx < N and 0 <= newy < N:
            if visited[newx][newy] == False:
                #색깔이 같으면
                if arr[newx][newy] == color:
                    dfs(newx, newy)


N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        #지나간 곳이 아닐때
        if visited[i][j] == False:
            dfs(i, j)
            #구간 더하기
            cnt += 1

#적록생맹
visited = [[False]*N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        #빨간색을 초록색으로 바꿔주기
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(N):
    for j in range(N):
        #지나간 곳이 아닐때
        if visited[i][j] == False:
            dfs(i, j)
            #구간 더하기
            cnt2 += 1

print(cnt, cnt2)
