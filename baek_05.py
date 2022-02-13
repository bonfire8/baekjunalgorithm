#1
N = int(input())
num = list(map(int, input().split()))

max = -1000000
min = 1000000
for n in range(N):
    if max < num[n]:
        max = num[n]
    if min > num[n]:
        min = num[n]
print(min, max)

#2
N = []
for i in range(9):
    N.append(int(input()))

max = 0
for i in range(9):
    if max < N[i]:
        max = N[i]
        a = i + 1

print(max)
print(a)

#3
a = int(input())
b = int(input())
c = int(input())

total = list(str(a*b*c))

for n in range(10):
    print(total.count(str(n)))

#4
N = []
for i in range(10):
    N.append(int(input()))

a = []
for n in N:
    if n%42 in a:
        pass
    else:
        a.append(n%42)

print(len(a))

#5
tc = int(input())
score = list(map(int, input().split()))
max = 0
for t in range(tc):
    if max < score[t]:
        max = score[t]

sum = 0
for t in range(tc):
    sum += score[t]/max*100

avg = sum/tc
print(avg)

#6
T = int(input())
for tc in range(T):
    ox = list(input())
    result = 0
    score = 0
    for i in ox:
        if i == 'O':
            result += 1
            score += result
        else:
            result = 0
    print(score)

#7
T = int(input())
for tc in range(T):
    score = list(map(int, input().split()))
    num = score[0]
    sum = 0
    for n in range(1, num+1):
        sum += score[n]
    avg = sum/num

    a = 0
    for i in range(1, num+1):
        if avg < score[i]:
            a += 1
    result = a/num*100
    print(f'{result:.3f}%')