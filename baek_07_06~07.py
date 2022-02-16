#1
lst = list(input().split())
print(len(lst))

#2
nums = list(map(str, input().split()))

new = []
for i in range(len(nums)):
    result = ''
    for j in range(len(nums[i])-1, -1, -1):
        result = result + nums[i][j]
    new.append(int(result))

maxV = 0
for i in range(len(new)):
    if maxV < new[i]:
        maxV = new[i]
print(maxV)