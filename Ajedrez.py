blancas = ["TB", "CB", "AB", "QB", "KB", "PB"]
negras = ["TN", "CN", "AN", "QN", "KN", "PN"]
lletres = ["A", "B", "C", "D", "E", "F", "G"]

def crear_jugadors():
    jugadors = []
    j1 = input("Introdueix el nom del jugador 1 (Blanc): ")
    j2 = input("Introdueix el nom del jugador 2 (Negre): ")
    jugadors.append(j1)
    jugadors.append(j2)

    print(f"Jugador 1: {jugadors[0]}, Jugador 2: {jugadors[1]}")
    print("Noms assignats, comença la partida!")

    return jugadors

def crear_taulell():
    taulell = []

    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(" ")
        taulell.append(fila)

    taulell[1] = ["PB"] * 8
    taulell[0] = ["TB", "CB", "AB", "QB", "KB", "AB", "CB", "TB"]

    taulell[7] = ["TN", "CN", "AN", "QN", "KN", "AN", "CN", "TN"]
    taulell[6] = ["PN"] * 8

    return taulell

def mostrar_taulell(taulell):
    print("\n    a    b    c    d    e    f    g    h")
    print("  +" + "----+" * 8)

    for i in range(8):
        print(f"{i + 1} |", end="")
        for peça in taulell[i]:
            if peça == " ":
                print("    |", end="")
            else:
                print(f" {peça} |", end="")
        print(f" {i + 1}")
        print("  +" + "----+" * 8)

    print("    a    b    c    d    e    f    g    h\n")

def comprovar_peça(taulell, fila, columna, torn, blancas, negras):
    peça = taulell[fila][columna]

    if peça == " ":
        print("No hi ha cap peça en aquesta posició!")
        return None

    if peça in blancas and torn == 0:
        print("Peça correcta (blanca)")
        return peça

    if peça in negras and torn == 1:
        print("Peça correcta (negra)")
        return peça

    print("Peça equivocada")
    return None

def joc():
    ronda = 0
    guanyador = False
    torn = 0

    while not guanyador:
        mostrar_taulell(taulell_def)
        print(f"Torn del jugador {torn + 1}, {jugadors[torn]}")

        fila = int(input("Fila de la peça (1 - 8): ")) - 1
        columna = input("Columna de la peça (a - h): ").upper()
        
        if columna == "ABANDONAR":
            if torn == 0:
                print(f"Guanyador jugador negre, {jugadors[1]}")
            else:
                print(f"Guanyador jugador blanc, {jugadors[0]}")
            
            guanyador = True
            break
        
        if columna not in lletres and not "ABANDONAR":
            print("Columna invàlida")
            continue
            
        col = lletres.index(columna)

        peça = comprovar_peça(taulell_def, fila, col, torn, blancas, negras)
        
        if peça is None: # Error en piezas, volver
            continue
        else: # Diferenciar piezas (acabar)
            if peça in blancas:
                if peça == "PB":
                    pass
                elif peça == "TB":
                    pass
                elif peça == "CB":
                    pass
                
            elif peça in negras:
                if peça == "PN":
                    pass
                elif peça == "TN":
                    pass
                elif peça == "CN":
                    pass

        fila_dest = int(input("Fila destí (1 - 8): ")) - 1
        col_dest = input("Columna destí (a - h): ").upper()

        if col_dest not in lletres:
            print("Columna invàlida")
            continue

        col_dest = lletres.index(col_dest)

        if taulell_def[fila_dest][col_dest] != " ":
            print("Aquesta casella ja està ocupada!")
            continue

        taulell_def[fila_dest][col_dest] = peça
        taulell_def[fila][col] = " "
        
        torn += 1
        if torn > 1:
            torn = 0

if __name__ == "__main__":
    jugadors = crear_jugadors()
    taulell_def = crear_taulell()
    mostrar_taulell(taulell_def)
    joc()
