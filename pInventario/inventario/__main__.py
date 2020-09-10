
#from .inventario_funciones import registrarProducto , mostrarDatosProducto
from .inventario_funciones import registrarProducto ,mostrarDatosProducto,buscarProducto,realizarVenta

def mostrarMenu():
    print('1. Registrar un nuevo producto')
    print('2. Mostrar informacion de producto')
    print('3. Vender Producto')
    print('0. Salir')
    
def capturarEntero(mensaje):
    while True:
        try:
            numero=int(input(f'{mensaje}:'))
            return numero
        except ValueError:
            print('Error debe digitar un numero entero:')
        print()

def capturarFloat(mensaje):
    while True:
        try:
            numero=float(input(f'{mensaje}:'))
            return numero
        except ValueError:
            print('Error debe digitar un numero entero:')
        print()
    
def capturarCadena(mensaje):
    while True:
        try:
            nombre=str(input(f'{mensaje}:')).strip()
            return nombre
        except ValueError:
            print('Error debe digitar una cadena:')
        print()
def listarProductos(productos):
    for p in productos:
        print(f"{p['idProducto']} -- {p['nombreProducto']}-- {p['cantidadProducto']}")

def continuar():
    print()
    print('Presione enter para continuar...', end='')
    input()
    print()

def main():
    while True:
        while True: #controla la validacion
            try:
                mostrarMenu()
                opcion = int(input('Ingese la opcion: '))
                if 0<= opcion <= 5:
                    break
                else:
                    print("El vaor debe estar entre 1 y 5")

            except ValueError:
                print()
                print('Error: Debe digitar un numero entero valido')
                
        if opcion==1:
            productos = []
            idProducto = capturarEntero('Digite el Id del producto')
            if idProducto > 0:
                producto = (productos,idProducto)
                if idProducto is None:
                    break
            else: 
                print("El numero debe ser positivo")

            nombreProducto=capturarCadena('Digite el nombre del producto')
            descripcioProducto = capturarCadena('Digite la descripcion de producto')
            precioProducto = capturarFloat('Digite el precio del producto')
            cantidadProducto = capturarEntero('Digite la cantidad del producto')
            nuevoProducto = {'idProducto':idProducto , 'nombreProducto':nombreProducto, 'descripcionProducto':descripcioProducto,'precioProducto':precioProducto,'cantidadProducto':cantidadProducto}
            registrarProducto(productos,nuevoProducto)
            

        if opcion==2:
            mostrarDatosProducto(nuevoProducto)

        if opcion==3:
            ventas=[]
            while True:
                listarProductos(productos)
                idProducto=capturarEntero('digite el id del producto')
                producto = buscarProducto(productos,idProducto)
                if producto:
                    break
                else:
                    print("Debe escribir un id de producto existente")
            while True:
                cantidadProducto = capturarEntero('digite la cantidad del producto')
                if cantidadProducto>0:
                    if cantidadProducto <= producto['cantidadProducto']:
                        break
                    else:
                        print("No existe stock")

                else:
                    print()
                    print("Debe digitar un valor positivo")
            
            nuevaVenta = {'idProducto':idProducto,'cantidadProducto':cantidadProducto,'total':producto['precioProducto']*cantidadProducto}
            realizarVenta(ventas,nuevaVenta)
            print('Total $%.2f' %(nuevaVenta['total']*1.12))
            print()
            print('MENSAJE: La venta se realizao con exito')
        continuar()

if __name__ ==  '__main__':
    main()
    