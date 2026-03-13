x = int(input())

a = x%2
b = x%3
c = x%5
d = x%7

print(x)
print(a)
print(b)
print(c)
print(d)

if x == 1 :
    print("not")
elif x == 2 or x == 3 or x == 5 or x == 7:
    print("yep")
elif a > 0 and b > 0 and c > 0 and d > 0:
    print("prime")
else:
    print("nad ave zé")