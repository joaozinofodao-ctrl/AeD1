# Código ANSI
roxo_bg = "\033[45m"
verde_txt = "\033[32m"
reset = "\033[0m"

print(roxo_bg + verde_txt + "=" * 60 + reset)
print(roxo_bg + verde_txt + "LISTA DE EXERCÍCIOS".center(60) + reset)
print(roxo_bg + verde_txt + "=" * 60 + reset)

print()
print(roxo_bg + verde_txt + "71. Leia uma lista de números e faça uma rotação para a direita em uma posição." + reset + "\n")

lis=[]

for i in range(5):
    lis.append(int(input("numb pra lista")))

print(lis)

lisR=[]

for i in range(len(lis)):
    if i ==0:
        lisR.append(lis[len(lis)-1])
    else:
        lisR.append(lis[i-1])

print(lisR)

print(roxo_bg + verde_txt + "72. Leia uma lista de números e verifique se ela está ordenada em ordem crescente." + reset + "\n")

tempero_salsa=lis[0]-1
crescer=None
for i in range(len(lis)):
    if i == len(lis)-1:
        if tempero_salsa<lis[i]:
            crescer=True
    elif tempero_salsa<lis[i] and lis[i]<lis[i+1]:
        tempero_salsa=lis[i]
        crescer=True
    else:
        crescer=False
        break
    
print(f"É crescente?{crescer}")

print(roxo_bg + verde_txt + "73. Leia uma lista e encontre o segundo maior valor distinto." + reset + "\n")

temp = min(lis)
for i in lis:
    if i < max(lis) and i > temp:
        temp=i

print(temp)

print(roxo_bg + verde_txt + "74. Leia uma lista de inteiros e separe os elementos em duas listas, positivos e negativos." + reset + "\n")

n=[]
p=[]
for i in lis:
    if i > 0:
        p.append(i)
    elif i < 0:
        n.append(i)

print(n)
print(p)

print(roxo_bg + verde_txt + "75. Implemente uma busca linear que receba uma lista e um valor-alvo," + reset)
print(roxo_bg + verde_txt + "    retornando a posição do elemento ou -1 se não encontrado." + reset + "\n")

tem=None
alvo=int(input("digite valor alvo"))
for i in range(len(lis)):
    if lis[i]==alvo:
        print(f"alvo na posição {i+1}")
        tem=True

if tem == None:
    print("-1")

print(roxo_bg + verde_txt + "76. Leia duas listas e gere uma terceira contendo apenas os elementos em comum," + reset)
print(roxo_bg + verde_txt + "    sem repetição." + reset + "\n")

lis3=[]
lis2=[]
lis1=[]
for i in range(5):
    lis1.append(int(input("numb pra lista")))
    lis2.append(int(input("numb pra lista(1)")))

for i in lis1:
    if i in lis3:
        continue
    elif i in lis2:
        lis3.append(i)

print(lis3)

print(roxo_bg + verde_txt + "77. Dada uma lista de números, calcule a frequência de cada valor" + reset)
print(roxo_bg + verde_txt + "    sem usar bibliotecas prontas de contagem." + reset + "\n")

lisrepet=[]
for i in range(5):
    lisrepet.append(int(input("numb pra lista repet")))

contt={}
for i in lisrepet:
    if i in contt:
        contt[i]+=1
    else:
        contt[i]=1

print(contt )

print(roxo_bg + verde_txt + "78. Leia uma lista de números e gere outra com soma acumulada." + reset)
print(roxo_bg + verde_txt + "    Exemplo: [2, 5, 1] resulta em [2, 7, 8]." + reset)

buaa=0
lisalt=[]
for i in lis:
    buaa+=i
    lisalt.append(buaa)
    

print(lisalt)
print(roxo_bg + verde_txt + "=" * 60 + reset)