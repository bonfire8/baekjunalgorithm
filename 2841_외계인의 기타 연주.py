#시간초과
import sys
input = sys.stdin.readline

N, P = map(int, input().split())

st = [[] for _ in range(7)]

cnt = 0
for _ in range(N):
    n, p = map(int, input().split())
    #아무것도 없으면 추가
    if not st[n]:
        st[n].append(p)
        cnt += 1

    else:
        # 새로 칠 음표가 더 크면 스택 추가, 카운트 +1
        if st[n][-1] < p:
            st[n].append(p)
            cnt += 1
        # 같으면 넘어가기
        elif st[n][-1] == p:
            continue

         # st[n][-1] > p:
        else:
            # 새로 칠 음표가 작으면 기존 값이 새로칠 음표보다 작아질때까지 pop 하고 계속 카운트 +1
            while st[n] and p < st[n][-1]:
                st[n].pop()
                cnt += 1

            # 같으면 패스
            if st[n] and st[n][-1] == p:
                continue

            st[n].append(p)
            cnt += 1

print(cnt)
