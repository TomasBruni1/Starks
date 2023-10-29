def normalizar_datos(lista):
    for e_lista in lista:
        if type(e_lista["altura"]) != type(float()):
            e_lista["altura"] = float(e_lista["altura"])
        if type(e_lista["peso"]) != type(float()):
            e_lista["peso"] = float(e_lista["peso"])
        if type(e_lista["fuerza"]) != type(float()):
            e_lista["fuerza"] = float(e_lista["fuerza"])

def imprimir_heroes(lista:list, genero:str):
    if genero == "M":
        for e_lista in lista:
            if e_lista["genero"] == "M":
                print(e_lista["nombre"])
    if genero == "F":
        for e_lista in lista:
            if e_lista["genero"] == "F":
                print(e_lista["nombre"])
    if genero != "F" and genero != "M":
        return print(-1)

def calcular_maximo_minimo(lista:list, estado:str, clave:str, genero:str):
    minmax = lista[0]
    flag = True
    for heroe in lista:
            if heroe["genero"] == genero:
                if flag or (estado == "max" and heroe[clave] > minmax[clave]):
                    minmax = heroe
                    flag = False
                elif flag or (estado == "min" and heroe[clave] < minmax[clave]):
                    minmax = heroe
                    flag = False
    if estado not in ["min", "max"] or genero not in ["F", "M"]:
        return -1
    return minmax
"""
    if estado == "max" and genero == "M":
        for heroe in lista:
            if heroe["genero"] == genero:
                if heroe[clave] > minmax[clave]:
                    minmax = heroe
    elif estado == "max" and genero == "F":
        for heroe in lista:
            if heroe["genero"] == genero:
                if heroe[clave] > minmax[clave]:
                    minmax = heroe
    elif estado == "min" and genero == "M":
        for heroe in lista:
            if heroe["genero"] == genero:
                if heroe[clave] < minmax[clave]:
                    minmax = heroe
    elif estado == "min" and genero == "F":
        for heroe in lista:
            if heroe["genero"] == genero:
                if heroe[clave] < minmax[clave]:
                    minmax = heroe
                    """

def imprimir_superheroe(lista:list, estado:str, clave:str, genero:str):
    minmax = calcular_maximo_minimo(lista, estado, clave, genero)
    print("Superheroe {0}: {1} | {2}: {3}".format(genero, minmax["nombre"], clave, minmax[clave]))

def calcular_promedio(lista:list, clave:str, genero:str):
    acumulador= 0
    contador = 0
    for heroes in lista:
        if heroes["genero"] == genero:
            acumulador += heroes[clave]
            contador += 1
    promedio = acumulador / contador
    return promedio

def imprimir_promedio(lista:list, clave:str, genero:str) -> str:
    print("Promedio: ", calcular_promedio(lista, clave, genero))

def obtener_tipode(lista:list, clave:str):
    contadortipos = {}

    for elemento in lista:
        contadortipos[elemento[clave].capitalize()] = 0

    for elemento in lista:
        contadortipos[elemento[clave].capitalize()] += 1

    for tipo in contadortipos:
        if tipo == " ":
            print("No tiene", clave.replace("_", " de "))
        else:
            print("Hay {0} superhéroes con {1} {2}.".format(contadortipos[tipo], clave.replace("_", " de "), tipo))

def listar_superheroes_segun_tipo(lista:list, clave:str):
    for heroe in lista:
        print("Superheroe: {0} | {1} {2}".format(heroe["nombre"], clave.replace("_", " de ").capitalize(), heroe[clave]))

def stark_marvel_app(lista:list):
    normalizar_datos(lista)
    while True:
        print("Menu de opciones:\n1. Mostrar heroes masculinos\n2. Mostrar heroes femeninos\n3. Superheroes masculino mas alto\n4. Superheroe femenino mas alto\n5. Superheroe masculino mas bajo\n6. Superheroe femenino mas bajo\n7. Altura promedio masculinos\n8. Altura promedio femeninos\n9. ¿Cuantos superheroes tienen cada color de ojos?\n10. ¿Cuantos superheroes tienen cada color de pelo?\n11. ¿Cuantos superheroes tienen cada tipo de inteligencia?\n12. Superheroes por color de ojos\n13. Superheroes por color de pelo\n14. Superheroes por tipo de inteligencia\n15. Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            imprimir_heroes(lista, "M")
        if opcion == 2:
            imprimir_heroes(lista, "F")
        if opcion == 3:
            imprimir_superheroe(lista, "max", "altura", "M")
        if opcion == 4:
            imprimir_superheroe(lista, "max", "altura", "F")
        if opcion == 5:
            imprimir_superheroe(lista, "min", "altura", "M")
        if opcion == 6:
            imprimir_superheroe(lista, "min", "altura", "F")
        if opcion == 7:
            imprimir_promedio(lista, "altura", "M")
        if opcion == 8:
            imprimir_promedio(lista, "altura", "F")
        if opcion == 9:
            obtener_tipode(lista, "color_ojos")
        if opcion == 10:
            obtener_tipode(lista, "color_pelo")
        if opcion == 11:
            obtener_tipode(lista, "inteligencia")
        if opcion == 12:
            listar_superheroes_segun_tipo(lista, "color_ojos")
        if opcion == 13:
            listar_superheroes_segun_tipo(lista, "color_pelo")
        if opcion == 14:
            listar_superheroes_segun_tipo(lista, "inteligencia")
        if opcion == 15:
            break