import math

#Ex1
r2:float = float(input("Introdueix el r2 del cercle: "))
area:float = (r2 * r2) * math.pi
print(f"resultat = {area}")

#Ex2
n1:int = int(input("Introdueix un numero: ")) 
n2:int = int(input("Introdueix un altre numero: "))
print(f"El resultat és: {n1 + n2}")

#Ex3
preu:float = float(input("Introdueix el preu: "))
descompte = preu * 20 / 100
print(f"El preu total és de {preu - descompte}")

#Ex4 
imp:float = float(input("Introdueix un import: "))
desc:float = float(input("Introdueix el descompte a aplicar: "))

desc = imp * desc / 100
total = imp - desc
print(total)

#Ex5
nom:str = input("Introdueix el teu nom: ")
print(f"Hola {nom}")

#Ex6
nota1:float = float(input("Introdueix nota: "))
nota2:float = float(input("Introdueix nota: "))
nota3:float = float(input("Introdueix nota: "))
print(f"mitjana: {(nota1 + nota2 + nota3) / 3}")

#Ex7
edat = int(input("Introdueix la teva edat: "))
dies = edat * 365
segons = edat * 31622400
print(f"Has viscut {dies} dies / {segons} segons.")

#Ex8
var1 = input("algo")
var2 = input("algo")

aux = var1
var1 = var2
var2 = aux
print(f"{var1}, {var2}")

#Ex9
varA = input("algo")
varB = input("algo")
varC = input("algo")

aux = varB
varB = varA
varA = varC
varC = aux
print(f"{varA}, {varB}, {varC}")

#Ex10
