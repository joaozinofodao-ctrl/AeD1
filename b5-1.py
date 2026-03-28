rosa_preto = "\033[1;35;40m"
reset = "\033[0m"

print(f"{rosa_preto}49.{reset}")
print(f"{rosa_preto}Leia números inteiros até que o usuário digite 0. Ao final, mostre{reset}")
print(f"{rosa_preto}a soma dos valores digitados, sem contar o zero.{reset}")

a=int(input("me da os numbers"))
s= 0

while a != 0:
    s+=a
    a= int(input("me da os numbers"))
    
print(s)

print("\n" + "-"*30 + "\n") # Separador

print(f"{rosa_preto}50.{reset}")
print(f"{rosa_preto}Simule um menu repetitivo de calculadora simples. O programa deve{reset}")
print(f"{rosa_preto}continuar executando até que o usuário escolha sair.{reset}")

ex="n"
while ex != "s":
    num1=int(input("numero 1 = "))
    op=input("operador = ")
    num2=int(input("numero 2 = "))
    E=f"{num1}{op}{num2}"
    r=eval(E)                   #eval executa uma string como se fosse uma linha de python
    print(r)
    ex=input("quer sair? s/n")

print(" ")
