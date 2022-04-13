
A = []
B = []
#x, y좌표끼리 따로 분류
for i in range(3):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

#2개가 같은 값이라면 나머지 하나의 값이 필요한 값
if A[0] == A[1]:
    resultA = A[2]
elif A[1] == A[2]:
    resultA = A[0]
elif A[2] == A[0]:
    resultA = A[1]

if B[0] == B[1]:
    resultB = B[2]
elif B[1] == B[2]:
    resultB = B[0]
elif B[2] == B[0]:
    resultB = B[1]

print(resultA, resultB)