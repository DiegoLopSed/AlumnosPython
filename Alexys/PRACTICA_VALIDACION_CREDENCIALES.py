class CREDENCIAL():
    def __init__(self,USER,PASSWORD):
        self.USUARIO = USER
        self.CONTRASENA = PASSWORD
        pass


class VALIDACION():
    def __init__(self):
        self.USUARIO = []
        pass

    def  REGISTRO_USUARIO(self,CREDENCIAL):
        self.USUARIO.append(CREDENCIAL)
        
    def VALIDACION(self):
        user =''
        while user != self.USUARIO:
            
            user = input ('USUARIO:')
            if user == self.USUARIO:
                password=''
                while password != self.CONTRASENA:
                    password = input ('CONTRASEÑA:')
                    if password == self.CONTRASENA:
                        print('ACCESO CONCEDIDO')
                    else:
                        print('CONTRASEÑA INCORRECTA, INTENTE DE NUEVO')
            else:
                print('USUARIO NO EXISTENTE')
        
USER1 = CREDENCIAL('Alexys','123')
USER2 = CREDENCIAL('Diego','456')
USER3 = CREDENCIAL('Luis','789')

