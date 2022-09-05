from interfaz import jugar_con_interfaz
from clases import Jugador
from tablero import TableroCatan

#Lista de jugadores
jugadores = [Jugador("TAW", (0,255,255)), Jugador("Mica", (0,0,0))]
#Tablero
tablero_a_jugar = TableroCatan()
#No se olviden de rellenar el tablero!
jugar_con_interfaz(jugadores,tablero_a_jugar)
