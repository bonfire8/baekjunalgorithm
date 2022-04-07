
def dfs(cnt):
    global result, kg
    if cnt == N:
        result += 1

    for i in range(N):
        #사용하지 않았고 사용했을때 중량이 500이상이면
        if used[i] == False and kg - K + lst[i] >= 500:
            #사용했고
            used[i] = True
            #중량 변화
            kg = kg-K+lst[i]
            dfs(cnt+1)
            #원상복귀
            used[i] = False
            kg = kg+K-lst[i]

N, K = map(int, input().split())
lst = list(map(int, input().split()))
used = [False] * N
kg = 500
result = 0

dfs(0)
print(result)

