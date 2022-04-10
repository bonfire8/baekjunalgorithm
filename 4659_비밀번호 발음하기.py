ahdma = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()
    if pw == 'end':
        break
    cnt = cnt2 = 0
    for i in pw:
        if i in ahdma:
            cnt2 += 1
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] not in ['e', 'o']:
            cnt += 1

    for i in range(len(pw)-2):
        if pw[i] in ahdma and pw[i+1] in ahdma and pw[i+2] in ahdma:
            cnt += 1
        elif pw[i] not in ahdma and pw[i+1] not in ahdma and pw[i+2] not in ahdma:
            cnt += 1

    if cnt == 1 or cnt2 == 0:
        print('<{}> is not acceptable.'.format(pw))
    else:
        print('<{}> is acceptable.'.format(pw))