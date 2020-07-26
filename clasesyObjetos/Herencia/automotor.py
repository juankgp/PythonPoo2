class  Automotor():
    def __init__(self,tipoMotor,potencia):
        self.tipoMotor = tipoMotor#input("Ingrese el tipo de combustible")
        self.potencia = potencia
    def __str__(self):
        return " con motor {}, una potenicia de {}".format(self.tipoMotor , self.potencia)

class Automovil():
    def __init__(self,numeroRuedas,modelo,color):
        self.numRuedas = numeroRuedas#int(input("Ingrese el numero de ruedas"))
        self.modelo = modelo
        self.color=color
    def __str__(self):
        return "{} ruedas , es modelo {},  de color {}".format(self.numRuedas,self.modelo,self.color)

class Moto(Automovil,Automotor):
    def __init__(self,numRuedas,modelo,color,tipoMotor,potencia,tipoAcelerador,numMarchas):
       Automovil.__init__(self,numRuedas,modelo,color)
       Automotor.__init__(self,tipoMotor,potencia)
       self.tipoAcelerador = tipoAcelerador
       self.numMarchas = numMarchas
    
    def __str__(self):
        return "Su moto tine " + Automovil.__str__(self) + Automotor.__str__(self) + " con un tipo de acelerador {} y {} marchas".format(self.tipoAcelerador,self.numMarchas)


moto = Moto(2,2020,"Negro","Elctrico","5KW","electronico",0)
#moto.present()
print(moto)

