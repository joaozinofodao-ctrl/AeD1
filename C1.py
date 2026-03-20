print('\033[44m Atividade 01 \033[0m')

dada_a_lista = [3,7,10,15,22,30]
print(dada_a_lista)

for i in dada_a_lista:
    if i > 10:
        print(i)

################################
print(" ")
################################
print('\033[44m Atividade 02 \033[0m')

x = [5,8,12,20]
coco = 0

for i in x:
    coco += i

print(coco)

################################
print(" ")
################################
print('\033[44m Atividade 03 \033[0m')

y = range(1,8)
par = 0

for i in y:
    if i%2 == 0:
        par += 1

print(par)

################################
print(" ")
################################
print('\033[44m Atividade 04 \033[0m')

z = [1,2,2,3,3,3,4,5]
dict = {}

for i in z:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)

#cod original era outro cheio de var(feito do jeito mais burro possivel)
#esse aq ja usa as funções do dicionario ficando bem mais simples

################################
print(" ")
################################
print('\033[44m Atividade 05 \033[0m')

calores = [10,25,7,99,3]
ip = 0

for i in calores:
    if i > ip:
        ip = i

print(ip)

################################
print(" ")
################################
print('\033[44m Atividade 06 \033[0m')

ys8 = list(range(1,51))
aiai = []

for i in ys8:
    if i%2 == 0 and i%5 == 0:
        aiai.append(i)

print(aiai)


