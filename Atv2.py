N = int(input("N"))
x = 0

for i in range(1,N+1):
    print(i)
    if i%2 == 0:
        x = x + 1

print(" ")
    
print("números pares:",x)