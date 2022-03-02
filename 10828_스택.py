import sys
N = int(input())
# 그냥 input()으로 받으면 시간이 초과된다
input = sys.stdin.readline
st = []

#push, top, size, empty, pop에 해당하는 코드를 작성한다
for n in range(N):
    a = input().split()
    
    if a[0] == 'push':
        #push 옆에 숫자 st에 넣기
        st.append(a[1])

    elif a[0] == 'top':
        #스택이 있다면
        if st:
            print(st[-1])
        else:
            print(-1)

    elif a[0] == 'size':
        print(len(st))

    elif a[0] == 'empty':
        #스택이 있다면
        if st:
            print(0)
        else:
            print(1)

    elif a[0] == 'pop':
        if st:
            print(st.pop())
        else:
            print(-1)
