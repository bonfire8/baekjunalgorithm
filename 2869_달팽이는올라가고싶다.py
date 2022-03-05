import math

A, B, V = map(int, input().split())

# 나무 막대의 정상에 올라가면 미끄러지지 않아도 된다.
# 그러므로 마지막 날의 A미터는 무조건 정상에 도달하므로 전체 높이를 V-A로 하고 +1을 했다.
# 전체 높이 V-A를 A-B로 나눠주고 1.5일인 경우는 2일이 걸린 것이므로 올림을 헀다.
result = math.ceil((V-A) / (A-B)) + 1
print(result)
