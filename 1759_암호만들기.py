
def dfs():

    if len(result) == L:
        cnt = cnt2= 0
        for i in range(L):
            #모음
            if result[i] in ahdma:
                cnt += 1
            #자음
            else:
                cnt2 += 1
        if cnt >= 1 and cnt2 >= 2:
            print(''.join(result))

    for i in range(C):
        if not used[i] and (len(result) == 0 or lst[i] > result[-1]):
            used[i] = True
            result.append(lst[i])
            dfs()
            used[i] = False
            result.pop()

L, C = map(int, input().split())
lst = sorted(list(map(str, input().split())))
used = [False] * C
result = []
result2 = []
ahdma = ['a', 'e', 'i', 'o', 'u']
dfs()
