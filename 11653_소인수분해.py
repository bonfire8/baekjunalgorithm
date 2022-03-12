N = int(input())
cnt = []

# 소인수 구하기
for i in range(2, N+1):
    if N%i == 0:
        cnt.append(i)
i= 0
while N != 1:
    #소인수 분해가 되면 해당 인수로 계속 나눠준다.
    if N%cnt[i] == 0:
        print(cnt[i])
        N = N/cnt[i]
    #아니면 i+1을 해준다.(cnt에서 한칸 뒤로 이동)
    else:
        i += 1