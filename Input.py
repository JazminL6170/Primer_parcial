from Validate import *

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, 
    reintentos: int) -> int| None:
    """
    Solicita al usuario un número entero dentro de un rango determinado, con intentos limitados.

    Parámetros:
    mensaje (str): Mensaje para solicitar el número al usuario.
    mensaje_error (str): Mensaje de error a mostrar si la entrada no es válida.
    minimo (int): Valor mínimo aceptado.
    maximo (int): Valor máximo aceptado.
    reintentos (int): Número máximo de intentos permitidos.

    Retorna:
    int | None: El número ingresado como int si es válido, o None si se agotaron los intentos.
    """

    contador = 1
    dato = None
    bandera = False

    while  contador <= reintentos and bandera == False:
        numero = (input(mensaje))
        
        if validate_number(numero, minimo, maximo):
            dato = int(numero)
            bandera = True
        else:
           intentos_restantes = reintentos - contador
           print(f"{mensaje_error} * Intentos restantes: {intentos_restantes} * \n")
           contador += 1
    return dato

            
def get_string(longitud_minima: int,longitud_maxima: int, mensaje_error: str,
    mensaje:str, reintentos: int)-> str| None:
    """
    Solicita al usuario una cadena de texto que cumpla 
    con ciertas restricciones de longitud y caracteres, con intentos limitados.

    Parámetros:
    longitud_minima (int): Longitud mínima permitida para la cadena.
    longitud_maxima (int): Longitud máxima permitida para la cadena.
    mensaje_error (str): Mensaje de error a mostrar si la cadena no es válida.
    mensaje (str): Mensaje para solicitar la cadena al usuario.
    reintentos (int): Número máximo de intentos permitidos.

    Retorna:
    str | None: La cadena ingresada si es válida, o None si se agotaron los intentos.
    """

    contador = 1
    validacion = None
    bandera = False

    while  contador <= reintentos and bandera == False:
      frase = input(mensaje)

      if validate_length(frase, longitud_minima, longitud_maxima):
          validacion = frase
          bandera = True
      else:
           intentos_restantes = reintentos - contador
           print(f"{mensaje_error} * Intentos restantes: {intentos_restantes} * \n")
           contador += 1

    return validacion

    