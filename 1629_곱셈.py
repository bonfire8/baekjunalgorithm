#곱셉 개수 줄이기
def rhq(a, b):
    if b == 1:
        return a % C
    #분배법칙
    #(A*B)%C = (A%C)*(B%C)%C
    else:
        ans = rhq(a, b//2)
        #짝수인 경우
        if b % 2 == 0:
            return ans * ans % C
        #홀수인 경우
        else:
            return ans * ans * a % C

A, B, C = map(int, input().split())

print(rhq(A, B))