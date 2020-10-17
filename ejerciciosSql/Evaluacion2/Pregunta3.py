#Pregunta 3: Un cliente realiza un prestamo. La cantidad inicial solicitada es de 2 dólares, 
# El operario cometió un error de digitación y debe eliminar la cantidad e ingresar la correcta
# Si el valor del prestamo supera los 2500 , se genera un interes que debe ser enviado por el método setter
# Los resultados deben ser muy similares a los esperados
# El ejercio debe utilizar los metodos de @property and setter para mostrar los resultados

class Prestamo:

    def __init__(self, nombres, valor, interes):
        self._nombres = nombres
        self._valor = valor
        self._interes = interes

  
    @property
    def nombres(self):
        return self._nombres
    
    @nombres.setter
    def nombres(self, nombres):
        self._nombres = nombres
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self,valor):
        self._valor=valor

    @valor.setter
    def prestInicial(self,valor):
        self._valor=valor
        print("Valor Prestamo Inicial: ",self._valor)
    @valor.setter
    def prestSoli(self,valor):
        self._valor=valor
        if valor > 2000:
            print("Interes Asignado Valor > 2000: % ",self.interes*100)    
        print("Valor Prestamo Solicitado: ",self._valor)
        if valor > 2000:
            print("Precio con Interes: ",self.valor*self.interes+self.valor)
        else:
            print("Precio sin Interes: ",self.valor)

    @valor.deleter
    def valor(self):
        print("Borrando valor..")
       

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nuevo_interes):
        self._interes = nuevo_interes
    @interes.setter
    def intInicial(self, int_ini):
        self._interes = int_ini
        print("Interes Inicial: ",self.interes)
  
        
 

vprestamo=Prestamo("Cliente : Paul Gonzales",2,0) # envio el cliente, valor e interes inicial
#del vprestamo.valor
print(vprestamo.nombres)
vprestamo.prestInicial=300
vprestamo.intInicial=0
vprestamo.interes=0.12
vprestamo.prestSoli=2500

#Resultados Esperados

'''
Cliente : Paul Gonzales
Valor Prestamo Inicial:  300
Interes Inicial:  0
Interes Asignado Valor > 2000: % 12
Valor Prestamo Solicitado:  2500
Precio con Interes:  2800.0
'''