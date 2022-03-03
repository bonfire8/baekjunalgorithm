N = int(input())
# 1-7 1개 6
# 8-19 2개 12
# 20-37 3개 18
# 38-61 4개 24
cnt = 1  # 1을 넣었을때 1이 출력돼야 하므로 기본값 1
room = 6 # 육각형
result = 1 #6, 12, 18, 24 ...

#N이 방번호보다 클 때, 작으면 실행 멈춤
while N > result:
    result += room
    room += 6
    cnt += 1
print(cnt)