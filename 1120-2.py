A, B = list(map(str, input().split()))
a = len(A)
b = len(B)

result = []

for i in range(b-a+1):
    cnt = 0
    for j in range(a):
        if A[j] != B[i+j]:
            cnt += 1
    result.append(cnt)
print(min(result))