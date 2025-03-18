from mooduldef import *
#Простейшие арифметические операции 
a=float(input("sisesta arv 1: "))
b=float(input("sisesta arv 2: "))
t=input("tehe: ")
v= arithmetic(a,b,t)
print(v)

#Kas aasta on liigaasta
ast=int(input("sisesta aasta: "))
vas=is_year_leap(ast)
print(vas)
if vas:
    print(f"{ast} liigaasta")
else:
    print(f"{ast} ei ole liigaasta")

#Ruudu umbermoot, pindala ja diagonaal
k=float(input("sisesta ruudu kulg: "))
v=square(k)
print(v)

#aastaajad 
k=int(input("sisesta kuu number: "))
v=season(k)
print(v)