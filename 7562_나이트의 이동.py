
from collections import deque

def bfs(x, y):
    global nextC

    #8방향
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    deq.append((x, y))
    #시작 1
    arr[x][y] = 1

    while deq:
        x, y = deq.popleft()
        if x == nextC[0] and y == nextC[1]:
            #이미 밟은칸이므로 -1
            return arr[x][y]-1
        for d in range(8):
            newx = x + dx[d]
            newy = y + dy[d]
            #안밟았으면 지나가기
            if 0 <= newx < l and 0 <= newy < l and arr[newx][newy] == 0:
                deq.append((newx, newy))
                arr[newx][newy] = arr[x][y] + 1

T = int(input())

for tc in range(T):
    l = int(input())
    arr = [[0]*(l) for _ in range(l)]
    curC = list(map(int, input().split())) #현재 있는 칸
    nextC = list(map(int, input().split())) #이동하려고 하는 칸
    deq = deque()

    print(bfs(curC[0], curC[1]))
