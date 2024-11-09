"""
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
Diga que opción Incorrecta
"""
print("🎮 PIEDRA, PAPEL O TIJERA 🎮")
print("\nInstrucciones:")
print("- Cada jugador debe escribir una de estas opciones: piedra, papel o tijera")
print("- Las reglas son:")
print("  * Piedra vence a Tijera")
print("  * Tijera vence a Papel")
print("  * Papel vence a Piedra")
print("\n¡Que comience el juego!")
print("-" * 50)

#Turno del jugador Jugador 1
print("\n🎮 TURNO JUGADOR 1:")
jugador1 = input("Elige tu opción (piedra/papel/tijera): ").lower()

if jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera":
    print("\n ERROR: Opción incorrecta Jugador 1")
    print("Las opciones válidas son: piedra, papel o tijera")
else:
    print(" Opción válida Jugador 1")
    
    # Turno del Jugador 2
    print("\n TURNO JUGADOR 2:")
    jugador2 = input("Elige tu opción (piedra/papel/tijera): ").lower()
    
    if jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera":
        print("\n ERROR: Opción incorrecta Jugador 2")
        print("Las opciones válidas son: piedra, papel o tijera")
    else:
        print(" Opción válida Jugador 2")
        
        print("\n RESULTADO DEL JUEGO:")
        print(f"Jugador 1 eligió: {jugador1.upper()}")
        print(f"Jugador 2 eligió: {jugador2.upper()}")
        print("-" * 25)
        
        if jugador1 == jugador2:
            print(" ¡EMPATE!")
            print(f"Ambos jugadores eligieron {jugador1.upper()}")
        else:
            if jugador1 == "piedra":
                if jugador2 == "tijera":
                    print("🏆 ¡GANA JUGADOR 1!")
                    print("Piedra rompe Tijera")
                else:
                    print("🏆 ¡GANA JUGADOR 2!")
                    print("Papel envuelve Piedra")
            else:
                if jugador1 == "papel":
                    if jugador2 == "piedra":
                        print("🏆 ¡GANA JUGADOR 1!")
                        print("Papel envuelve Piedra")
                    else:
                        print("🏆 ¡GANA JUGADOR 2!")
                        print("Tijera corta Papel")
                else:
                    if jugador2 == "papel":
                        print("🏆 ¡GANA JUGADOR 1!")
                        print("Tijera corta Papel")
                    else:
                        print("🏆 ¡GANA JUGADOR 2!")
                        print("Piedra rompe Tijera")

print("\nFin del juego 👋")