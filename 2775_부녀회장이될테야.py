T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    # 0인 14층 14호의 행렬 생성
    arr = [[0] * 14 for _ in range(15)]

    #1호는 모두 1
    for i in range(15):
        arr[i][0] = 1
    #0층은 각 숫자
    for j in range(14):
        arr[0][j] = j+1
    #해당 호의 명수는 앞 집과 아랫집의 명수를 더하면 된다.
    for i in range(1, 15):
        for j in range(1, 14):
            arr[i][j] = arr[i][j-1] + arr[i-1][j]

    print(arr[k][n-1])