def validar_numero_natural() -> int:
    '''Recibe por teclado un número y valida si es natural o no,
    indicando la naturaleza exacta del error.

    Pre: el número se ingresa por teclado.

    Post: devuelve el número sólo si es váido.
    '''

    while True:
        numero = input("Ingrese un número natural: ")
        try:
            salida = float(numero)
            assert salida > 0, 'No puede ser menor o igual que cero'
            assert salida == int(salida) , 'No puede ser un flotante. Ingrese un entero'
        except ValueError:
            print(f"{numero} no es un número")
        except AssertionError as mensaje:
            print(mensaje)
        else:
            return int(salida)
        
    
# Programa de comprobación

numero = validar_numero_natural()
print(f"El número ingresado es {numero}")

