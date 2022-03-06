T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())
    #i는 배정될 층수 j는 호수
    #예시 6층 12호까지 있을때 10번째 손님은 4층 2호 이므로 층수가 나머지 호수가 몫이다.
    #호수는 1부터 있으니 +1
    i = N%H
    j = N//H+1
    #배정될 층수가 호텔 층수의 배수일 경우
    if i == 0:
        i = H
        j -=1
    result = i*100 +j
    print(result)