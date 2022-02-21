lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
eng = list(input())

sum = 0
for i in range(len(lst)):
    for j in eng:
        if j in lst[i]:
            sum += i+3
print(sum)