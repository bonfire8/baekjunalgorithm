def dfs():
    #백트래킹
    if len(lst) == M:
        #리스트 안에서 하나씩 꺼내서 출력
        print(' '.join(map(str, lst)))
        return

    for i in range(1, N+1):
        #중복 방지
        if i not in lst:
            lst.append(i)
            #재귀
            dfs()
            lst.pop()

N, M = map(int, input().split())
lst = []
dfs()