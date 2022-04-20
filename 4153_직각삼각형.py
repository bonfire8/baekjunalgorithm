
while True:
    lst = list(map(int, input().split()))

    #0이면 멈추기
    if sum(lst) == 0:
        break
    #최대값 찾아서 리스트에서 삭제
    maxV = max(lst)
    lst.remove(maxV)
    #피타고라스 정리
    if lst[0]**2 + lst[1]**2 == maxV*maxV:
        print('right')
    else:
        print('wrong')