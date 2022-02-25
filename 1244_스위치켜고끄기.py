N = int(input())
switch = [-1] + list(map(int, input().split())) + [-2]
student = int(input())
for st in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, N+1, num):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1

    elif gender == 2:
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0
        for i in range(1, min(num, N-num)+1):
            if switch[num-i] != switch[num+i]:
                break
            else:
                if switch[num-i] == 1 and switch[num+i] == 1:
                    switch[num-i] = 0
                    switch[num+i] = 0
                elif switch[num-i] == 0 and switch[num+i] == 0:
                    switch[num-i] = 1
                    switch[num+i] = 1

i = 0
k = N
while k > 0:
    if k >= 20:
        print(" ".join(list(map(str, switch[20*i+1:20*(i+1)+1]))))
    else:
        print(" ".join(list(map(str, switch[20*i+1:N+1]))))
    i += 1
    k -= 20
