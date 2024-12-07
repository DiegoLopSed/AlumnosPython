class CREDENCIAL():
    def __init__(self,USER,PASSWORD):
        self.USUARIO = USER
        self.COntrasena = PASSWORD
        pass

    def VALIDACION(self):
        user =''
        while user != self.USUARIO:
            
            user = input ('USUARIO:')
            if user == self.USUARIO:
                password=''
                while password != self.COntrasena:
                    password = input ('CONTRASEÑA:')
                    if password == self.COntrasena:
                        print('ACCESO CONCEDIDO')
                    else:
                        print('CONTRASEÑA INCORRECTA, INTENTE DE NUEVO')
            else:
                print('USUARIO NO EXISTENTE')
        
USER1 = CREDENCIAL('Alexys','1234')
USER1.VALIDACION()