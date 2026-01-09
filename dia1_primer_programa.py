# Mi primer programa - 8 de enero 2026

nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}! Bienvenido a tu viaje como programador")

edad = input("¿Cuántos años tienes? ")
edad = int(edad)

if edad < 18:
    print(f"{nombre}, aún eres menor de edad")
else:
    print(f"{nombre}, ya eres adulto")
