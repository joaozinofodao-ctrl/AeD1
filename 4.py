print("numero pra sabe se é divisivel por 3 e 15 at the same time")
x = int(input())

y = x%3
z = x%15

print(y)
print(z)

if y == 0 and z == 0:
    print("acerto miseravi")
else:
    print("carai borracha mano")