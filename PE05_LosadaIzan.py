tiquet = "" 
afegir = "s"
total_sense_iva = 0
comanda_existent = False

def mostrar_tiquet_complet():
    global tiquet # Variables globals
    global total_sense_iva

    iva = total_sense_iva * 0.10 # Calculem l'import de l'IVA
    total = total_sense_iva + iva # Calculem el total amb IVA

    tiquet_complet = ( tiquet + f"\n--------------------------------------\n" #Afegim la part posterior al tiquet
        f"Total sense iva: {total_sense_iva:.2f}\n"
        f"IVA: {iva:.2f}\n"
        f"Total a pagar: {total:.2f}\n"
        f"--------------------------------------")

    print(tiquet_complet)

def afegirproductes():
    global tiquet # Variables globals
    global afegir
    global total_sense_iva
    global comanda_existent

    nom = input("Introdueix el nom del client: ") # Demanem el nom de l'usuari
    afegir = "s" 
    total_sense_iva = 0

    tiquet = ( #Afegim els apartats fixes al tiquet
        "______________________________________\n"
        "=============== TIQUET ===============\n"
        "______________________________________\n"
        f"Client: {nom}\n"
        f"{'Producte':<15}{'Quantitat':<12}{'Preu unit.':<12}{'Subtotal':<10}\n"
        "--------------------------------------------------")
    comanda_existent = True # Ara existeix una comanda

    while afegir == "s": # Mentre afegeixi més executarem la funció
        afegirproducte()

    if afegir == "n": # En cas contrari mostra el tiquet
        mostrar_tiquet_complet()

def afegirproducte():
    global tiquet
    global afegir
    global total_sense_iva

    # Demanem les dades per un nou producte
    producte = input("Introdueix el producte: ")
    preu = float(input("Preu unitari: ").replace(",", "."))
    quantitat = int(input("Quantitat d'aquest producte: "))
    subtotal = quantitat * preu # Calculem el subtotal
    total_sense_iva += subtotal

    tiquet += f"\n{producte:<15}{quantitat:<12}{preu:<12.2f}{subtotal:<10.2f}" # Les afegim al tiquet

    afegir = input("Vols afegir més productes? (s/n): ").lower() # Tornem a demanar per si volgués tornar a agafar més productes
    while afegir not in ("s", "n"): # En cas de no posar opcions vàlides ho mostrem 
        print("Escogeix una opció vàlida") 
        afegir = input("Vols afegir més productes? (s/n): ").lower() # Tornem a preguntar

    mostrar_tiquet_complet() # Mostrem tiquet

def menuprincipal(): 
    opcio = 0
    while opcio != 4: # Mentre no escogeixi sortir
        print("--------------------------------------\n===== GESTIÓ COMANDES RESTAURANT =====\n--------------------------------------")
        print("1. Crear nova comanda\n2. Actualitzar comanda anterior\n3. Visualitzar últim tiquet\n4. Sortir")
        try:
            opcio = int(input("Tria una opció: "))
        except ValueError: # En cas d'introduir un valor incorrecte
            print("Tria una de les opcions anteriors (1-4).")
            continue
        except Exception as e:  # qualsevol altre error
            print("Ha ocorregut un error", e)
            continue
        if opcio not in (1, 2, 3, 4): # Si escogeix un numero que no es troba entre les opcions
            print("Escull una de les opcions anteriors (1-4)")
        else:
            match opcio: # Depenent de la tecla executem el mètode corresponent
                case 1:
                    print("______________________________________\n===========  NOVA COMANDA  ===========\n______________________________________")
                    afegirproductes()
                case 2:
                    if comanda_existent: # En cas d'existir comanda permetem afegir productes
                        print("________________________________\n=============== ACTUALITZA COMANDA ===============\n________________________________")
                        afegirproducte()
                    else: # Si no, ho mostrem
                        print("No hi ha cap comanda existent")
                case 3:
                    print("______________________________________\n============ ÚLTIM TIQUET ============\n______________________________________")
                    mostrar_tiquet_complet()
                case 4:
                    print("-------------------------------------\n========== FINS LA PROPERA ==========\n-------------------------------------")
                    break # Parem el bucle

if __name__ == "__main__":
    menuprincipal()