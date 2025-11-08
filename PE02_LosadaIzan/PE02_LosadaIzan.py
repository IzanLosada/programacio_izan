import random #Importem la llibreria random
vida:int = 100 #Creem variable int pels punts de vida inicials

print("Ets un aventurer que entra a una cova misteriosa buscant un tresor màgic. Durant el camí, hauràs de prendre diverses decisions que afectaran el teu destí.")
print("Et trobes a l'entrada de la cova.")
dec = input("Entrar/Tornar? ").upper() #Afegim upper per pasar la resposta a majúscules 
if dec == "ENTRAR": #En cas d'entrar
    print("Continues caminant i trobes una bifurcació")
    cami = input("Esquerra/Dreta? ").upper() #Fem a l'usuari escollir entre els camins
    
    if cami == "ESQUERRA": #Si esculls el camí de l'esquerra
        print("Trobes una espasa brillant al terra")
        espasa = input("Agafes la espasa? SI/NO. ").upper() #Preguntem si agafa la espasa
        print("A continuació et trobes amb un drac protegint el tresor. ")
        if espasa == "SI": #Si l'agafes
            print("Gràcies a haver agafat l'espasa aconsegueixes matar al drac! ")
        elif espasa == "NO": #Si no l'agafes
            vida = vida - 50 #Baixem 50 punts de vida a l'usuari
            print(f"El drac et fa perdre 50 punts de vida et queden {vida} punts de vida.") #Mostrem el que ha passat i punts de vida restants
        font = input("Estas cansat després d'haver barallat contra el drac, però continues avançant i trobes una font. Beus d'ella? SI/NO. ").upper() #Preguntem a l'usuari si beu de la font
        if font == "SI":
            mort = random.randint(1, 2)
            if mort == 1:
                vida = 0
                print("L'aigua estava enverinada i mors. GAME OVER") #En cas de morir acabem el joc
            elif mort == 2:
                vida = vida - 50
                print(f"Perds 50 de vida punts restants {vida}")
                if vida == 0:
                    print("GAME OVER")
        if vida > 0:
            codi = random.randint(1, 5) #Generem un numero random entre 1-5
            intent = int(input("Trobes una porta amb un candau amb numeros entre 1-5. Introdueix un numero: "))
            if codi != intent and vida == 100: # Si no encerta
                vida = vida - 50 # Restem 50 punts de vida
                print(f"Codi incorrecte (la solució era {codi}). S'activa una trampa que et fa perdre 50 punts de vida. Punts restants: {vida}")
                codi = random.randint(1, 5) #Generem un nou numero random entre 1-5
                intent = int(input("S'ha generat un nou codi. Tens un altre intent. Introdueix un numero del 1-5: ")) #Demanem un nou intent
                if codi != intent: #Si torna a fallar
                    vida = vida - 50 #Resta 50 de vida
                    print(f"Codi incorrecte (la solució era {codi}). S'activa una trampa que et fa perdre 50 punts de vida. Punts restants: {vida}") #Ho mostrem
                    print("T'has quedat sense punts de vida. GAME OVER") #Perd
                else: #En cas d'encertar guanya
                    print("S'obre la porta i trobes el tresor. Enhorabona!") 
            elif codi != intent and vida == 50: #Si la vida arriba a 0 perd la partida i acaba el joc
                vida = vida - 50 # Restem 50 punts de vida
                print(f"Codi incorrecte (la solució era {codi}). S'activa una trampa que et fa perdre 50 punts de vida. Punts restants: {vida}. GAME OVER")
            else: #Si encerta
                print("S'obre la porta i trobes el tresor. Enhorabona!") #Guanya
    elif cami == "DRETA": #Si esculls el camí de la dreta.
        print("Trobes una porta amb una endevinalla.")
        endevinalla = input("Té claus però no pot obrir cap porta. Què és? ").lower() #Preguntem a l'usuari una endevinalla i la passem a minúscula.
        if endevinalla == "piano": #Si encerta
            print("Resposta correcta.")
            print("Aconsegueixes obrir la porta i trobes el tresor. Enhorabona") #Guanya
        else: #Si no encerta
            vida = vida - 50 #Restem punts de vida
            print(f"Resposta incorrecta, perds 50 punts de vida, vida restant: {vida}") #Mostrem punts restants
            print("Encara així tindràs una altra oportunitat")
            endevinalla2 = input("Té agulles però no sap cosir. Què és?").lower() #Fem el mateix procés amb una altra endevinalla
            if endevinalla2 == "rellotge": #Si encerta
                print("Resposta correcta.")
                print("Aconsegueixes obrir la porta i trobes el tresor. Enhorabona!") #Guanya
            else: #Si no encerta
                print(f"Resposta incorrecta, perds 50 punts de vida, vida restant: {vida}")
                print("T'has quedat sense punts de vida. GAME OVER") #Perd
                
elif dec == "TORNAR": #Si decideix tornar acaba el joc
    print("Decideixes que no val la pena arriscar-se i tornes a casa sense el tresor.")