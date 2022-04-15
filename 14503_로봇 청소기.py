N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[r][c] = 1
cnt = 1
#회전 횟수
cnt2 = 0
#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    #왼쪽 이동
    d -= 1
    if d == -1:
        d = 3
    #왼쪽 이동한 좌표
    newx = r + dx[d]
    newy = c + dy[d]
    #청소 안 했고 방문한 적 없으면
    if lst[newx][newy] == 0 and visited[newx][newy] == 0:
        visited[newx][newy] = 1
        cnt += 1
        r = newx
        c = newy
        cnt2 = 0 #회전 횟수 초기화
        continue
    else:
        cnt2 += 1

    #회전 횟수 4번
    if cnt2 == 4:
        #청소 안 한 곳이면 청소하기
        if lst[r-dx[d]][c-dy[d]] == 0:
            r = r - dx[d]
            c = c - dy[d]
        else:
            #종료
            break
        cnt2 = 0
print(cnt)