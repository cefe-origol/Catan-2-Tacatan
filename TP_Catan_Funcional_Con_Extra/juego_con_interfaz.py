from clases import Jugador
from interfaz import jugar_con_interfaz
from tablero import TableroCatan
from juego import *

#Lista de jugadores
jugadores = [Jugador("jose", (255,0,125)),Jugador("pepe", (0,255,125)),Jugador("Alstolfo", (100,0,125)),Jugador("Josefa", (255,0,200))]
#Tablero
tablero_a_jugar = None

tablero_a_jugar = TableroCatan()
rellenar_tablero(tablero_a_jugar)

#No se olviden de rellenar el tablero!
jugar_con_interfaz(jugadores,tablero_a_jugar)