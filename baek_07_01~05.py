#1
print(ord(input()))

#2
N = int(input())
lst = list(map(str, input()))

sum = 0
for n in range(N):
    sum += int(lst[n])
print(sum)

#3
word = list(map(str, input()))
lst = [-1] * 26

for i in range(len(word)):
    if lst[ord(word[i])-97] == -1:
        lst[ord(word[i])-97] = i

for j in lst:
    print(j, end=" ")

#4
T = int(input())
for tc in range(T):
    R, S = input().split()
    result = ""
    for i in S:
        result += int(R) * i
    print(result)

#5
word = input().upper()
word_set = list(set(word))
result = []

for w in word_set:
    cnt = word.count(w)
    result.append(cnt)

if result.count(max(result)) >= 2:
    print('?')

else:
    print(word_set[result.index(max(result))])

