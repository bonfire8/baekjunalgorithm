A, B = map(int, input().split())
C = int(input())

if B+C > 59:
    #분
    D = (B+C)%60
    #시간
    A += (B+C)//60
    #23시 지나면 0시로 초기화
    if A > 23:
        A = A-24
else:
    D = B+C

print(A, D)