from Input import *
from os import system

def crear_array(cantidad_elementos: int) -> list:
    """
    Crea una lista (arreglo) con la longitud especificada.

    Args:
        cantidad_elementos (int): Número de elementos que tendrá la lista.

    Returns:
        list: Lista creada, inicializada con valores None.
    """
    mi_arreglo = [None]*cantidad_elementos
    return mi_arreglo


def crear_matriz(cantidad_filas: int, cantidad_columnas: int,
                 valor_inicial: any) -> list:
    """
    Crea una matriz con las dimensiones especificadas,
    inicializada con un valor dado.

    Args:
        cantidad_filas (int): Número de filas de la matriz.
        cantidad_columnas (int): Número de columnas de la matriz.
        valor_inicial (any): Valor con el que se inicializarán todos los elementos de la matriz.

    Returns:
        list: Retorna Matriz creada.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def cargar_participantes(participantes: list) -> bool:
    """
    Solicita al usuario los nombres de los participantes, valida la entrada
    y actualiza la lista recibida con los nombres formateados en mayúsculas.

    Args:
        participantes (list): Lista de participantes que será actualizada
            con los nombres ingresados por el usuario. 

    Returns:
        bool: True si todos los nombres fueron cargados correctamente, False
        en caso de error o cancelación en la entrada de datos.
    """
    mensaje_error = (
    "-------------------------\n"
    "ERROR DE ENTRADA\n"
    "-------------------------\n"
    "- No se admiten caracteres especiales.\n"
    "- Longitud mínima: 3 caracteres\n"
    "- Longitud máxima: 20 caracteres\n"

    )
    if type(participantes) == list and len(participantes) > 0:
        retorno = True
        for i in range(len(participantes)):
            nombre = get_string(
                3, 20, mensaje_error, f"Ingrese el nombre del participante numero {i+1}: ", 3)
            if nombre == None:
                retorno = False
                break
            else:
                nombre = convertir_mayusculas(nombre)
                participantes[i] = nombre
    else:
        retorno = False
    return retorno


def cargar_puntuacion(participantes: list, matriz_puntuacion: list) -> bool:
    """
    Solicita al usuario ingresar las puntuaciones de cada participante evaluado
    por cada jurado. Con sus respectivas validaciones.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz_puntuacion (list): Matriz  que representa las
            puntuaciones de cada participante. 

    Returns:
        bool: True si todas las puntuaciones fueron ingresadas correctamente,
            False si se detectó un error en el ingreso
    """
    mensaje_error = (
    "-------------------------\n"
    "ERROR DE ENTRADA\n"
    "-------------------------\n"
    "- No se admiten caracteres especiales o letras\n"
    "- Rango esperado : numero ENTERO del 1-10 \n"

    )
    if type(matriz_puntuacion) == list and len(matriz_puntuacion) > 0:
        retorno = True
        for fil in range(len(matriz_puntuacion)):
            for col in range(len(matriz_puntuacion[fil])):
                dato = get_int(f"Ingrese la puntuacion de {participantes[fil]}, Jurado:  {col + 1} : ",
                mensaje_error, 1, 10, 3)
                if dato == None:
                    retorno = False
                    break
                else:
                    matriz_puntuacion[fil][col] = dato
            if retorno == False:
                break
    else:
        retorno = False
    return retorno


def sumar_fila(matriz: list, indice: int) -> int:
    """
    Calcula la suma de los elementos de una fila específica de la matriz.

    Args:
        matriz (list): Matriz de puntuaciones.
        indice (int): Índice de la fila a sumar.

    Returns:
        int: Resultado de la suma de la fila especificada.
    """
    suma_fila = 0
    for col in range(len(matriz[indice])):
        dato = matriz[indice][col]
        suma_fila += dato
    return suma_fila

def sumar_columnas(matriz: list, indice: int) -> int:
    """
    Calcula la suma de los elementos de una columna específica de la matriz.

    Args:
        matriz (list): Matriz con las puntuaciones.
        indice (int): Índice de la columna a sumar.

    Returns:
        int:  Resultado de la suma de la columna especificada.
    """
    suma_columna = 0
    for fila in range(len(matriz)):
        dato = matriz[fila][indice]
        suma_columna += dato
    return suma_columna

def calcular_promedio(parcial: int, total: int) -> int | float:
    """
    Calcula el promedio dividiendo un valor parcial por el valor total.

    Args:
        parcial (int): El valor total a dividir.
        total (int): El número por el cual se divide el total.

    Returns:
        int | float: El promedio calculado. El resultado puede ser
        un número entero o flotante.
    """
    promedio = parcial/total
    return promedio


def mostrar_participante(participantes: list, matriz_puntuacion: list, indice: int) -> bool:
    """
    Muestra en pantalla el nombre y las puntuaciones del participante
    en el indice ingresado, junto con su puntaje promedio calculado.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz_puntuacion (list): Matriz de puntuaciones.
        indice (int): Índice del participante a mostrar.

    Returns:
        bool: True si el índice es válido y la información se muestra
            correctamente, False si el índice es inválido.
    """
    retorno = False
    if indice >= len(participantes) or indice < 0:
        retorno = False
    else:
        retorno = True
        puntuacion_fila = sumar_fila(matriz_puntuacion, indice)
        promedio = round(calcular_promedio(puntuacion_fila, 3), 2)
        print(f"PARTICIPANTE: {participantes[indice]}")
        print(f"PUNTAJE JURADO 1 : {matriz_puntuacion[indice][0]}")
        print(f"PUNTAJE JURADO 2 : {matriz_puntuacion[indice][1]}")
        print(f"PUNTAJE JURADO 3 : {matriz_puntuacion[indice][2]}")
        print(f"PUNTAJE PROMEDIO : {promedio} / 10 \n")
    return retorno


def mostrar_todos_los_participantes(participantes: list, matriz_puntuacion: list) -> None:
    """
    Muestra en pantalla los datos de todos los participantes.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz_puntuacion (list): Matriz que contiene
            las puntuaciones de cada participante .

    Returns:
        None: No retorna nada ya que es una funcion para mostrar por pantalla.
    """
    for i in range(len(matriz_puntuacion)):
        mostrar_participante(participantes, matriz_puntuacion, i)


def verificar_promedio(participantes: list, matriz: list, promedio_verficar: int) -> bool:
    """
    Verifica y muestra los participantes cuyo puntaje promedio
    supere el valor especificado.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz (list): Matriz con las puntuaciones de cada participante.
        promedio_verficar (int): Valor límite de promedio a verificar.

    Returns:
        bool: True si al menos un participante supera el promedio especificado,
            False en caso contrario.
    """
    retorno = False
    for fil in range(len(matriz)):
        puntuacion_fila = sumar_fila(matriz, fil)
        promedio = round(calcular_promedio(puntuacion_fila, 3), 2)
        if promedio > promedio_verficar:
            print(f"PARTICIPANTE {participantes[fil]} con {promedio} / 10")
            retorno = True
    return retorno

def calcular_promedio_jurado(matriz: list, columna: int) -> int | float:
    """
    Calcula el promedio de las puntuaciones otorgadas por un jurado específico.

    Args:
        matriz (list): Matriz  de puntuaciones.
        columna (int): Índice de la columna (jurado) para la cual se desea calcular el promedio.

    Returns:
        int: Promedio de las puntuaciones del jurado especificado.
    """
    suma_puntajes = sumar_columnas(matriz, columna)
    promedio_jurado = calcular_promedio(suma_puntajes, 5)
    return promedio_jurado

def mostrar_jurado(matriz:  list, columna: int) -> None:
     """
    Muestra en pantalla el promedio de puntuación otorgado por un jurado específico.

    Args:
        matriz (list): Matriz de puntuaciones.
        columna (int): Índice del jurado (columna) para el cual se calculará el promedio.

    Returns:
        None. La información se imprime en pantalla.
     """
     promedio = round(calcular_promedio_jurado(matriz, columna),2)
     print(f"JURADO {columna+1}, promedio de puntuacion: {promedio} / 10")

def mostrar_jurados(matriz: list) -> bool:
    """
    Muestra en pantalla el promedio de puntuación otorgado por todos los jurados.

    Args:
        matriz (list): Matriz de puntuaciones.

    Returns:
        bool: True si la matriz es válida y se muestran los datos correctamente,
            False si la matriz está vacía.
    """
    retorno = True
    if len(matriz) > 0:
        cantidad_columnas = len(matriz[0])
        for col in range(cantidad_columnas):
            mostrar_jurado(matriz, col)
    else:
        retorno = False
    return retorno

def definir_jurado_mas_estricto (matriz: list) -> int:
    """
    Determina qué jurado tiene el promedio de puntuación más bajo.

    Args:
        matriz (list): Matriz de puntuaciones.

    Returns:
        int: Índice del jurado más estricto.
    """
    jurado = None
    promedio_minimo= None
    cantidad_columnas = len(matriz[0])
    for col in range(cantidad_columnas):
        puntuacion_columna = sumar_columnas(matriz, col)
        promedio = round(calcular_promedio(puntuacion_columna, 3), 2)
        if promedio_minimo == None:
            promedio_minimo = promedio
            jurado = col
        else:
            if promedio < promedio_minimo:
                promedio_minimo = promedio
                jurado = col
    return jurado

def convertir_mayusculas(cadena:str) -> str:
    """
    Convierte una cadena de texto a mayúsculas, utilizando el código ASCII
    para transformar las letras minúsculas a  mayúsculas.

    Args:
        cadena (str): La cadena de texto a convertir.

    Returns:
        str: Retorna la cadena convertida a mayúsculas.
    """
    longitud_cadena = len(cadena)
    cadena_mayusc = ""
    for i in range (longitud_cadena):
        caracter_actual = cadena[i] 
        ascii = ord(caracter_actual)
        if ascii >= 97 and ascii <=122:
         mayuscula = ascii - 32
         cadena_mayusc += chr(mayuscula)
        else:
           mayuscula = ascii 
           cadena_mayusc += chr(mayuscula)

    return cadena_mayusc

def buscar_por_nombre(participantes: list, matriz: list, nombre:str) -> bool:
    """
     Busca un participante por su nombre y muestra su información si lo encuentra.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz (list): Matriz de puntuaciones.
        nombre (str): Nombre del participante a buscar.

    Returns:
        bool: True si se encontró y se mostró el participante, False si no se encontró.
    """
    nombre_mayusc = convertir_mayusculas(nombre)
    longitud = len(participantes)
    retorno = False
    for i in range(len(participantes)):
        actual = convertir_mayusculas(participantes[i])
        if nombre_mayusc == actual:
            mostrar_participante(participantes, matriz, i)
            retorno = True
            break
    return retorno

def intercambiar_elementos(array:list,izq:int,der:int) -> None:
    """
    Intercambia dos elementos en una lista dada sus posiciones.

    Args:
        array (list): Lista donde se realizará el intercambio.
        izq (int): Índice del primer elemento.
        der (int): Índice del segundo elemento.

    Returns:
        None: solo modifica el orden de la lista.
    """
    auxiliar = array[izq]
    array[izq] = array[der]
    array[der] = auxiliar



def listar_promedios(participantes: list, matriz_puntuacion: list) -> list:
    """
    Calcula y devuelve una lista con los promedios de puntuación de cada participante.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz_puntuacion (list): Matriz de puntuaciones.

    Returns:
        list: Lista de promedios (redondeados a 2 decimales) para cada participante.
    """
    longitud = (len(matriz_puntuacion))
    participantes_lista = crear_array(longitud)
    for i in range(len(matriz_puntuacion)):
        suma_puntos = sumar_fila(matriz_puntuacion,i)
        promedio = calcular_promedio(suma_puntos,3)
        participantes_lista [i] = round(promedio,2)
    return participantes_lista


def ordenar_participantes_por_promedio(participantes:list,matriz:list) -> None:
    """
    Ordena la lista de participantes de mayor a menor según su promedio de puntuaciones. 
     Tambien modifica la matriz de puntuaciones para no perder la correspondencia.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz (list): Matriz de puntuaciones.

    Returns:
        None: solo modifica el orden de las listas.
    """
    for izq in range(len(matriz) - 1):
        for der in range((izq + 1),len(matriz)):
            total_der = sumar_fila(matriz, der)
            total_izq = sumar_fila(matriz, izq)    
            promedio_izq =calcular_promedio(total_izq,3)
            promedio_der = calcular_promedio(total_der, 3) 
            if promedio_izq< promedio_der:
                intercambiar_elementos(participantes,izq,der)
                intercambiar_elementos(matriz,izq,der)

def mostrar_matriz_top_3(matriz: list,participantes : list) -> None:
    """
    Muestra en pantalla los tres participantes con mayor promedio de puntuaciones.

    Args:
        matriz (list): Matriz de puntuaciones.
        participantes (list): Lista de nombres de los participantes.

    Returns:
        None: Imprime datos por pantalla.
    """
    for fil in range(0,3):
         print(f"TOP {fil+1}")
         mostrar_participante(participantes,matriz,fil)    
    print(" ")

def ordenar_participantes_alfabeticamente(participantes:list,matriz:list) -> None:
    """
    Ordena alfabéticamente la lista de participantes, ajustando la matriz de puntuaciones
    para no perder la correspondencia.

    Args:
        participantes (list): Lista de nombres de los participantes.
        matriz (list): Matriz de puntuaciones.

    Returns:
        None: Modifica la lista.
    """
    for izq in range(len(participantes) - 1):
        for der in range((izq + 1),len(participantes)):        
            if participantes[izq] > participantes[der]:
                #Intercambiar sus nombres
                intercambiar_elementos(participantes,izq,der)
                intercambiar_elementos(matriz,izq,der)

def limpiar_pantalla():
    
    system("cls")