N = int(input())
lst = list(map(int, input().split()))
M = int(input())
minV = 0
maxV = max(lst)

#이분탐색
while minV <= maxV:
    #중간값
    mid = (minV+maxV)//2
    ans = 0

    for i in lst:
        if i <= mid:
            ans += i
        else:
            ans += mid
    if ans > M:
        maxV = mid - 1
    else:
        minV = mid + 1
print(maxV)
