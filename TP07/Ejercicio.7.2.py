import sys

sys.setrecursionlimit(2000)


def convertir_a_decimal(num: int, potencia: int, resultado: int) -> int:
    """Desarrollar una función que reciba un número binario y lo devuelva convertido a
    base decimal.

    """
    if num == 0:
        return resultado
    elif num % 10 == 0:
        resultado += 0 * 2**potencia
        return convertir_a_decimal(num // 10, potencia + 1, resultado)
    else:
        resultado += 1 * 2**potencia
        return convertir_a_decimal(num // 10, potencia + 1, resultado)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    convertir_a_decimal y le pasa el número, la potencia y el resultado
    como parámetros.

    """
    numero_convertido = convertir_a_decimal(10101100, 0, 0)
    print(numero_convertido)


if __name__ == "__main__":
    main()
