x = [7.5, 8.0, 6.5, 9.0]
m = sum(x) / len(x)
if m > 7:
    print(m, "aprovado")
else:
    print(m, "not")

x.append(5.0)
print(x)

x.remove(6.5)
print(x)

x.sort()
print(x)

x.reverse()
print(x)
