import random
from clases import Asentamiento, Camino


ORDEN_ESPECIAL = True

def tirar_dados(): # devuelve la suma de dos dados aleatorios
    return random.randint(1,6) + random.randint(1,6)

def rellenar_tablero(_tablero):
    tablero = []
    offsets = { 'Ladrillo': 3, 'Piedra': 3, 'Trigo': 4, 'Lana': 4, 'Madera': 4} # 'recurso':cantidad
    for recurso in offsets:
        tablero+=[recurso]*offsets[recurso] # agregar los recursos por la cantidad del mismo ej: 'ladrillo':3 -> ['ladrillo','ladrillo','ladrillo']

    random.shuffle(tablero) # desordeno el tablero

    _fichas = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    random.shuffle(_fichas)

    for pos in range(len(tablero)): # iterar desde el 0 al 17 (18)
        tablero[pos] = tablero[pos],_fichas[pos] # a cada casilla del tablero le asigno una ficha ej: 'ladrillo' -> ['ladrillo', 2]
    
    tablero.insert(9, ('Desierto', 1)) # agregamos el desierto en el medio (9) 


    for i in range(1,20):
        _tablero.colocar_recurso(i, tablero[i-1][0])
        _tablero.colocar_numero(i, tablero[i-1][1])


def jugar_catan(jugadores,tablero):
    
    for jugador in jugadores:
        comando = input("Coloque primer asentamiento: ").split()
        ficha = int(comando[0])
        vertice = int(comando[1])
        tablero.colocar_asentamiento(ficha,vertice, Asentamiento(jugador))

        comando = input("Coloque primer camino: ").split()
        ficha = int(comando[0])
        vertice = int(comando[1])
        tablero.colocar_camino(ficha, vertice, Camino(jugador))

    for jugador in reversed(jugadores):
        comando = input("Coloque segundo asentamiento: ").split()
        ficha = int(comando[0])
        vertice = int(comando[1])
        tablero.colocar_asentamiento(ficha,vertice, Asentamiento(jugador))
        
        comando = input("Coloque segundo camino: ").split()
        ficha = int(comando[0])
        vertice = int(comando[1])
        tablero.colocar_camino(ficha, vertice, Camino(jugador))

    while(True):
        for jugador in jugadores:
            dados = tirar_dados()
            for n in range(1,20):
                ficha = tablero.obtener_numero_de_ficha(n)
                if(ficha == dados):
                    asentamientos = tablero.asentamientos_por_ficha(n)
                    for asentamiento in asentamientos:
                        recurso = tablero.obtener_recurso_de_ficha(n)
                        asentamiento.jugador.AgregarRecurso(recurso, 1)

            while(True):
                comando = input("Comando: ").split()
                if comando[0] == "pas":
                    break
                elif comando[0] == "fin":
                    return
                elif comando[0] == "ase":
                    ficha = int(comando[1])
                    vertice = int(comando[2])
                    if(jugador.madera >= 1 and jugador.ladrillo >= 1 and jugador.lana >= 1 and jugador.trigo >= 1):
                        tablero.colocar_asentamiento(ficha, vertice, Asentamiento(jugador))
                        jugador.madera -= 1
                        jugador.ladrillo -= 1
                        jugador.lana -= 1
                        jugador.trigo -= 1
                elif comando[0] == "cam":
                    ficha = int(comando[1])
                    vertice = int(comando[2])
                    if(jugador.madera >= 1 and jugador.ladrillo >= 1):
                        tablero.colocar_camino(ficha, vertice, Camino(jugador))
                        jugador.madera -= 1
                        jugador.ladrillo -= 1
            
           

                

        
        

