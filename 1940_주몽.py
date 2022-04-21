N = int(input())
M = int(input())
lst = list(map(int, input().split()))
#정렬된 리스트의 첫번쨰 값과 마지막 값에서 한 칸씩 가운데로 이동
lst.sort()
cnt = 0
s = 0 #시작
e = N-1 #끝
while s < e:
    #갑옷을 만들 수 있으면 한칸씩 앞, 뒤로 이동
    if lst[s]+lst[e] == M:
        cnt += 1
        s += 1
        e -= 1
    #값이 더 크다면 끝 값(큰 값)을 줄여줌
    elif lst[s]+lst[e] > M:
        e -= 1
    #값이 더 작다면 시작 값(작은 값)을 키워줌
    elif lst[s]+lst[e] < M:
        s += 1

print(cnt)