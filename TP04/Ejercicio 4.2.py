import shutil

def obtener_ancho_pantalla() -> float:
    '''Devuelve el ancho de la pantalla de la terminal.

    Pre: a importar la librería shutil.

    Post: devuelve el ancho como un número flotante.
    '''
    ancho, alto = shutil.get_terminal_size()
    
    return ancho


def centrar_cadena(cadena:str) -> str:
    '''Devuelve una cadena de caracteres centrada.
    
    Pre: ingresar una cadena.

    Post: devuelve la cadena por pantalla en forma centrada.
    '''
    ancho = obtener_ancho_pantalla()
    cadena_centrada = cadena.center(ancho)
    print(cadena_centrada)


# programa

centrar_cadena("Este es un ejemplo de una cadena de texto que tiene exactamente ochenta caracteres.")
