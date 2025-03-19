from mooduldef import *


#lihtarvud
n=int(input("sisesta arv: "))
v=is_prime(n)
print(v)

#kuupaevad
kuu=int(input("sisesta kuu number: "))
paev=int(input("sisesta paev: "))
v=date(kuu, paev)
print(v)


#bank
a=int(input("sisesta raha: "))
years=int(input("sisesta aastad: "))
v=bank(a, years)
print(v)


#XOR krüpteerimine
text=input("sisesta tekst: ")
key=input("sisesta võti: ")
v=XOR_cipher(text, key)
print(v)


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
v= season(k)
print(v)    

