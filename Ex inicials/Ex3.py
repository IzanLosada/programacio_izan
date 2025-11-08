paraigues:bool = False
plou:bool = input("plou?") == "si" 
nuvol:bool = input("nuvol?") == "si"

paraigues = plou or nuvol
print(paraigues)