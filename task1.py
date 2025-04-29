a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = int(input('Enter a Num: '))
b = []
e = []
for j in a:
    if j<c:
        e.append(j)
print(f'Actual List: {a}')
for i in a:
    if i<5:
        b.append(i)
print(f'less then 5 : {b}')
print(f'less then user input: {e}')
