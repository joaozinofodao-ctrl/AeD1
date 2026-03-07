print("wins?")
W = int(input())
print("loses?")
L = int(input())

games = W + L 

WR = (W*100)/games
print("winRate:" + str(WR))
print("total gaimes" + str(games))

#espaço uiuui
print(" ")

#pergunta meio fodase/ dá pra joga fora
print("is that correct?")
certo = input()

if certo == "s":
    print("fodase?")
    
if certo != "s":
    print("olokinho meu")