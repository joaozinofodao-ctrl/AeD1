cty = [
    [1, 0, 2, 0, 1],  
    [0, 9, 2, 1, 3],  
    [1, 0, 1, 9, 2],  
    [9, 3, 0, 2, 1],  
    [0, 1, 2, 0, 9] 
]

cs = 0
hos = 0
ger = 0
ard = 0
nd = 0

tmg = 0
tmi = 0
tmh = 0 # temporari pra hosp
tmp = 0 # pra ve o nmb anterior
hp = 0 # hospital em prerigo

for i in list(range(len(cty))):
    if tmi == 5:
        tmh = 0
        tmg = 0
        tmi = 0
    for n in list(range(len(cty[i]))):
        if cty[i][n]== 1:
            cs+=1
        if cty[i][n] == 2:
            tmh==1
            hos+=1
            if n>=0 and n<=len(cty[i]):
                if cty[i][n-1]==9 or cty[i][n+1]==9:
                    hp+=1
                elif i<(len(cty)-1):
                    if cty[i-1][n]==9 or cty[i+1][n]==9:
                        hp+=1
                elif i==(len(cty)-1):
                    if cty[i-1][n]==9:
                        hp+=1
        if cty[i][n] == 3:
            tmg==1
            ger+=1
            print(f"linha {i+1} com energia")
        if cty[i][n] == 9:
            ard+=1
        else:
            nd+=1
        if tmp<hp:
            print(f"Hospital em {i+1,n+1} em perigo")
        tmp = hp
    tmi+=1
    if tmh==1 and tmg==1:
        print(f"Hospital linha {i+1} com energia")

print(" ")
print(f"Casas: {cs}  |  Hospitais: {hos}  |  Geradores: {ger}  |  Áreas destruídas: {ard}")

# if len(cty)>i>0 and len(cty[i])>n>0 and cty[i][n-1]==9 or cty[i][n+1]==9 or cty[i-1][n]==9 or cty[i+1][n]==9:
#        else:
#            print(f"Hospital em {i+1,n+1} seguro")