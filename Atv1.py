#user insere n percorrer 0 a n somar os num contidos 0 a n percorrer o print e result da soma

N = int(input("N"))
x = range(0,N+1)
S = int(sum(x))
y = range(0,S+1)

for i in x:
    print(i)

print("")

for i in y:
    print(i)

print("soma =",S)
