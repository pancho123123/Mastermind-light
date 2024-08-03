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
value = []
number_times = 4


while colores != colores_escogidos:
    while len(colores_escogidos) < 4:
        eleccion = input("Elige un color: rojo(r), verde(v), azul(a), morado(m), yellow(y), celeste(c), fucsia(f) o brown(b)")
        if eleccion == "r":
            colores_escogidos.append("rojo")
        elif eleccion == "v":
            colores_escogidos.append("verde")
        elif eleccion == "a":
            colores_escogidos.append("azul")
        elif eleccion == "m":
            colores_escogidos.append("morado")
        elif eleccion == "y":
            colores_escogidos.append("yellow")
        elif eleccion == "c":
            colores_escogidos.append("celeste")
        elif eleccion == "f":
            colores_escogidos.append("fucsia")
        elif eleccion == "b":
            colores_escogidos.append("brown")
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

    for color in colores_escogidos:
        if color in colores:
            value.append("white")
            colores.remove(color)

    print(value)
    colores = []
    colores.append(number_a)
    colores.append(number_b)
    colores.append(number_c)
    colores.append(number_d)
    print(colores)
    colores_escogidos = []
    value = []


colores = []
colores.append(number_a)
colores.append(number_b)
colores.append(number_c)
colores.append(number_d)
print(colores)