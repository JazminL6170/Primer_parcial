def verificar_entero(numero:str) -> bool:
    """
    Verifica si una cadena representa un número entero positivo (sin signos ni puntos).

    Parámetros:
    numero (str): La cadena a verificar.

    Retorna:
    bool: True si la cadena representa un número entero positivo, False en caso contrario.
    """
    retorno = True
    cadena = str(numero)
    if len(cadena) == 0:
        retorno = False
    else:
        for i in range(len(cadena)):
         valor_ascii = ord(cadena[i])
         if valor_ascii > 57 or valor_ascii < 48:
            retorno = False
            break
    
    return retorno

def validate_number(numero: float, minimo: int, maximo: int) -> bool:
    """
    Verifica si el número ingresado es un entero positivo dentro de un rango especificado.

    Parámetros:
    numero (float): El número a validar.
    minimo (int): Valor mínimo permitido.
    maximo (int): Valor máximo permitido.

    Retorna:
    bool: True si el número es un entero válido dentro del rango, False en caso contrario.
    """
    bandera = False
    es_valido = verificar_entero(numero)
    if es_valido == True:
       numero = int(numero) 
       if (numero >= minimo and numero <= maximo):
           bandera = True

    return bandera

def verificar_nombre(nombre: str ) -> bool:
    """
    Verifica si un nombre es válido, es decir, contiene solo letras (mayúsculas o minúsculas) y espacios.

    Parámetros:
    nombre (str): El nombre a verificar.

    Retorna:
    bool: True si el nombre es válido, False si contiene caracteres no permitidos.
    """
    es_valido = True
    longitud = len(nombre)
    for i in range (0,longitud):
        caracter = nombre[i]
        ascii = ord(caracter)
        if (ascii >= 65 and ascii <=90) or (ascii >= 97 and ascii <=122):
            continue
        elif ascii == 32:
             continue
        else:
            es_valido = False
            break
    return es_valido


def validate_length(frase: str, minimo: int, maximo: int) -> bool:
    """
    Verifica si la longitud de una cadena está dentro de un rango permitido y si contiene solo letras y espacios.

    Parámetros:
    frase (str): La cadena a validar.
    minimo (int): Longitud mínima permitida.
    maximo (int): Longitud máxima permitida.

    Retorna:
    bool: True si la longitud es válida y la cadena contiene solo letras y espacios, False en caso contrario.
    """
    longitud = len(frase)
    bandera = False
    nombre_valido = verificar_nombre(frase)
    if (minimo <= longitud <= maximo) and nombre_valido == True:
        bandera = True

    return bandera
        
