x = float(input("x"))
y = float(input("y"))


print(" ")

print("""  +      -      *     **""")
print(" ")
print(x+y, " ",x-y, " ",x*y, " ", x**y)

print(" ")

if y != 0:
    print("""/     //     %""")
    print(x/y, " ",x//y, " ", x%y)
    
if y == 0:
    print("não da pra dividi por zero lerdão")
    

