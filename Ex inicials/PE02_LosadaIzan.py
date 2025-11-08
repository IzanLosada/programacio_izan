edat = int(input("Quina és la teva edat? "))
soci = input("Ets soci? SI/NO")

if (edat < 18):
    print("no pots entrar per edat")
elif (edat >= 18 and edat < 35 and soci == "NO"):
    print("Pots entrar amb un preu de 20€")
elif (edat >= 35):
    print("Pots accedir gratuïtament per ser major de 35")
elif (edat > 18 and soci == "SI"): 
    print("Entres gratuitament")