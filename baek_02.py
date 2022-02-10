#1
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')

#2
a = int(input())
if 90 <= a <= 100:
    print('A')
elif 80 <= a:
    print('B')
elif 70 <= a:
    print('C')
elif 60 <= a:
    print('D')
else:
    print('F')

#3
year = int(input())
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)

#4
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

#5
h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
elif h >= 1 and m < 45:
    print(h-1, m+15)
else:
    print(23, m+15)