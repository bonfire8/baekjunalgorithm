M = int(input())
N = int(input())

cnt = []
for n in range(M, N+1):
    # 2부터 해당 숫자까지 나눠본다
    for i in range(2, N+1):
        #나머지가 0일때(딱 떨어질때)
        if n%i == 0:
            #나누는 수가 해당 숫자와 같으면 소수이다.
            if i == n:
                cnt.append(n)
            #첫번째로 나머지가 0일때가 해당 숫자와 같아야 한다.
            break

if len(cnt) != 0:
    print(sum(cnt))
    print(min(cnt))
else:
    print(-1)