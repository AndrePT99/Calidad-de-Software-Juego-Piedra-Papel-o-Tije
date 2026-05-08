import random

def obtener_jugada_sistema():
    return random.choice(["piedra", "papel", "tijera"])


def determinar_ganador(usuario, sistema):
    if usuario == sistema:
        return "empate"
    
    if (usuario == "piedra" and sistema == "tijera") or \
       (usuario == "papel" and sistema == "piedra") or \
       (usuario == "tijera" and sistema == "papel"):
        return "usuario"
    
    return "sistema"


def mostrar_resultado(usuario, sistema, resultado):
    print("\n---------------------------")
    print(f"🧑 Usuario: {usuario}")
    print(f"💻 Sistema: {sistema}")
   
    if resultado == "empate":
        print("😶 ¡Empate!")
    elif resultado == "usuario":
        print("😁 ¡Ganaste!")
    else:
        print("😢 Perdiste")
    print("---------------------------\n")


def obtener_jugada_usuario():
    while True:
        usuario = input("Elige (piedra, papel, tijera): ").lower()
        if usuario in ["piedra", "papel", "tijera"]:
            return usuario
        print("⚠️ Entrada inválida, intenta de nuevo.")


def jugar():
    print("🎮 BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA")
    rondas = 5

    puntaje = {
        "usuario": 0,
        "sistema": 0,
        "empate": 0
    }

    for ronda in range(1, rondas + 1):
        print(f"\n🔁 Ronda {ronda} de {rondas}")

        usuario = obtener_jugada_usuario()
        sistema = obtener_jugada_sistema()

        resultado = determinar_ganador(usuario, sistema)
        puntaje[resultado] += 1

        mostrar_resultado(usuario, sistema, resultado)

    # Resultado final
    print("//////////////////////////////////////////////")
    print(" ")
    print("\n🏁 RESULTADO FINAL")
    print(f"Usuario: {puntaje['usuario']}")
    print(f"Sistema: {puntaje['sistema']}")
    print(f"Empates: {puntaje['empate']}")

    print("//////////////////////////////////////////////")
    print(" ")
    
    if puntaje["usuario"] > puntaje["sistema"]:
        print("🎉 ¡Ganaste el juego!")
    elif puntaje["usuario"] < puntaje["sistema"]:
        print("😢 Perdiste el juego")
    else:
        print("🤝 El juego terminó en empate")


if __name__ == "__main__":
    jugar()