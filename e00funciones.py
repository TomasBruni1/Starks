#1
def obtener_nombre(diccionario:dict) -> str:
    return diccionario["nombre"]

def imprimir_dato(dato:str):
    print(dato)

def stark_imprimir_nombres_heroes(lista:list):
    retorno = -1
    if(len(lista) > 0):
        for e_lista in lista:
            nombre = obtener_nombre(e_lista)
            retorno = imprimir_dato(nombre)
    return retorno

def stark_imprimir_nombres_alturas(lista:list):
    retorno = -1
    if len(lista) > 0:
        for e_lista in lista:
            obtener_nombre_y_dato(e_lista, "altura")
    else:
        return retorno

#2
def obtener_nombre_y_dato(diccionario:dict, dato:str) -> str:
    nombre_dato = "Nombre {0} | {1} {2}".format(diccionario["nombre"], dato.capitalize(), diccionario[dato])
    return print(nombre_dato)

#3
def calcular_max(lista:list, key:str):
    max = lista[0]
    for e_lista in lista:
        if e_lista[key] > max[key]:
            max = e_lista
    return max
#4
def calcular_min(lista:list, key:str):
    min = lista[0]
    for e_lista in lista:
        if e_lista[key] < min[key]:
            min = e_lista
    return min

def calcular_max_min_dato(lista:list, estado:str, key:str):
    if estado == "max":
        max = calcular_max(lista, key)
        return max
    elif estado == "min":
        min = calcular_min(lista, key)
        return min

def stark_calcular_imprimir_heroe(lista:list, estado:str, key:str):
    maxmin = calcular_max_min_dato(lista, estado, key)
    print("Superheroe: {0} | {1} {2}".format(maxmin["nombre"], key, maxmin[key]))

def es_dict(diccionario:dict) -> bool:
    return type(diccionario) == type(dict()) and len(diccionario) > 0
#5

def contador(lista:list):
    contador = 0
    for e_lista in lista:
        contador += 1
    return contador

def sumar_dato_heroe(lista:list, key:str):
    acu_key = 0
    for e_lista in lista:
        if es_dict(e_lista):
            acu_key += e_lista[key]
    return acu_key

def dividir(dividendo:int, divisor:int):
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor
    
def calcular_promedio(lista:list, key:str):
    acu_key = sumar_dato_heroe(lista, key)
    con_key = contador(lista)
    division = dividir(acu_key, con_key)
    return division

def stark_calcular_imprimir_promedio_altura(lista:list, key:str):
    retorno = 1
    if len(lista) > 0:
        retorno = calcular_promedio(lista, key)
    return imprimir_dato(retorno)

#6
def imprimir_menu():
    imprimir_dato("Menu de opciones:\n1. Superheroe mas alto\n2. Superheroe mas bajo\n3. Promedio de altura\n4. Superheroe mas pesado\n5. Superheroe menos pesado\n6. Salir")

def validar_entero(string:str):
    return string in ["0","1","2","3","4","5","6","7","8","9"]

def stark_menu_principal():
    retorno = -1
    print(imprimir_menu())
    opcion = input("Opcion: ")
    if validar_entero(opcion):
        retorno = int(opcion)
    return retorno
    
#7
def stark_marvel_app(lista:list):
    stark_normalizar_datos(lista)
    stark_imprimir_nombres_heroes(lista)
    stark_imprimir_nombres_alturas(lista)
    while True:
        opcion = stark_menu_principal()
        if opcion == 1:
            stark_calcular_imprimir_heroe(lista,"max","altura")
        if opcion == 2:
            stark_calcular_imprimir_heroe(lista,"min","altura")
        if opcion == 3:
            stark_calcular_imprimir_promedio_altura(lista, "altura")
        if opcion == 4:
             stark_calcular_imprimir_heroe(lista, "max", "peso")
        if opcion == 5:
             stark_calcular_imprimir_heroe(lista, "min", "peso")
        if opcion == 6:
            break

def stark_normalizar_datos(lista):
    for e_lista in lista:
        if e_lista["altura"] != type(float()):
            e_lista["altura"] = float(e_lista["altura"])
        if e_lista["peso"] != type(float()):
            e_lista["peso"] = float(e_lista["peso"])
    if e_lista["altura"] == type(float()) or e_lista["peso"] == type(float()):
        print("Datos normalizados")

#01 A y B
def imprimir_heroes(lista:list, estado:str):
    if estado == "M":
        for e_lista in lista:
            if e_lista["genero"] == "M":
                print(e_lista["nombre"])
    if estado == "F":
        for e_lista in lista:
            if e_lista["genero"] == "F":
                print(e_lista["nombre"])
    if estado != "F" and estado != "M":
        return print(-1)

def calcular_maximo_minimo(lista:list, estado:str, clave:str, genero:str):
    minmax = lista[0]
    if estado == "max" and genero == "M":
        for e_lista in lista:
            if e_lista["genero"] == genero:
                if e_lista[clave] > minmax[clave]:
                    minmax = e_lista
    elif estado == "max" and genero == "F":
        for e_lista in lista:
            if e_lista["genero"] == genero:
                if e_lista[clave] > minmax[clave]:
                    minmax = e_lista
    elif estado == "min" and genero == "M":
        for e_lista in lista:
            if e_lista["genero"] == genero:
                if e_lista[clave] < minmax[clave]:
                    minmax = e_lista
    elif estado == "min" and genero == "F":
        for e_lista in lista:
            if e_lista["genero"] == genero:
                if e_lista[clave] < minmax[clave]:
                    minmax = e_lista
    if estado not in ["min", "max"] or genero not in ["F", "M"]:
        return print(-1)
    return minmax

def imprimir_superheroe(lista:list, estado:str, clave:str, genero:str):
    minmax = calcular_maximo_minimo(lista, estado, clave, genero)
    print("Superheroe {0}: {1} | {2} {3}".format(genero, minmax["nombre"], clave, minmax[clave]))

"""
def imprimir_heroe_m_mas_alto(lista:list):
    heroe_mas_alto = lista[0]
    for e_lista in lista:
        if e_lista["altura"] > heroe_mas_alto["altura"]:
"""