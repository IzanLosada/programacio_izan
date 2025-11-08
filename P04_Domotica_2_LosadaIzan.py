import random

aigua:float = None # Variabes per aigua i hora a executar-se
hora:float = None

def aspersor():  # Funció per l'aspersor
    asp = ""
    while asp != "c": # Mentre no sigui sortir s'efectua el bucle
        global hora # Variables com a globals
        global aigua
        print("a) Modificar horaris d'ús / Aigua")  # Mostrem opcions
        print("b) Suspensió/Apagar aspersors")
        print("c) Sortir")
        asp = input("Que vols fer? ").lower()
        if asp == "a":
            try:
                hora = float(input("Introdueix hora d'ús: ").replace(":", ".")) #Demanem i mostrem dades d'hora i aigua
                aigua = float(input("Introdueix el nombre de litres d'aigua que vols utilitzar: ").replace(",", "."))
                print(f"Nova hora introduïda: {hora:.2f} h.")
                print(f"Nova quantitat d'aigua establerta: {aigua:.2f} L.")
            except ValueError:
                print("Introdueix valors numèrics vàlids.")
        elif asp == "b":
            hora = None # Buidem les variables
            aigua = None
            print("Aspersors desactivats. (Hauràs de reconfigurar la hora per que tornin a activar-se)")
        elif asp == "c":
            print("Sortint...")
            break # Parem el bucle el que farà tornar al menú anterior
        else:
            print("Introdueix una de les opcions anteriors.")

on = None # Definim variables
off = None
def estatcalefaccio():
    global on # Variables com a globals
    global off
    temp_actual = random.randint(0, 40)  # Random per la temperatura actual
    print(f"Temperatura actual: {temp_actual}")  # Mostrem la temperatura actual

    if on is None or off is None: # En cas d'estar buides ho fem saber a l'usuari
        print("No s'han configurat les temperatures límit.")
    # Depenent de la temperatura actual i els límits establerts per l'usuari mostrem l'estat de la calefacció
    if temp_actual < on:
        print("Calefacció activada (la temperatura és inferior al mínim establert).")
    elif temp_actual > off:
        print("Calefacció desactivada (la temperatura és superior al màxim establert).")
    else:
        print("Calefacció activada (temperatura dins del rang).")

def calefaccio(a, b):  # Funció per mostrar temperatures límit
    print(f"Configuració reconfigurada correctament: Nova temperatura mínima per activar la calefacció: {a}.")
    print(f"nova temperatura màxima per apagar-la: {b}.")

def menu_calefaccio():  # Funció com menú de calefacció
    global on, off
    opcio = ""
    while opcio != "c": # Mentre no sigui sortir s'efectua el bucle
        print("a) Ingresar temperatures límits")
        print("b) Mostrar estat")
        print("c) Sortir")
        opcio = input("Que vols fer: ").lower()
        match opcio:
            case "a":
                try: # Demanem temperatures límits i les mostrem
                    on = float(input("Introdueix el número de graus mínim per activar la calefacció: ").replace(",", "."))
                    off = float(input("Introdueix el número de graus per apagar la calefacció: ").replace(",", "."))
                    calefaccio(on, off)
                except ValueError:
                    print("Introdueix un valor vàlid")
            case "b":
                estatcalefaccio()
            case "c":
                print("Sortint...")
                break
            case _:
                print("Tecla invàlida, introdueix una de les opcions anteriors.")

estat = False # Definim variable en false com predeterminat
co2_limit = 800  # valor inicial per defecte

def estatalarma(a, b):
    global estat # Variable global
    if a >= b:  # Si el co2 actual supera el límit estat pasa a ser true si no false
        estat = True
    else:
        estat = False
    
    if estat: # Mostrem l'estat de l'alarma amb el nivell de Co2
        print("L'alarma es troba activada")
        print(f"Nivell Co2 actual: {a}")
    else:
        print("L'alarma es troba desactivada")
        print(f"Nivell Co2 actual: {a}")

def alarma():
    global co2_limit # Deixem la variable com global
    opcio = ""
    while opcio != "c": # Mentre no sigui sortir s'efectua el bucle
        co2_actual = random.randint(400, 1200) # Random pel Co2 actual
        print("a) Configurar nivell màxim de CO2")
        print("b) Comprovar estat")
        print("c) Sortir")
        opcio = input("Què vols fer? ").lower()

        match opcio:
            case "a":
                try: # Demanem el límit de cCo2 i ho mostrem
                    co2_limit = float(input("Introdueix nivell màxim de CO2 permès: "))
                    print(f"Nou límit de CO2: {co2_limit}")
                except ValueError:
                    print("Introdueix un valor numèric vàlid.")
            case "b": # Cridem a la funció per comprovar l'estat de l'alarma depenent del Co2 límit i actual
                estatalarma(co2_actual, co2_limit)
            case "c":
                print("Sortint del menú d'alarma...")
                break
            case _:
                print("Tecla invàlida.")

