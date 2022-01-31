from notas import Note
from notebook import Book

# note = Note('soy el titulo', 'este es el mensage', 0)

# note2 = Note('secont title', 'message', 1)

# notebook = Book()

# notebook.create_note(note.get_note())

# notebook.create_note(note2.get_note())

# print(notebook.get_all_notes())

finish = True  # estado inicial
# finish = False # termino del siclo

print('Bienbenido al programa de notas')


def ver_instrucciones() -> bool:
    seccion = input(
        'coloca 1 si quieres ver incrucciones de uso, de lo contrario coloca 0: ')
    if(seccion == "1"):
        return True
    else:
        return False


def tutorials():
    print(
        '''
          -Si requiere ver la lista de comandos que puede utilizar escriba "help"
        -Si quiere escribir una nota escriba "create".
        --- se le pedira el titulo despues el mensage y por ultimo el tipo ("categoria") a la que pertenece la nota.
        -Si desea eliminar una nota escriba "delete".
        --- despues se le pedira que agrege ya sea la pocicion de la nota, el titulo o el tipo de nota
        --- haciendo esto el programa intentara traer la nota o notas que coincidan con lo proporcionado.
        --- despues solo tiene que agregar el numero de la pocicion de la nota que quiera editar
        -Si desea actualizar una nota escriba "update".
        --- despues se le pedira que agrege ya sea la pocicion de la nota, el titulo o el tipo de nota
        --- haciendo esto el programa intentara traer la nota o notas que coincidan con lo proporcionado.
        --- despues solo tiene que agregar el numero de la pocicion de la nota que quiera editar
        -Si desea ver la lista total de notas esritas escriba "all_notes".
        -Si requiere ver el contenido de una nota en espesifico escriba "get_note".
        --- despues se le pedira que agrege ya sea la pocicion de la nota, el titulo o el tipo de nota
        --- haciendo esto el programa intentara traer la nota o notas que coincidan con lo proporcionado.
        --- despues solo tiene que agregar el numero de la pocicion de la nota que quiera ver
        ''')


def comand_help():
    MESSAGE_HELP = '''
     lista de comandos:
        -Si requiere ver la lista de comandos que puede utilizar escriba "help"
        -Si quiere escribir una nota escriba "create".
        -Si desea eliminar una nota escriba "delete".
        -Si desea actualizar una nota escriba "update".
        -Si desea ver la lista total de notas esritas escriba "all_notes".
        -Si requiere ver el contenido de una nota en espesifico escriba "get_note".
    '''
    print(MESSAGE_HELP)


instrucciones = ver_instrucciones()

if(instrucciones):
    print(
        '''
        Este programa de consola sirve para crear, editar, consultar y eliminar notas;
        -Se le preguntara el titulo de la nota a guardar,
         asi como el contenido de la misma y el tipo de nota a la que esta pertenece.
        -para continuar coloca 1, si quieres terminar el tutorial coloca 0  
    '''
    )
    continuar = input(
        '-para continuar escreba 1, si quieres terminar el tutorial escribe 0: ->')

    if(int(continuar) == 1):
        tutorials()
        print('Gracias por finalizar este tutorial')


while(finish):
    comand = input('que desea hacer: ')
    notebook = Book()
    list_comand = ['help', 'create', 'update', 'delete', 'all_notes']

    if(comand == "help"):
        comand_help()

    if(comand == "create"):
        title = input('coloca un titulo a tu nota: ')
        message = input('coloca el contenido de tu nota: ')
        type_nota = input('coloca el tipo o categoria de la nota: ')
        nota = Note(title, message, type_nota)
        notebook.create_note(nota.get_note())
        pass

    if(comand == "update"):
        pass

    if(comand == "delete"):
        pass

    if(comand == "all_notes"):
        pass

    if(comand == "get_note"):
        print(notebook.get_all_notes())
        pass

    comando_invalido = comand not in list_comand

    if(comando_invalido):
        print('comando invalido vuelbe a intentarlo')
