import sys
input = sys.stdin.readline
M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    # 전체를 돌면서 다 검사했더니 시간초과가 났다.
    # 소수를 알아볼때 해당 수의 제곱근까지만 봐도 된다.
    for j in range(2, int(i**(0.5))+1):
        # 나눠서 처음으로 나머지가 0이 나오는 숫자가 소수이다.
        if i%j == 0:
            break
    # 멈추고 그 수를 출력
    else:
        print(i)
