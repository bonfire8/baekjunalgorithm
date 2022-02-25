arr = [[0]*100 for _ in range(100)]
for n in range(4):
    lec = list(map(int, input().split()))
    for i in range(lec[0],lec[2]):
        for j in range(lec[1],lec[3]):
            arr[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)