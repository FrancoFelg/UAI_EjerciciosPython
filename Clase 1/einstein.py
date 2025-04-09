

def getE(M):
    #M * C**2
    return M * 300000000 ** 2
    
# E = MC ** 2

# E = Energía medida en Julios
# M = Masa (KG)
# C = Velocidad de la luz (300.000.000 Mts x Seg)

masa = float(input("Inserte la masa como entero en KG: "))
rta = getE(masa)
print("La energía en Julios es igual a ", rta)