import sys
input = sys.stdin.readline

N, C = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()
s = 1
e = lst[-1]-1
ans = 0

while s <= e:
    mid = (s+e)//2
    now = lst[0] #현재 위치
    cnt = 1  #공유기 갯수
    for i in range(1, N):
        if lst[i] >= now + mid:
            cnt += 1
            now = lst[i]

    if cnt >= C:
        s = mid + 1
    else:
        e = mid -1

print(e)