a, b, c, = input().split()
a = int(a)
b = int(b)
c = int(c)

#제품 1개를 생산하는데 필요한 가변 비용이 판매가보다 크면 절대 이익이 발생할 수 없다.
if b >= c:
    result = -1
else:
    result = a/(c-b)+1

#정수형으로 출력한다.
print(int(result))
