# ======================= BLOCO 7 — VETORES =======================

print("\033[95m" + "="*70 + "\033[0m")
print("\033[95m" + " " * 25 + "BLOCO 7 — VETORES" + " " * 25 + "\033[0m")
print("\033[95m" + "="*70 + "\033[0m")
print()

print("\033[97m61. Leia 5 números inteiros e armazene em uma lista. Depois, exiba a lista completa.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 61 AQUI ←←←←←←←←←←

lis=[]

for i in range(5):
    lis.append(int(input("numb pra lista")))

print(lis)

print("\n\033[97m62. Leia 10 números e exiba a soma e a média dos elementos da lista.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 62 AQUI ←←←←←←←←←←

print("agr mais 5 pvf")
for i in range(5):
    lis.append(int(input("numb pra lista")))

print(sum(lis),sum(lis)/len(lis))

print("\n\033[97m63. Leia 8 números e informe o maior valor e sua posição na lista.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 63 AQUI ←←←←←←←←←←

for i in range(2):
    lis.pop(i)
for i in range(len(lis)):
    if lis[i]==max(lis):
        po=i
print(lis)
print(f"maior numero é {max(lis)} e sua posição é {po+1}")


print("\n\033[97m64. Leia 10 números inteiros e crie uma nova lista apenas com os valores pares.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 64 AQUI ←←←←←←←←←←

lisP=[]
for i in lis:
    if i%2 ==0:
        lisP.append(i)
print(lisP)
        

print("\n\033[97m65. Leia uma lista com 6 nomes e exiba em ordem alfabética.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 65 AQUI ←←←←←←←←←←

lisnn=[]
for i in range(6):
    tempero=input("nome pra lista")
    lisnn.append(tempero)
lisnn.sort()
print(lisnn)



print("\n\033[97m66. Leia 10 números e conte quantas vezes um determinado valor aparece na lista.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 66 AQUI ←←←←←←←←←←

for i in range(2):
    lis.append(input("number pls"))

liscont={}
for i in lis:
    if i in liscont:
        liscont[i]+=1
    else:
        liscont[i]=1
print(liscont)


print("\n\033[97m67. Leia 7 números e crie uma segunda lista com os quadrados dos elementos da primeira.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 67 AQUI ←←←←←←←←←←

aaaaaaa=[]
aaaaaaatothesquare=[]
for i in range(7):
    farofa=int(input("numb pra lista"))
    aaaaaaa.append(farofa)
    aaaaaaatothesquare.append(farofa**2)
print(aaaaaaa)
print(aaaaaaatothesquare)

print("\n\033[97m68. Leia duas listas de 5 posições e gere uma terceira lista com a soma dos elementos de mesmo índice.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 68 AQUI ←←←←←←←←←←

essacadeiradoidemais=[]
naoaguentomaisfazelista=[]
chucrutecomazeitona=[]

for i in range(5):
    alface=int(input("numb pra lista 1"))
    tomate=int(input("numb pra lista 2"))
    essacadeiradoidemais.append(alface)
    naoaguentomaisfazelista.append(tomate)

    ketchup=alface+tomate
    chucrutecomazeitona.append(ketchup)
    
print(essacadeiradoidemais)
print(naoaguentomaisfazelista)
print(chucrutecomazeitona)

print("\n\033[97m69. Leia uma lista de 10 números e remova os valores repetidos, mantendo apenas a primeira ocorrência.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 69 AQUI ←←←←←←←←←←

arteria_entupida=[]
for i in lis:
    if i in arteria_entupida:
        continue
    else:
        arteria_entupida.append(i)

print("\n\033[97m70. Leia uma lista de notas de alunos e informe quantos ficaram acima da média da turma.\033[0m")
print("\033[95m" + "-"*70 + "\033[0m")
# ←←←←←←←←←← PROGRAME O EXERCÍCIO 70 AQUI ←←←←←←←←←←

BondeDosPescocudo={}
for i in range(6):
    hipercalorico=int(input("adicione uma nota de aluno"))
    if hipercalorico > 70:
        insulina = "Aprovado"
    else:
        insulina = "Reprovado"
    BondeDosPescocudo[hipercalorico]=insulina

print(BondeDosPescocudo)


print("\n\033[95m" + "="*70 + "\033[0m")
print("\033[95m" + "     FIM DO BLOCO 7 — VETORES     ".center(70) + "\033[0m")
print("\033[95m" + "="*70 + "\033[0m")