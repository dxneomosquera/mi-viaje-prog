import random

numero_secreto = random.randint(1, 50)
intentos = 0
adivinado = False

print("🎮 JUEGO DE ADIVINANZA - Tengo un número del 1 al 50")
print("Tienes 10 intentos\n")

while not adivinado and intentos < 10:
    intento = input(f"Intento {intentos + 1}: Escribe un número: ")
    intento = int(intento)
    intentos += 1

    if intento < numero_secreto:
        print("📍 Muy bajo, intenta con uno más grande\n")
    elif intento > numero_secreto:
        print("📍 Muy alto, intenta con uno más pequeño\n")
    else:
        print(f"🎉 ¡Correcto! Lo adivinaste en {intentos} intentos")
        adivinado = True

if not adivinado:
    print(f"😢 No lo adivinaste. El número secreto era {numero_secreto}")