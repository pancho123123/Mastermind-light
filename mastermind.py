import random

todos_colores = ["rojo", "verde", "azul", "morado", "yellow", "celeste", "fucsia", "brown"]

colores = []

number_a = random.choice(todos_colores)
number_b = random.choice(todos_colores)
number_c = random.choice(todos_colores)
number_d = random.choice(todos_colores)

colores.append(number_a)
colores.append(number_b)
colores.append(number_c)
colores.append(number_d)

colores_escogidos = []
colores_escogidos2 = []
value = []
game = True


while game:
    while len(colores_escogidos) < 4:
        eleccion = input("Elige color: rojo(r), verde(v), azul(a), morado(m), yellow(y), celeste(c), fucsia(f) o brown(b)")
        if eleccion == "r":
            colores_escogidos.append("rojo")
            colores_escogidos2.append("rojo")
        elif eleccion == "v":
            colores_escogidos.append("verde")
            colores_escogidos2.append("verde")
        elif eleccion == "a":
            colores_escogidos.append("azul")
            colores_escogidos2.append("azul")
        elif eleccion == "m":
            colores_escogidos.append("morado")
            colores_escogidos2.append("morado")
        elif eleccion == "y":
            colores_escogidos.append("yellow")
            colores_escogidos2.append("yellow")
        elif eleccion == "c":
            colores_escogidos.append("celeste")
            colores_escogidos2.append("celeste")
        elif eleccion == "f":
            colores_escogidos.append("fucsia")
            colores_escogidos2.append("fucsia")
        elif eleccion == "b":
            colores_escogidos.append("brown")
            colores_escogidos2.append("brown")
        else:
            pass


    for i in range(4):
        if colores_escogidos[i] == colores[i]:
            value.append("red")
            colores[i] = "valued"
            colores_escogidos[i] = "pass"
        elif colores_escogidos[i] != colores[i]:
            if colores_escogidos[i] not in colores:
                colores_escogidos[i] = "pass"

    for i in range(4):
        if value[i] == "red":
            game = False

    for color in colores_escogidos:
        if color in colores:
            value.append("white")
            colores.remove(color)

    print(colores_escogidos2)
    print(value)
    colores = []
    colores.append(number_a)
    colores.append(number_b)
    colores.append(number_c)
    colores.append(number_d)
    colores_escogidos = []
    colores_escogidos2 = []
    value = []


colores = []
colores.append(number_a)
colores.append(number_b)
colores.append(number_c)
colores.append(number_d)
print(colores)