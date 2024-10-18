from random import randint

def adivinar_numero() -> None:
    '''Genera un número al azar entre 1 y 500. Le pide al usuario que ingrese un 
    número con la idea que adivine el generado automáticamente.
    Cada vez que se introduce un número se mostrará un mensaje indicando
    si el número que tiene que adivinar es menor o mayor al ingresado.
    Cuando consiga adivinarlo hay que imprimir por pantalla la cantidad de intentos.
    Si el usuario introduce algo que no sea un número se mostrará un mensaje y se
    lo tomará como un intento más.

    Pre: se le pide al usuario un número entero,

    Post: no devuelve nada.    
    '''

    numero = randint(1,500)
    intentos = 0
    while True:
        try:
            apuesta = int(input("Ingrese el número que cree que salió entre 1 y 500: "))
            intentos +=1
        except:
            print("El dato ingresado no es un número")
        else:
            if apuesta == numero:
                print("¡Adivinó!")
                print(f"La cantidad de intentos fue {intentos} ")
                break
            else:
                if apuesta > numero:
                    print("El número ingresado es mayor al número a adivinar")
                else:
                    print("El número ingresado es menor al número a adivinar")
            

adivinar_numero()
