#Pregunta 2: Utilizando los métodos de property and Setter se requiere:
#Controlar los datos del empleado se hereden a la clase empleado salario
#Considere un método para calcular el salario con y sin horas extras imprima resultados
# Considere otro método para imprimir la información del empleado
# Considere 2 objetos para mostrar resultados

from empleado import Empleado

class EmpleadoSalario(Empleado):
    
    def __init__(self, ci, nombre, edad,valorhora,horastrabajo,horasextras):
        Empleado.__init__(self, ci, nombre, edad)
        self.valorhora=valorhora
        self.horastrabajo=horastrabajo
        self.horasextras=horasextras
    
    def __str__(self):
        #return Empleado.__str__(self.nombre,self.edad)
        return f"Nombre: {self.nombre} Edad: {self.edad}\nTotal Salario: {self.valorhora*self.horastrabajo}\nTotal Horas Extras: {self.horasextras}\nToal + Horas Extras: {self.valorhora*self.horastrabajo+self.horasextras}"
    def calcular_salario(self):
        salario = self.valorhora*self.horastrabajo
        return salario
            

    def imprimir(self):
        print("Nombre: {} Edad: {}".format(e1.nombre,e1.edad))
        print("Total Salario: ",e1.calcular_salario())
        print("Total Horas Extra: ",e1.horasextras)
        print("Total + Horas Extras: ",e1.calcular_salario() + e1.horasextras)

e1 = EmpleadoSalario('1714574801','Paul Rosales',27,2,260,65)
e1.imprimir()
print("***********************")
print(e1)
print("-----------------------")
e2 = EmpleadoSalario('1714574801','Juan Gutierrez',37,3,260,80)
print(e2)


#e1 = EmpleadoSalario('1714574801','Paul Rosales',27,1,520,65)


# Resultado Esperado

'''
Empleado 1:

Nombre:  Paul Rosales  Edad:  27
Total Salario: 520
Total horas Extras: 65
Total + Horas Extras: 585


Empleado 2:
'''



