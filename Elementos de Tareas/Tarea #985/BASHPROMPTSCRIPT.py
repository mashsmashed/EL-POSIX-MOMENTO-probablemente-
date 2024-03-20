import os as PC
import time

BASHUPDATE = 'tunuevalineadebash!(asegurate de vaciarme antes que nada)>'

def entrada_entero(lim1,lim2):
    while True:
        try:
            entrada = int(input('===>'))
        except ValueError: 
            print('...eso no es un numero')
        else:
            if lim1 <= entrada <= lim2:
                return entrada
            else:
                print('Inserta un valor valido')
    
def texto():

    global BASHUPDATE

    print('ingresa texto: \n\n===> ')
    text = input()
    print('elige el color de tu texto:')
    print('0- Negro')
    print('1- Rojo')
    print('2- Verde')
    print('3- Naranja')
    print('4- Azul')
    print('5- Morado')
    print('6- Cian')
    print('7- Gris claro')

    color = entrada_entero(0,7)

    print('te gustaria hacer el color mas claro?')
    print('1- si')
    print('2- no')

    colorint = entrada_entero(1,2)

    print('elige el color del fondo de tu texto:')
    print('0- Negro')
    print('1- Rojo')
    print('2- Verde')
    print('3- Naranja')
    print('4- Azul')
    print('5- Morado')
    print('6- Cian')
    print('7- Gris claro')
    print('8- ninguno')

    fondo = entrada_entero(0,8)

    if fondo != 8:
        print('te gustaria hacer el color mas claro?')
        print('1- si')
        print('2- no')

        fondoint = entrada_entero(1,2)

    print('Ahora, que aspecto quieres que tenga el texto?:')
    print('0- Ninguno')
    print('1- En negritas')
    print('2- Difuminado')
    print('3- En italicas')
    print('4- Subrayado')
    print('5- parpadeando!!!')

    effect = entrada_entero(0,5) 

    if colorint == 1:
        colorint = 9
    else:
        colorint = 3

    if fondo != 8:
        if fondoint == 1:
            fondoint = 4
        else:
            fondoint = 10
        BASHUPDATE = BASHUPDATE + "\033[" + str(colorint) + str(color) + ';' + str(fondoint) + str(fondo) + ';' + str(effect) + 'm' + text + '\033[0m'
    else:
        BASHUPDATE = BASHUPDATE + "\033[" + str(effect) + ';' + str(colorint) + str(color) + 'm' + text + '\033[0m'

def make_backup():

    bashfile = '/home/' + PC.getlogin()
    PC.chdir(bashfile)

    if PC.path.isfile('./.bashrc_backup') == True:
        print('respaldo encontrado! no veo por que hacer otro, verdad?')
    else:
        if PC.path.isfile('./.bashrc') == False:
            print('el directorio de .bashrc no existe... o no esta en donde se puede de hecho usar.')
        else:
            copycmd= 'cp .bashrc .bashrc_backup'
            print('encontrado! creando un respaldo...')
            PC.system(copycmd)
    time.sleep(2)

def restore_backup():

    bashfile = '/home/' + PC.getlogin()
    PC.chdir(bashfile)

    if PC.path.isfile('./.bashrc_backup') == True:
        print('respaldo encontrado! restaurando...')
        copybackup= 'cp .bashrc_backup .bashrc'
        PC.system(copybackup)

    else:
        print('el restauro de bashrc no se encontro... intenta remover el ULTIMO PS1=* del archivo de .bashrc')
    time.sleep(3)

def push_changes():

    global BASHUPDATE

    print("haciendo cambios...")
    time.sleep(4)
    bashfile = '/home/' + PC.getlogin()
    PC.chdir(bashfile)
    if PC.path.isfile('./.bashrc') == False:
        print('el directorio de .bashrc no existe... o no esta en donde se puede de hecho usar.')
        time.sleep(3)

    else:
        push= "echo \'PS1=\"" + BASHUPDATE + "\"\' >> ~/.bashrc"
        print(push)
        PC.system(push)
        print("Listo! tu nuevo prompt se ha agregado!")
        time.sleep(3)

def element_selector():

    global BASHUPDATE

    while True:
        PC.system('clear')
        print('tu linea nueva de bash: \n ')
        print(BASHUPDATE)
        print('\nque quieres hacer?')
        print('1- Anadir texto!!!')
        print('2- Reiniciar tu texto! (o vaciarlo, como quieras verlo)')
        print('3- Imprimir ayuda...')
        print('4- Terminar y actualizar!')
        print('5- Cancelar por completo...')
        print('===> ')
        opc = input()

        if opc == '1':

            texto()

        elif opc == '2':
        
            BASHUPDATE=''

        elif opc == '3':

            PC.system('clear')
            print('Poner /u en tu texto lo va a sustituir con el usuario del sistema.')
            print('Poner /H en tu texto lo va a sustituir con el nombre del sistema.')
            print('Poner /d en tu texto lo va a sustituir con la fecha del sistema.')
            print('Poner /n en tu texto hara que continue en una nueva linea.')
            print('Poner /w en tu texto lo va a sustituir con el directorio actual')
            print('Poner /A en tu texto lo va a sustituir con la hora del sistema en formato de 24 horas.')
            print('Poner /@ en tu texto lo va a sustituir con la hora del sistema en formato de 12 horas.')
            print('Los colores a estos tambien afectan al texto sustituido.')
            print('Hay muchas otras secuencias de escape, puedes intentar buscarlas!.')
            print('alternativamente, solo escribe el usuario que quieras que se muestre...')
            input('por cierto, presiona enter para salir de esta pantalla')

        elif opc == '4':

            push_changes()

        elif opc == '5':

            break

        elif opc == '6':
            print(BASHUPDATE)
            input('XDDD')

        else:

            print('LITERALMENTE TE ARRASTRARE AL MENU DE NUEVO POR METER ALGO INVALIDO')
            time.sleep(3)

while True:
    PC.system('clear')
    print("PROGRAMA QUE TE DEJA EDITAR EL PROMPT DE BASH!!!!!")
    print("Que quieres hacer primero?")
    print("")
    print("1- EDITAR EL PROMPT!!!")
    print("2- RESTAURAR EL PROMPT!!!")
    print("3- salir :c")

    opc = input()

    if opc == '1':
        print('en proceso...')
        make_backup()
        element_selector()
    elif opc == '2':
        restore_backup()
    elif opc == '3':
        print('ESPERO TE HAYA GUSTADO!!!\n\nPor cierto, para que tu nuevo prompt tome efecto, o reinicia la terminal o ejecuta "source .bashrc"')      
        break

    else:
        print('LITERALMENTE TE ARRASTRARE AL MENU DE NUEVO POR METER ALGO INVALIDO')
        time.sleep(3)

