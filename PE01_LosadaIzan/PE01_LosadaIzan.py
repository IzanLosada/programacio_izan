nom:str = input("Introdueix el teu nom: ") #String per introduïr nom
cognom:str = input("Introdueix el teu cognom: ") #String per introduïr cognom
data:str = input("Introdueix el teu aniversari. DD/MM: ") #Int per introduïr la data de naixement
any_naixement:int = int(input("Introdueix l'any de naixement: "))
ciutat:str = input("Introdueix la teva ciutat: ")
codi:int = int(input("Introdueix el teu codi postal: "))
usuari:str = input("Introdueix el teu nom d'usuari: ")
contrasenya:str = input("Introdueix la teva contrasenya: ")
estudiant:bool = input("Introdueix si ets estudiant. Si/No: ") == "Si" #Bool que en cas de ser Si passa a true
print("Dades introduïdes correctament.")

#Inici de sessió
inici_nom:bool = input("Introdueix el teu usuari: ") == usuari #Comprovem si l'usuari i contrasenya coincideixen amb els introduïts anteriorment
inici_contrasenya:bool = input("Introdueix la contrasenya: ") == contrasenya
validacio:bool = inici_contrasenya and inici_nom #Booleà per si han coincidit amb l'usuari i contrasenya anteriors

edat:int = (2025 - any_naixement) #Calculem l'edat
major:bool = edat >= 18 #En cas que l'edat sigui major o igual a 18 major serà true
 
#Mostrem les dades
print(validacio)
print(f"Nom complet: {nom} {cognom}")
print(f"Edat: {edat}")
print(f"Major d'edat: {major}")
print(f"Estudiant: {estudiant}")