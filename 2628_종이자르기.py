X, Y = input().split()
N = int(input())
row = []
col = []
for n in range(N):
    a, b = input().split()

    if a == '0':
        col.append(int(b))
    elif a == '1':
        row.append(int(b))

row.append(int(X))
row.append(0)
col.append(int(Y))
col.append(0)

row.sort()
col.sort()

maxV = 0
for i in range(1, len(row)):
    for j in range(1, len(col)):
        x = row[i] - row[i-1]
        y = col[j] - col[j-1]
        area = x*y
        maxV = max(maxV, x*y)

print(maxV)