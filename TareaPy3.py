peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
masa_corporal = peso / (estatura**2)
print("Su IMC es: "+str(round(masa_corporal, 2)))
