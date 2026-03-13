print("horas?")
x = int(input())
y = 10+(x-1)*5

print("Especial?")
P = input("S/N")


if x<1:
    print("grãtis")
if x >= 1 and x<=3:
    R = y
elif x>3:
    R = (y+(x-3)*8)

if P == "S":
    print(R-((R*15)/100))
else:
    print(R)