from pymongo import MongoClient



# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Database']

# ---------------------------------------- CRUD ----------------------------------------

# Crear
def insertar(nombreJugador, idJugador):
    documento = {
        'Player': nombreJugador,
        'Player ID': idJugador
    }
    resultado = db['vct'].insert_one(documento)
    return resultado.inserted_id

# Leer
def Leer(idJugador):
    jugador = db['vct'].find({'Player ID': idJugador})
    for dato in jugador:
        print(dato)

# Actualizar
def actualizar(idJugador, Actualizado):
    resultado = db['vct'].update({'Player ID': idJugador}, {'$set': {'Player': Actualizado}})
    return resultado.modified_count

# Eliminar
def eliminar(idJugador):
    resultado = db['vct'].delete_many({'Player ID': idJugador})
    print(f'Jugador eliminado: {resultado.deleted_count}')

# ---------------------------------------------------------------------------------------

# interfaz por consola

def menu():
    print('1. Insertar un jugador')
    print('2. Leer un jugador')
    print('3. Actualizar un jugador')
    print('4. Eliminar un jugador')
    print('5. Cerrar')
    opcion = input('Ingrese una opción: ')
    return opcion

while True:
    opcion = menu()
    
    if opcion == '1':
        nombreJugador = input('Ingrese el nombre del jugador: ')
        idJugador = int(input('Ingrese el ID del jugador: '))
        resultado = insertar(nombreJugador, idJugador)
        print(f'Jugador insertado con el ID: {resultado}')
    
    elif opcion == '2':
        
        idJugador = int(input('Ingrese el ID del jugador: '))
        jugador = Leer(idJugador)
        print(jugador)
        
    elif opcion == '3':
        idJugador = int(input('Ingrese el ID del jugador: '))
        Actualizado = input('Ingrese el nuevo nombre del jugador: ')
        resultado = actualizar(idJugador, Actualizado)
        print(f'Jugador actualizado: {resultado}')

    elif opcion == '4':
        idJugador = int(input('Ingrese el ID del jugador: '))
        resultado = eliminar(idJugador)
        print(f'Jugador eliminado: {resultado}')

    elif opcion == '5':
        break

    else:
        print('Opción no válida')    

