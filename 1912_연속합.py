N = int(input())

lst = list(map(int, input().split()))
#연속합 저장할 리스트 생성
D = [0] * N
D[0] = lst[0]

for i in range(1, N):
    #최댓값을 원하므로 lst[i]와 이전까지 합 중에 더 큰 것을 저장
    D[i] = max(lst[i], D[i-1]+lst[i])

#최대값 출력
print(max(D))

