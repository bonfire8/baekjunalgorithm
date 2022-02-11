#1
N = int(input())
for n in range(1, 10):
    ans = n * N
    print(f'{N} * {n} = {ans}')

#2
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    print(a+b)

#3
N = int(input())
sum = 0
for n in range(1, N+1):
    sum += n
print(sum)

#4
import sys

T = int(input())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

#5
N = int(input())
for n in range(1, N+1):
    print(n)

#6
N = int(input())
for n in range(N, 0, -1):
    print(n)

#7
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{tc}: {a+b}')

#8
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{tc}: {a} + {b} = {a+b}')

#9
N = int(input())
for n in range(1, N+1):
    print('*' * n)

#10
N = int(input())
for n in range(1, N+1):
    print(' ' * (N-n) + '*' * n)

#11
N, X = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(len(lst)):
    if lst[i] < X :
        print(lst[i], end=" ")