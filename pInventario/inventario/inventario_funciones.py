from datetime import datetime
from collections import Counter
#import __main__


def registrarProducto(lProductos,producto):
    lProductos.append(producto)
    #print(productos)

def mostrarDatosProducto(producto):
    print()
    print(f"ID: {producto['idProducto']}")
    print(f'Nombre: {producto["nombreProducto"]}')
    print(f'Descipcion: {producto["descripcionProducto"]}')
    print(f'Precio: {producto["precioProducto"]}')
    print(f'Cantidad: {producto["cantidadProducto"]}')


def buscarProducto(productos,idProducto):
    for p in productos:
        if p["idProducto"]==idProducto:
            return p
    return None

def realizarVenta(lventas,venta):
    venta['fecha']=datetime.now()
    lventas.append(venta)
    