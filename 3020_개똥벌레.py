import sys
input = sys.stdin.readline

N, H = map(int, input().split())
high = [0] * (H+1) #종유석
low = [0] * (H+1)  #석순

#홀수, 짝수의 경우를 나누어 종유석, 석순 리스트에 추가
for i in range(N):
    if i%2 == 0:
        low[int(input())] += 1
    else:
        high[int(input())] += 1

#누적합
for i in range(H-1, 0, -1):
    low[i] += low[i+1]
    high[i] += high[i+1]

#최소값을 구하고 최소값과 같다면 cnt에 +1
minV = N
cnt = 0
for i in range(1, H+1):
    if minV > (low[i]+high[H-i+1]):
        minV = low[i]+high[H-i+1]
        cnt = 1
    elif minV == (low[i]+high[H-i+1]):
        cnt += 1
print(minV, cnt)