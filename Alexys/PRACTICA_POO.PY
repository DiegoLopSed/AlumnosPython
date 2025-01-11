def MENU():
    objeto = OBJETO(usuario,contrasena)
    while True:
        print('1. Crear \n2. Leer \n3. Actualizar \n4.Eliminar \n5. salir')
        choice = input('Elija una opcion:\n')

        if choice == '1':
            usuario = input('INGRESE EL NUEVO USUARIO:')
            contrasena = input('INGRESE CONTRASEñA:')
            objeto.CREATE(usuario,contrasena)
        if choice == '2':
            OBJETO.READ(self= OBJETO)
        '''
        if choice == '3':
            OBJETO.UPTADE
        if choice == '4':
            OBJETO.DELETE
        if choice == '5':
            break
        '''     

class OBJETO:
    def __init__(self,CREDENCIAL,TIPO):
        self.TIPO = TIPO
        self.CREDENCIAL = CREDENCIAL
        self.USER = {}
        self.PASSWORD = {}
        pass

    def CREATE(self, usuario,contrasena):
        self.USER[str(usuario)] = usuario
        self.PASSWORD[str(contrasena)] = contrasena
        print(f'NUEVO USUARIO AGREGADO \nUsuario: {usuario} \n Contraseña: {contrasena}')
    def READ(self):
        for usuario, contrasena in self.USER.items() and self.PASSWORD.items():
            print(f'{usuario}:{contrasena}')
    #def UPTADE():

    #def DELETE():

MENU()

usuario1 = OBJETO('LALO','123')
'''
objeto = usuario & contraseña 

objeto input

usuario = input

contrasena = input

objeto.OBJETO(usuario,contrasena)
'''

