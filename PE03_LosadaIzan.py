while True: # bucle infinit
    print("a) Introduir dades") # Mostrem menu amb opcions
    print("b) Modificar dades")
    print("c) Visualitzar dades")
    print("d) Sortir")
    
    decisio:str = input("Introdueix una opció: ").lower()
    match(decisio): # Fem match per separar les opcions de l'usuari en cases
        case "a": # # En cas d'introduir "a" al menú inicial
            print("Opció escollida: a) Introduir dades")
            nom:str = input("Introdueix el teu nom complet: ")
            if nom == "": # Nom buit - mostrem error   
                print("Error: El nom no pot quedar buit.")
            elif len(nom) < 2:
                print("Longitud invàlida")
            else:
                try:
                    edat:int = int(input("Introdueix la teva edat: "))
                except ValueError: # Si no posa un número enter mostrem error
                    print("Error: L'edat ha de ser un enter positiu ≤ 120.")
                else:
                    if edat <= 0 or edat > 120: # En cas de no cumplir valors limit mostrem error
                        print("Error: L'edat ha de ser un enter positiu ≤ 120.")
                    else:
                        try: 
                            pes:float = float(input("Introdueix el teu pes: ").replace(",", ".")) # Utilitzem un replace que cambia les (,) per (.) així l'usuari podrà introduir qualsevol d'elles
                        except ValueError: # Si introdueix caracter que no sigui numero / num amb decimals mostrem error
                            print("El pes ha de ser un nombre decimal positiu")
                        else:
                            if pes > 400 or pes <= 0: # En cas de superar valors límits mostrem error
                                print("Error: El pes ha de ser un decimal positiu raonable.")
                            else:
                                try:
                                    alçada:float = float(input("Introdueix la teva alçada: ").replace(",", ".")) # Utilitzem un replace que cambia les (,) per (.) així l'usuari podrà introduir qualsevol d'elles
                                except ValueError: # Si introdueix caracter que no sigui numero / num amb decimals mostrem error
                                    print("Error: El pes ha de ser un decimal positiu raonable.")
                                else:
                                    if alçada < 0.5 or alçada > 2.5: # En cas de superar valors límits mostrem error
                                        print("Error: L'alçada ha de ser un decimal positiu entre 0.5 i 2.5 metres.")
                                    else: # Si no hi han hagut errors mostrem el següent missatge
                                        print("Dades introduïdes correctament. ")
        case "b": # En cas d'introduir "b" al menú inicial
            print("Opció escollida: b) Modificar dades") # Mostrem opció escollida i dades a modificar
            print("a) Nom")
            print("b) Edat")
            print("c) Pes")
            print("d) Alçada")
            modificar:str = input("Quina dada vols modificar? ").lower()
            match(modificar):
                case "a": # Si escull a
                    nom_modi:str = input("Introdueix el teu nom complet: ") # Demanem un nou nom
                    if nom_modi == "": # Evitem que el pugui deixar buit
                        print("Error: El nom no pot quedar buit.")
                    else: # En cas de ser correcte
                        nom = nom_modi # Modiifquem el nom
                        print(f"Dada modificada. Hola {nom}!")
                case "b": # Si escull b
                    try:
                        edat_modi:int = int(input("Introdueix la teva edat: ")) # Demanem una nova edat
                    except ValueError: # Si no posa un número enter mostrem error
                        print("Error: L'edat ha de ser un enter positiu ≤ 120.")
                    else: 
                        if edat_modi < 0 or edat_modi >= 120: # En cas de superar valors límits mostrem error
                            print("Error: L'edat ha de ser un enter positiu ≤ 120.")
                        else: # En cas de ser correcte
                            edat = edat_modi # Modifiquem l'edat anterior
                            print(f"Edat modificada correctament. Nova edat: {edat}")
                case "c": # Si escull c
                    try:    
                        pes_modi:float = float(input("Introdueix el teu pes: ").replace(",", ".")) # Demanem un nou pes
                    except ValueError: # Si introdueix caracter que no sigui numero / num amb decimals mostrem error
                        print("El pes ha de ser un nombre decimal positiu menor de 400")
                    else: 
                        if pes_modi < 0 or pes_modi >= 400: # En cas de superar valors límits mostrem error
                            print("Error: El pes ha de ser un decimal positiu raonable.")
                        else: # En cas de ser correcte
                            pes = pes_modi # Modifiquem el pes anterior
                            print(f"Pes modificat correctament. Nou pes: {pes}")
                case "d": # Si escull d
                    try:
                        alçada_modi:float = float(input("Introdueix la teva alçada: ").replace(",", ".")) # Demanem una nova alçada
                    except ValueError: # Si introdueix caracter que no sigui numero / num amb decimals mostrem error
                        print("Error: El pes ha de ser un decimal positiu raonable.")
                    else:
                        if alçada_modi < 0.5 or alçada_modi > 2.5: # En cas de superar valors límits mostrem error
                            print("Error: L'alçada ha de ser un decimal positiu entre 0.5 i 2.5 metres.")
                        else: # En cas de ser correcte
                            alçada:float = alçada_modi # Modifiquem l'alçada anterior
                            print(f"Dades introduïdes correctament. Nova alçada: {alçada} ")
        case "c": # En cas d'introduir "c" al menú inicial
            print("Opció escollida: c) Visualitzar dades") # Mostrem opció escollida 
            nom = nom.capitalize() # Opció per passar a majúscules la primera lletra de cada paraula
            print(f"Hola {nom}!") 
            imc:float = pes / (alçada * alçada) # Calculem l'IMC
            if imc < 18.5: # Mostra l'IMC amb dos decimals i amb condicionals comprova l'estat de pes
                print(f"IMC: {imc:.2f} Pes baix")
            elif imc >= 18.5 and imc <= 24.9:
                print(f"IMC: {imc:.2f} Pes normal")
            elif imc >= 25 and imc < 30:
                print(f"IMC: {imc:.2f} Sobrepes")
            else:
                print(f"IMC: {imc:.2f} Obesitat")
            fc_max:int = 220 - edat # Calculem la fc màxima
            print(f"FC màxima estimada: {fc_max} bpm") #Mostrem la fc màxima
            fc50:float = fc_max * 0.5  #Calculem el 50% i 85%
            fc85:float = fc_max * 0.85
            print(f"Zona FC objectiu: {int(fc50)} – {int(fc85)} bpm") #Mostrem els percentatges anteriors
            aigua = pes * 0.35  # Calculem els ml necesaris i els passem a litres
            print(f"Aigua recomenada: {aigua:.2f} L/dia")
            print(f"Any de naixement aproximat: {2025 - edat}") # Calculem i mostrem any de naixement
        case "d": # En cas d'introduir "d" al menú inicial
            print("Sortint del programa...") # Para el bucle i surt del programa
            break
        case _: # En cas d'introduir qualsevol altra cosa al menú inicial mostra les opcions i torna a preguntar
            print("Has d'introduir una de les opcions anteriors (a,b,c,d)")