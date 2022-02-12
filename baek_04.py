#1
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)

#2
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

#3
N = n = int(input())
i = 0
while True:
    N = ((N//10) + (N%10))%10 + ((N%10)*10)
    i += 1
    if N == n:
        break
print(i)