accessos = 0 # Variable per comptar accessos
def simular_faceid():
    global accessos # La deixem com a global
    numrandom = random.randint(1, 20) # Generem un num random i si surt 20 sumem un accés al dia
    if numrandom == 20:
        accessos += 1
    print(f"Accessos avui: {accessos}")

persones = [] # Llista per persones amb accés
def face_id(): 
    opcio = ""
    while opcio != "c": # Mentre no sigui sortir s'efectua el bucle
        print("a) Accedir") # Mostrem les opcions i demanem una
        print("b) Registrar nova cara: ")
        print("c) Sortir")
        opcio:str = input("Que vols fer? ")
        match(opcio):
            case "a": # Si vol accedir demanem a l'usuari que s'identifiqui
                persona:str = input("Qui ets? ").lower()
                if persona in persones: # Si es troba a la llista de persones identificades permet accés
                    print("Accès permès.")
                else: # Si no, denega accés
                    print("Accès denegat")
            case "b": # Si vol introduir nova persona
                nova_persona:str = input("Introdueix la persona que vols incluir: ").lower() # Demanem una nova persona
                persones.append(nova_persona) # L'afegim a la llista
            case "c":
                print("Sortint...")
                break
            case _:
                print("Tecla invàlda")

def menu_conf(): # Menú de configuració
    opcio = ""
    while opcio != "e": # Mentre no sigui sortir s'efectua el bucle
        print("MODE CONFIGURACIÓ")
        print("a) Configurar aspersors")
        print("b) Calefacció")
        print("c) Alarma d'incendi")
        print("d) Porta Face ID")
        print("e) Sortir")
        opcio = input("Escogeix una opció: ").lower()
        match opcio: # Depenent de la selecció posem la funció que redirigeix a l'usuari al menú corresponent
            case "a":
                aspersor()
            case "b":
                menu_calefaccio()
            case "c":
                alarma()
            case "d":
                face_id()
            case "e":
                print("Sortint del menú principal...")
                break
            case _:
                print("Introdueix una de les opcions anteriors.")

def menuprincipal(): # Menú principal
    opcio = ""
    while opcio != "c": # Mentre no sigui sortir s'efectua el bucle
        opcio = input("Escogeix mode configuració (a), simulació (b) o sortir (c): ")
        match(opcio): # Redirigim a l'usuari al menú corresponent
            case "a":
                menu_conf()
            case "b":
                simulacio()
            case "c":
                print("sortint...")
                break
            case _:
                print("Tecla no vàlida.")

def simulacio(): # Part de simulació
    hores = 0 # Variables per hores i mins
    minuts = 0
    global co2_limit # Variables globals
    global hora
    global aigua 
    global on 
    global off 
    global accessos
    opcio = ""
    while opcio != "e": # Mentre no sigui sortir s'efectua el bucle
        minuts += 15 # Bucle per hores (suma 15 min per iteració)
        if minuts >= 60:
            minuts = 0
            hores += 1
            if hores >= 24:
                hores = 0

        print("MODE SIMULACIÓ")
        print("a) Estat aspersors")
        print("b) Estat de la calefacció")
        print("c) Estat alarma d'incendi")
        print("d) Estat Face ID")
        print("e) Sortir")
        opcio = input("Que vols comprovar? ").lower()

        match opcio:
            case "a":
                if hora is None or aigua is None: # En cas de no haver configurat les variables o mostrem
                    print("Aspersors desactivats. Sense configurar.")
                else: # En altre cas calculem l'hora actual passant-la a un decimal
                    hora_actual = hores + minuts / 60
                    marge = 10 / 60 # Calculem un marge de temps que pot durar el procés
                    if hora_actual >= hora and hora_actual <= hora + marge: # En cas que l'hora actual es trobi dins dels paràmetres + marge afegits per l'usuari es troben activats
                        print(f"Aspersors activats. Usant {aigua:.2f} L d'aigua.")
                    else: # Si no estan desactivats
                        print(f"Aspersors desactivats. Hora actual: {hora_actual:.2f} h, hora programada: {hora:.2f} h.")
            case "b": # Mostrem l'estat de la calefacció
                estatcalefaccio()
            case "c": 
                co2_actual = random.randint(400, 1200)
                estatalarma(co2_actual, co2_limit) # Mostrem l'estat de l'alarma
            case "d": # Simulem el face id
                simular_faceid()
            case "e":
                print("Sortint de la simulació...")
                break
            case _:
                print("Tecla invàlida.")

if __name__ == "__main__":
    menuprincipal()