import sys
input = sys.stdin.readline

#소수 구하기 함수
def isPrime(i):
    i = int(i)
    if i == 1:
        return False
    else:
        for j in range(2, int(i**(0.5))+1):
            if i%j == 0:
                return False
        return True

# 문제에서 123456안의 범위만 하라고 함
# 안하면 시간초과
Num_list = list(range(2, 246912))
result = []
for i in Num_list:
    if isPrime(i):
        result.append(i)

while True:
    N = int(input())
    cnt = 0
    #0이면 끝내기
    if N == 0:
        break
    # N부터 2N까지만 찾기
    for i in result:
        if N < i <= 2*N:
            cnt += 1
    print(cnt)