#1
def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

a = list(map(int, input().split()))
print(solve(a))

#2
N = set(range(1, 10001))
remove = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove.add(i)

result = N - remove
for j in sorted(result):
    print(j)

#3
X = int(input())
cnt = 0
for i in range(1, X + 1):
    lst = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif lst[0] - lst[1] == lst[1] - lst[2]:
        cnt += 1
print(cnt)