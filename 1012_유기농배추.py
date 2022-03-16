#런타임 에러방지 재귀 최대깊이 정하기
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    #상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for d in range(4):
        newx = x + dx[d]
        newy = y + dy[d]
        # 배추를 만나면 이미 센 곳이기때문에 값을 바꿔준다.
        if 0 <= newx <N and 0 <= newy <M and arr[newx][newy] == 1:
            arr[newx][newy] = -1
            dfs(newx, newy)

T = int(input())
for tc in range(T):
    M,N,K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    #배추 심기
    for k in range(K):
        i, j = map(int, input().split())
        arr[j][i] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            #이미 지나간 곳은 -1로 바꿔줬기때문에 0보다 클때
            if arr[i][j] >0:
                dfs(i, j)
                #필요한 지렁이 숫자 더하기
                cnt += 1
    print(cnt)

