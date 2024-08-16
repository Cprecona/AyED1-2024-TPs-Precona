totalCompra = int(input("Ingrese el total de la compra: "))
totalDinero = int(input("Ingrese el dinero recibido: "))

diferencia = totalDinero - totalCompra

cant5000 = diferencia // 5000
diferencia = diferencia % 5000
cant1000 = diferencia // 1000
diferencia = diferencia % 1000
cant500 = diferencia // 500
diferencia = diferencia % 500
cant100 = diferencia // 100
diferencia = diferencia % 100
cant50 = diferencia // 50
diferencia = diferencia % 50
cant10 = diferencia // 10

if totalCompra > totalDinero:
    print("Dinero insuficiente")
else:
    print("El vuelto es: ", cant5000, "billetes de 5000, ", cant1000, "billetes de 1000, ", cant500, "billetes de 500, ", cant100, "billetes de 100, ", cant50, "billetes de 50 y ", cant10,"billetes de 10")
