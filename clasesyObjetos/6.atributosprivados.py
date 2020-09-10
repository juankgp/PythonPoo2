#atributos privados ("__")
#puede ser accedido por la misma clase y subclases
class usuario(object):
    def __init__(self,nombre,clave):
        self.nombre=nombre
        self.__clave=clave

vusuario=usuario("juank","jkjkjk")