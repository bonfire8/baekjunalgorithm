N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for n in range(N):
    # 2부터 해당 숫자까지 나눠본다
    for i in range(2, nums[n]+1):
        #나머지가 0일때(딱 떨어질때)
        if nums[n]%i == 0:
            #나누는 수가 해당 숫자와 같으면 소수이다.
            if i == nums[n]:
                cnt +=1
            #첫번째로 나머지가 0일때가 해당 숫자와 같아야 한다.
            break

print(cnt)