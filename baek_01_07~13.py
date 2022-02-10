#7
a, b = map(int, input().split())
c = a * b
print(c)

#8
a, b = map(int, input().split())
c = a / b
print(c)

#9
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#10
name = input()
print(f'{name}??!')

#18018
bkyear = int(input())
year = bkyear-543
print(year)

#10430
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#2588
a = int(input())
b, c, d = map(int, input())
e = 100*b + 10*c + d
print(a*d)
print(a*c)
print(a*b)
print(a*e)