
def hanoi(n, s, e):
    if n == 1:
        print(s, e)
        return
    # 6 = 1+2+3(전체)
    hanoi(n-1, s, 6-s-e)
    print(s,e)
    hanoi(n-1, 6-s-e, e)

N = int(input())
#옮긴 횟수
print(2**N-1)
hanoi(N, 1, 3)