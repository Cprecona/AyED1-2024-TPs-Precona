def guardar_nacionalidad()-> None:
    '''
    Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
    ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
    terminados en "EZ". Descartar el resto. Ejemplo:
    Arslanian, Gustavo:  ARMENIA.TXT
    Rossini, Giuseppe:  ITALIA.TXT
    Pérez, Juan: ESPAÑA.TXT
    Smith, John: descartar
    
    Pre: el archivo de nombres debe estar previamente creado para su lectura.

    Post: no devuelve nada, sino que crea los archivos.
    '''

    separador = ","
    try:
        with open('TP0601/personas.txt','rt',encoding='utf-8') as archivo_personas:
            linea = archivo_personas.readline()
            while True:
                linea = archivo_personas.readline()
                if not linea:
                    break
                apellidos,nombres = linea.strip().split(separador)
                if apellidos.endswith("ian"):
                    with open('ARMENIA.TXT','wt',encoding='utf-8') as armenia:
                        armenia.write(f"{apellidos},{nombres}\n")
                elif apellidos.endswith("ini"):
                    with open('ITALIA.TXT','wt',encoding='utf-8') as italia:
                        italia.write(f"{apellidos},{nombres}\n")
                elif apellidos.endswith("ez"):
                    with open('ESPAÑA.TXT','wt',encoding='utf-8') as espania:
                        espania.write(f"{apellidos},{nombres}\n")
                else:
                    continue
    except FileNotFoundError as msg:
        print(f"El achivo no fue encontrado: {msg}")
    except:
        print(f"Error en los datos")
    else:
        print(f"\nArchivos leídos y creados existosamente")

def main()-> None:
    ''' Este es el programa principal
    Solamente llama a la función guardar_nacionalidad'''

    guardar_nacionalidad()

if __name__ == "__main__":
    main()



