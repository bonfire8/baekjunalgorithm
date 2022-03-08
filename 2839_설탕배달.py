N = int(input())
cnt = 0
#N이 0이 될때까지
while N != 0:
    #봉지의 최솟값을 찾아야하므로 5kg의 봉지가 많아야 최소가 된다고 생각하여 5를 기준으로 했다.
    #5의 배수가 아니라면 3kg봉지를 하나 추가해줬으니 3kg를 빼준다.
    if N % 5 != 0:
        N -= 3
        #나머지가 존재하면(1, 2kg가 남으면)
        if 0< N < 3:
            cnt = -1
            break
        cnt += 1
    #5의 배수이면 5로 나눈 몫이 답이다.
    else:
        cnt += N//5
        break
print(cnt)