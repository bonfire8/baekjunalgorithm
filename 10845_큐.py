import sys
input = sys.stdin.readline
N = int(input())
# 그냥 input()으로 받으면 시간이 초과된다
st = []

#push, size, empty, pop, front, back에 해당하는 코드를 작성한다
for n in range(N):
    a = input().split()

    if a[0] == 'push':
        # 0번째 자리에 push 옆 숫자 st에 넣기
        st.insert(0, a[1])

    elif a[0] == 'size':
        print(len(st))

    elif a[0] == 'empty':
        # 스택이 있다면
        if st:
            print(0)
        else:
            print(1)

    elif a[0] == 'pop':
        if st:
            print(st.pop())
        else:
            print(-1)

    #가장 처음에 추가된 요소를 뜻하므로 list의 맨 끝요소를 출력해야 한다
    elif a[0] == 'front':
        if st:
            print(st[len(st)-1])
        else:
            print(-1)

    #가장 마지막에 추가된 요소이므로 list의 0번째 요소를 출력한다.
    elif a[0] == 'back':
        if st:
            print(st[0])
        else:
            print(-1)
