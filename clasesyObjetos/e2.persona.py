class Persona:
    def __init__(self,nombre,edad,saldo):
        self.nombre=nombre
        self.edad=edad
        self.saldo=saldo
    def imprimir(self):
        print(f"Persona {self.nombre}")
        print(f"Edad {self.edad}")

    def incremento(self):
        self.edad=self.edad+1

    def transfer(self,persona,monto):
        if self.saldo >= monto:
            calculo = self.saldo-monto
            print(f"{persona.nombre}")
            #print(calculo)
            persona.saldo=calculo
            print("tranferencia Exitosa")
        else:
            print("Saldo insuficiente")

vpersona=Persona("Jose",19,1000)
vpersona.transfer(vpersona,300)
vpersona.incremento()
print("Saldo de cuenta")
print(vpersona.saldo)
#vpersona.imprimir()