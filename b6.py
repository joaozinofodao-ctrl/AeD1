print(f"\033[33;40m 51. Leia idades até que seja digitada uma idade negativa. Ao final, mostre a média das idades válidas. \033[0m")
print(" ")
idd=0
s=0
l=0
while idd>=0:
    try:
        idd=int(input("idade"))
    except:
        continue
    if idd<0:
        break
    s+=idd
    l+=1

if l!=0:
    print(s/l)

print(f"\033[33;40m 52. Leia 10 números inteiros e determine o maior e o menor valor lido. \033[0m")
print(" ")

lis=list(range(1,85,8))
for i in lis:
    print(i)
print(" ")
print(f"maior numero = {max(lis)} e o menor numero = {min(lis)}")

print(f"\033[33;40m 53. Leia um número inteiro n e informe se ele é primo. \033[0m")
print(" ")

def prima(x):
    a = x%2
    b = x%3
    c = x%5
    d = x%7

    if x == 1 :
        print("not")
    elif x == 2 or x == 3 or x == 5 or x == 7:
        print("prime")
    elif a > 0 and b > 0 and c > 0 and d > 0:
        print("prime")
    else:
        print("nad ave zé")

primo=int(input("numero pra ver se é primo"))
prima(primo)

print(f"\033[33;40m 54. Exiba todos os números primos de 1 até 100. \033[0m")
print(" ")

for i in list(range(101)):
    print(i)
    prima(i)

print(f"\033[33;40m 55. Leia um número inteiro positivo e calcule a soma de seus divisores. \033[0m")
print(" ")

PInTO=0
pinto = 75
print(pinto)
for p in list(range(1,pinto+1)):
    if pinto%p==0:
        PInTO+=p
        print(p)

print(PInTO)

print(f"\033[33;40m 56. Leia um valor inteiro e inverta seus dígitos sem usar strings. \033[0m")
print(" ")

numbero = 87
y=numbero//10
cen=y//10
if cen==0:
    cen=""
dez=y%10
if dez==0:
    dez=""
uni=numbero%10
print(numbero)
print(cen,dez,uni)
print(uni,dez,cen)

print(f"\033[33;40m 57. Simule um sistema de login que permita até 3 tentativas para acertar uma senha cadastrada. \033[0m")
print(" ")

nombre= input("tu nombre")
senh = input("su sennia")
tntv = 1

while tntv<=3:
    sna=input("digite sennia")
    if sna ==senh:
        print("Bravo!")
        break
    else:
        print("muito burro kkk")
        tntv+=1

if tntv>=3:
    print("blocked >:(")

print(f"\033[33;40m 58. Leia vários números até o usuário decidir encerrar. Mostre a média apenas dos números pares digitados. \033[0m")
print(" ")

qrfcr=0
somama=0
while qrfcr!= "n":
    trespratos=input("numbre")
    if trespratos%2==0:
        somama=+trespratos
    qrfcr=input("Digite 'N' para sair").lower()

print(f"\033[33;40m 59. Faça um programa que descubra se um número é perfeito, isto é, igual à soma de seus divisores próprios. \033[0m")
print(" ")

print(f"\033[33;40m 60. Leia um número inteiro e converta-o para binário usando divisões sucessivas. \033[0m")
print(" ")