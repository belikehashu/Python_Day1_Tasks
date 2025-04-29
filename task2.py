a = input("Enter Long String: ")
b = a.split()
b = list(b)
b.reverse()
b = tuple(b)
space = " "
d = space.join(b)
print(d)
