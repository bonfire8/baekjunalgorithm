T= int(input())
for tc in range(T):
    K = int(input())
    lst = list(map(int, input().split()))
    D = [[0]*(K+1) for _ in range(K+1)]

    for i in range(K-1):
        D[i][i+1] = lst[i] + lst[i+1]
