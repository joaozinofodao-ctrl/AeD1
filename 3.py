print("insira 3 notas")

x = int(input())
y = int(input())
z = int(input())

M = (x+y+z)/3

if M >= 70:
    print("aprovado!!!")
elif M > 40:
    print("vai faze o exame caba")
else:
    print("reprovado >:(")

print(M)