x = [1, 2, 3, 3, 5, 6]
x = set(x)
print(x)

x.add(2)
x.remove(6)
print(x)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)
print(s1 & s2)
print(s2 - s1)
