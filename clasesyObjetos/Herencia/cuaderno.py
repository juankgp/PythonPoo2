import datetime
ultima_id =0
class Nota:
    def __init__(self, memo , tags=''):
        self.memo=memo
        self.tags=tags
        self.creacion_fecha=datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id=ultima_id
    def match(self,filter):
        #determina si esta nota concuerda con el filtro de texto
        #devuleve true si concuerda
        return filter in self.memo or filter in self.tags

        
class Cuaderno:
    def __init__(self):
        self.notas=[]

    def nueva_nota(self,memo,tags=''):
        self.notas.append(Nota(memo,tags))

    def encontrar_nota(self,notaid):
        #localizar la nota en el diccionario
        for nota in self.notas:
            if str(nota.id) == notaid:
                return nota
            return None
    def modificar_memo(self,nota_id,memo):
        #cambiar el valor del memo
        nota = self.encontrar_nota(nota_id)
        if nota:
            nota.memo = memo
            return True
        return False
    
    def modificar_tags(self,nota_id,tags):
        #cambiar el valor del memo
        nota = self.encontrar_nota(nota_id)
        if nota:
            nota.tags = tags
            return True
        return False

    def buscar(self,filter):
        #buscar las que concuerdan con un filtro
        return[nota for nota in self.notas if nota.match(filter)]
