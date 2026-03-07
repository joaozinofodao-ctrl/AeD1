x = float(input("x"))
y = float(input("y"))

OP = input("op")

if OP == "+":
    print(x+y)
    
if OP == "-":
    print(x-y)
    
if OP == "*":
    print(x*y) 
    
if OP == "/" and y != 0:
    print(x/y)
else:
    print("aiaiui")
    
