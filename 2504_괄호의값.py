lst = list(input())
st = []
ans = 0 #결과 값
result = 1 #중간에 더할 값
for i in range(len(lst)):
    #여는 괄호면 스택에 추가
    if lst[i] == '[':
        st.append(lst[i])
        result *= 3

    elif lst[i] == '(':
        st.append(lst[i])
        result *= 2

    #닫는 괄호
    elif lst[i] == ')':
        #빈 스택이거나 짝이 안 맞으면 0
        if not st or st[-1] == '[':
            ans = 0
            break
        #짝이 맞으면 더하기
        if lst[i-1] == '(':
            ans += result
        #짝 맞았으니까 스택에서 빼기
        st.pop()
        result //=2

    elif lst[i] == ']':
        if not st or st[-1] == '(':
            ans = 0
            break
        if lst[i-1] == '[':
            ans += result
        st.pop()
        result //=3

#짝이 안 맞으면
if st:
    ans = 0

print(ans)