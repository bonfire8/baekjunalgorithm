N = int(input())
#층수-개수 (개수는 등차수열)
#1-1 / 2-3 / 3-6 / 4-10 / 5-15 ...

line = 1 #층수
total = 1 #개수
while N > total:
    line += 1
    total += line
index = total-N
#홀수(분모가 커짐, 분자가 작아짐)
if line % 2 != 0:
    result = str(index+1)+'/'+str(line-index)

#짝수(분자가 커짐, 분모가 작아짐)
else:
    result = str(line-index)+'/'+str(index+1)

print(result)