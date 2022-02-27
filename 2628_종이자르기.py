X, Y = input().split()
N = int(input())
row = []
col = []
#빈 리스트를 행, 열로 생성하고 a의 값이 0이라면 열의 리스트에 1이라면 행의 리스트에 추가했다.
for n in range(N):
    a, b = input().split()

    if a == '0':
        col.append(int(b))
    elif a == '1':
        row.append(int(b))

#범위의 처음과 끝 값을 주기 위해 append를 했다.
row.append(int(X))
row.append(0)
col.append(int(Y))
col.append(0)

#종이를 자르는 순간 다시 붙여지지 않으므로 정렬을 하여 간격을 볼 수 있게 sort함수를 이용했다.
row.sort()
col.sort()

#반복문을 이용하여 가로길이는 고정하고 세로길이에 따라 변하는 면적, 그다음에는 가로길이까지 변하는 면적을 구하고 최대값을 구하기 위해 초기 최대값을 0으로 설정해준뒤 max함수를 이용하여 최대값을 구했다.
maxV = 0
for i in range(1, len(row)):
    for j in range(1, len(col)):
        x = row[i] - row[i-1]
        y = col[j] - col[j-1]
        area = x*y
        maxV = max(maxV, x*y)

print(maxV)