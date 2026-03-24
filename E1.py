m = [[1,2,3],
    [4,5,6],
    [7,8,9],
    [7,8,9],
]

for i in list(range(len(m))):
    print(m[i])
    
for n in list(range(len(m))):  # n in 0 a 3
    for e in list(range(len(m[n]))): # e in 
        print(m[n][e])

print(" ")

o=[]
l = []

for c in range(4):
    o.append(0)   
for p in range(4):
    l.append(o)

print(l)

print(" ")

a1=[]
a2=[]

for i in range(3):
    a1.append(len(a1))

print(a1)

for ie in range(3):
    a2.append(a1[]+len(a2))

print(a2)

print(" ")