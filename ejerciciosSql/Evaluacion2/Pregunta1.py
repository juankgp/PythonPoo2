
#PREGUNTA 1 : Clases y Objetos
#De acuerdo al ejercicio propuesto, se solicita mediante 2 objetos instanciar las clases y mostrar resultados 
# similares a la pantalla esperada. Considere imprimir el total final por la venta del producto

class Producto:

    def __init__(self, codigo,nombre,descripcion , presentacion, precio,cantidad):
        self.codigo=codigo
        self.nombre=nombre
        self.descripcion=descripcion
        self.presentacion=presentacion
        self.precio=precio
        self.cantidad=cantidad
        
    def imprimir(self):
        print("_________________________")
        print ("Codigo :", self.codigo)
        print ("Nombre :", self.nombre)
        print ("Descripción :", self.descripcion)
        print ("Presentación :", self.presentacion)
        print ("Precio : $", self.precio)
        print ("Cantidad Solicitada : $", self.cantidad)
        print("Total final:",self.total)
        
    def tipo_producto(self, nombre,p1,p2,p3):
        lista={"Lacteos":p1,"Jugos":p2,"Galletas":p3}
        print(" Stock por tipo de Productos \n")
        for m, n in lista.items():
            if (n < 7):
                
                print ("  :", m, " Total Stock: ", n)

        

    def control_venta(self, producto1, cantidad):
        self.total=producto1*cantidad
        print("")
        

p1 = Producto('1','Yogurth','De Fresa','250ml',7,2)
p1.tipo_producto('Stock',2,6,5)
p1.control_venta(p1.precio,p1.cantidad)
p1.imprimir()

p2 = Producto('2','Jugo Pera','Sabor a Pera sin Azucar','1 litro',2.5,5)
p2.control_venta(p2.precio,p2.cantidad)
p2.imprimir()

# Salida de Pantalla esperada
'''
 Stock por tipo de Productos 

  : Lacteos  Total Stock:  2
  : Jugos  Total Stock:  6
  : Galletas  Total Stock:  5
_________________________
Codigo : 1
Nombre : Yogurt
Descripción : De fresa
Presentación : 250 ml
Precio : $ 7
Cantidad Solicitada : 2
Total final : 14
_________________________
Codigo : 2
Nombre : Jugo Pera
Descripción : Sabor a Pera sin Azucar
Presentación : 1 litro
Precio : $ 2.5
Cantidad Solicitada : 5
Total final : 12.5
 
  '''