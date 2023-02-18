cantidadProducto=int(input("ingrese la cantidad de productos comprados "))
total=cantidadProducto*10000
print("el total a pagar es",total)
pago=int(input("ingrese valor que paga el cliente"))
resultado=pago-total
print("su cambio es",resultado)