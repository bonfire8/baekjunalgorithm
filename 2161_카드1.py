N = int(input())
st =[]
st2 = []
for n in range(1, N+1):
    st.append(n)

while len(st) > 1:
    #새로운 스택에 맨 앞 스택 추가
    st2.append(st.pop(0))
    # 맨 앞 스택 다시 맨 뒤로 추가
    st.append(st.pop(0))

# 하나 남은거 맨뒤에 추가
if len(st) == 1:
    st2.append(*st)

print(*st2, end=' ')