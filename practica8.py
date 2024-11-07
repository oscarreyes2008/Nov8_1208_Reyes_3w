print(" ")#deja un espacio a la hora de ejecutar
print("Oscar Alonso Reyes Yañez_1208_3w:practica sobre tabla de multiplicar ")
print(" ")#deja un espacio a la hora de ejecutar

# Número cuyo rango de multiplicación queremos mostrar
numero = int(input("Introduce el número para la tabla de multiplicar: "))

# Imprimir la tabla de multiplicar utilizando un rango
for i in range(1, 11):  
    print(f"{numero} x {i} = {numero * i}")
