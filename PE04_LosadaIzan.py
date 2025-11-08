import random

def aspersor(): # Funció per l'aspersor
    print("a) Modificar horaris d'ús / Aigua") # Mostrem a l'usuari les opcions i demanem que agafi una
    print("b) Suspensió/Apagar aspersors")
    asp = input("Que vols fer? ").lower()
    aigua:float = "" # Variabes per aigua i hora a executar-se
    hora:float = ""
    if asp == "a": 
        hora:float = float(input("Introdueix hora d'ús: ").replace(":", ".")) # Demanem hora d'activació i litres d'aigua
        aigua:float = float(input("Introdueix el nombre de litres d'aigua que vols utilitzar: ").replace(",", "."))
        print(f"Nova hora introduïda: {hora:.2f}.") # Mostrem dades escollides
        print(f"Nova quantitat d'aigua establerta: {aigua:.2f}L.")
    elif asp == "b":
        hora:float = "" # Buidem les dades desactivant així els aspersors
        aigua:float = ""
        print("Aspersors desactivats. (Hauràs de reconfigurar la hora per que tornin a activar-se)")
    else:
        print("Introdueix una de les opcions anteriors")

def calefaccio(a, b): # Funció per mostrar temperatures límit
    print(f"Configuració reconfigurada correctament: Nova temperatura mínima per activar la calefacció: {a}.")
    print(f"nova temperatura màxima per apagar-la: {b}.")

def menu_calefaccio():
    print("a) Ingresar temperatures límits") # Mostrem a l'usuari les opcions i demanem que agafi una
    print("b) Mostrar estat")
    print("c) sortir")
    opcio:str = input("Que vols fer: ").lower()
    on:float = 0 # Creem les variables per temperatures límits
    off:float = 0
    match(opcio):
        case "a": 
            try: # Demanem que configuri les temperatures limit i les mostrem amb la funció anterior
                on:float = float(input("Introdueix el número de graus mínim per activar la calefacció: ").replace(",", "."))
                off:float = float(input("Intrpdueix el número de graus per apagar la calefacció: ").replace(",", "."))
                calefaccio(on, off)
            except ValueError: # Error en cas que agafi un valor incorrecte
                print("Introdueix un valor vàlid")
        case "b": 
            temp_actual:int = random.randint(0, 40) # Random per la temperatura actual
            print(F"Temperatura actual: {temp_actual}") # Mostrem la temperatura actual
            calefaccio(on, off)
        case "c": # Opció per sortir d'aquest menú
            print("Sortint...")
        case "_": # En cas de posar altres tecles mostrem missatge
            print("Tecla invàlida, introdueix una de les opcions anteriors.")
    
def alarma():
    estat:bool = False # Alarma es troba desactivada per defecte
    co2_actual:int = random.randint(400, 1200) #Posem un número random com el co2 actual (ja que ho detecta automàticament)
    print("a) Configurar nivell màxim de CO2") # Mostrem opcions i demanem una
    print("b) Comprovar estat")
    print("c) sortir")
    opcio:str = input("Que vols fer? ").lower()
    co2:float = "" 
    match(opcio):
        case "a":
            co2:float = float(input("Introdueix nivell màxim de CO2 permès: ")) # Demanem el limit de co2 permès i el mostrem
            print(f"Nou límit de CO2: {co2}")
        case "b":
            if co2_actual >= co2: # Si el co2 actual supera el limit establert per l'usuari 
                estat == True # S'activa l'alarma
                print("L'alarma es troba activada")
            else: # Si no, no s'activa
                print("L'alarma es troba desactivada")
        case "c": # Opció per sortir
            print("Sortint...")
        case "_": # En cas de escollir altra tecla torna a demanar
            print("Introdueix una de les opcions anteriors")
            
def face_id(): 
    print("a) Accedir") # Mostrem les opcions i demanem una
    print("b) Registrar nova cara: ")
    opcio:str = input("Que vols fer? ")
    persones = []
    match(opcio):
        case "a": # Si vol accedir demanem a l'usuari que s'identifiqui
            persona:str = input("Qui ets?").lower()
            if persona in persones: # Si es troba a la llista de persones identificades permet accés
                print("Accès permès.")
            else: # Si no, denega accés
                print("Accès denegat")
        case "b": # Si vol introduir nova persona
            nova_persona:str = input("Introdueix la persona que vols incluir: ").lower() # Demanem una nova persona
            persones.append(nova_persona) # L'afegim a la llista

while True: # Creem el menú infinit aplicant les funcions anteriors
    print("a) Configurar aspersors")
    print("b) Calefacció")
    print("c) Alarma d'incendi")
    print("d) Porta Face ID")
    print("e) Sortir")
    opcio:str = input("Escogeix una opció: ").lower()
    match(opcio):
        case "a":
            aspersor()
        case "b":
            try: 
                menu_calefaccio()
            except ValueError:
                print("Valor incorrecte, introdueix un número decimal")
        case "c":
            alarma()
        case "d":
            face_id()
        case "e":
            print("Sortint del programa...")
            break
        case "_":
            print("Introdueix una de les opcions anteriors")