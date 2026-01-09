# Tabla de multiplicar (pide número al usuario)

numero = input("Escribe un número: ")
numero = int(numero)

print(f"\n--- tabla del {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")