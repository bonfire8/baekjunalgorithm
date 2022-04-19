def goldbach():
    #0, 1은 소수가 아니니까 False
    check = [False, False] + [True] * 10000

    for i in range(2, 101):
        if  check[i] == True:
            #소수가 아니면 False
            for j in range(2*i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        #반으로 나눠서 찾기(차이가 가장 적은걸 찾아야하기 때문에 절반에서 출발)
        a = n//2
        b = a
        for _ in range(10000):
            #모두 True이면 출력
            if check[a] and check[b]:
                print(a, b)
                break
            #a는 앞으로 b는 뒤로 가기
            a -=1
            b += 1
goldbach()