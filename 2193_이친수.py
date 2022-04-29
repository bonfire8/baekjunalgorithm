import sys
imput = sys.stdin.readline

N= int(input())
D = [1, 1]

  #           1          1: 1개
  #          /
  #          0           2: 1개
  #        /  \
  #       1    0         3 : 2개
  #      /     /\
  #     0     1  0       4 : 3개
  #    / \   /  / \
  #   1  0   0  0  1     5 : 5개
  #  /  /\   /\ /\  \
  # 0  1 0  1 0 1 0  0   6 : 8개

    #D[i]의 합은 이전 2개의 합

for i in range(2, 90):
    D.append(D[i-1] + D[i-2])

print(D[N-1])