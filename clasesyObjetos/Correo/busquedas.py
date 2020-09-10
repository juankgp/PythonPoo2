import datetime
ultima_id =0
class Validaciones:
    def __init__(self):
        self.user = "juank@gmail.com"
        self.password = "jkjkjk"
       
    def valida(self , user , password):    
        if (self.user == user and self.password == password):
            return True
        else:
            return False

    def capturarCorreo(self,mensaje):
        haya = False
        hayp = False
        while True:
            correo = input(f"{mensaje}")
            for p in correo:
                if p == "@":
                    haya = True
                if p == ".":
                    hayp = True
            if haya == True and hayp == True:
                return correo
            else:
                print("-------------Correo incorrecto vuelva a intentar-----------------a")
class Correo:
    def __init__(self,destinatario,asunto,correo):
        self.destinatario = destinatario
        self.asunto = asunto
        self.correo = correo
        self.fechaEnvio = datetime.datetime.today()
        global ultima_id 
        ultima_id += 1
        self.id = ultima_id
    def match(self,filter):
        #determina si el correo concuerda con el filtro de texto
        #devuleve true si concuerda
        return filter in self.asunto or filter in self.destinatario
        
class Mail:
    def __init__(self):
        self.correos=[]

    def encontrarMail(self,correoId):
        for p in self.correos:
            if str(p.id) == correoId:
                return p
        return None
    
    def nuevoCorreo(self,destinatario,asunto,correo):
        self.correos.append(Correo(destinatario,asunto,correo))
    def buscar(self,filter):
        return[p for p in self.correos if p.match(filter)]
    def modificarAsunto(self,correoId,asunto):
        correo = self.encontrarMail(correoId)
        if correo:
            correo.asunto = asunto
            return True
        return False
    def modificarCorreo(self,correoId,correo):
        correo1 = self.encontrarMail(correoId)
        if correo1:
            correo1.correo = correo
            return True
        return False
    def borrarCorreo(self,correoId):
        correo2 = self.encontrarMail(correoId)
        if correo2:
            self.correos.remove(correo2)
            return True
        return  False
