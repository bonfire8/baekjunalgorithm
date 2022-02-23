a = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(croatia)):
    a = a.replace(croatia[i], '1')

print(len(a))
