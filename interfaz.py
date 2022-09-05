import pygame
from math import pi,cos,sin
import numpy as np
import threading
import juego
import time
import queue
from clases import Asentamiento,Ciudad

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

colors_per_resource = {
    "Ladrillo": pygame.Color("#dc5539"),
    "Trigo"   : pygame.Color("#ebbd68"),
    "Madera"  : pygame.Color("#5d2906"),
    "Piedra"  : pygame.Color("#888c8d"),
    "Lana"    : pygame.Color("#7ec850"),
    "Central" : (255,255,255),
}
white = (255,255,255)
black = (0,0,0)
thief_color = (48,48,48)

def draw_hexagon(surface, border_color,fill_color, radius, position, width=0):
    n, r = 6, radius
    x, y = position
    #Fill
    pygame.draw.polygon(surface, fill_color, [
        (x + r * cos(2 * pi * (i +0.5) / n), y + r * sin(2 * pi * (i +0.5) / n))
        for i in range(n)
    ], 0)
    #Border
    pygame.draw.polygon(surface, border_color, [
        (x + r * cos(2 * pi * (i +0.5) / n), y + r * sin(2 * pi * (i+0.5) / n))
        for i in range(n)
    ], width)

def draw_thief(position,screen):
    x,y = position
    thief_width = 18
    thief_head_radius = 12/2
    pygame.draw.rect(screen,thief_color,pygame.Rect(x - thief_width/2,y - thief_width,thief_width,thief_width))
    pygame.draw.circle(screen,thief_color,(x,y - thief_width),thief_width/2)
    pygame.draw.circle(screen,thief_color,(x,y - thief_width*3/2 - thief_head_radius),thief_head_radius)

def draw_tile(surface,tile,border_color, position,radius = 50,width = 15):
    #El color depende del recurso
    fill_color = colors_per_resource[tile.recurso] if tile.recurso != "" else (255,255,255)  
    draw_hexagon(surface,border_color,fill_color,radius,position,width)
    n, r = 6, radius
    x, y = position
    vertexes = [
        (x - r * cos(2 * pi * (i +1.5) / n), y - r * sin(2 * pi * (i +1.5) / n))
        for i in range(n)
    ] 
    #Dibujo los caminos
    roads = tile.obtener_caminos()
    for pos,road in roads:
        pygame.draw.line(surface,road.jugador.color,vertexes[pos],vertexes[(pos + 1)%n],width + 2)  
    #Dibujo las casas
    houses = tile.obtener_asentamientos()
    for pos,house in houses:
        if isinstance(house,Asentamiento):
            pygame.draw.circle(surface,house.jugador.color,vertexes[pos],15)
            pygame.draw.circle(surface,black,vertexes[pos],15,width=3)
        elif isinstance(house,Ciudad):
            pygame.draw.rect(surface,house.jugador.color,pygame.Rect(vertexes[pos][0] - 15,vertexes[pos][1] - 15,30,30))
            pygame.draw.rect(surface,black,pygame.Rect(vertexes[pos][0] - 15,vertexes[pos][1] - 15,30,30),3)
    font = pygame.font.Font('freesansbold.ttf', 22)
    number = font.render(str(tile.numero),True,black,white)
    numberRect = number.get_rect(center = position)
    pygame.draw.circle(surface,white,position,17.5)
    surface.blit(number,numberRect)
    #Dibujo al ladrón
    if tile.ladron:
       draw_thief((x,y - 18),surface)
       if not tile.recurso == "Central":
        pygame.draw.circle(surface,thief_color,position,17.5,3)
    
def draw_catan_board(tiles,screen,center):
    radius = 75
    deltaX = cos(pi/6) *radius
    deltaY = sin(pi/6) *radius
    positions = []
    for row,row_span in enumerate([2,3,4,3,2]):
        x_center,y_center = center
        for x in np.arange(-deltaX*row_span,deltaX*row_span +1,deltaX*2):
            positions.append((x_center + x,y_center + (row-2)*(radius + deltaY) ))
    for number,tile in enumerate(tiles):
        draw_tile(screen,tile,(0,0,0),positions[number],radius,6)
    pygame.display.flip()

def draw_resources(player,screen,start):
    x,y = start
    for position,resource in enumerate(["Madera","Trigo","Ladrillo","Lana","Piedra"]):
        pygame.draw.rect(screen,colors_per_resource[resource],pygame.Rect(x + position*50,y,40,40))
        pygame.draw.rect(screen,black,pygame.Rect(x + position*50,y,40,40),3)
        font = pygame.font.Font('freesansbold.ttf', 25)
        quantity = font.render(str(player.cantidad_de(resource)),True,black,white)
        quantity_rect = quantity.get_rect(center = (x + position*50 + 20,y + 60))
        pygame.draw.rect(screen,white,pygame.Rect(x + position*50,y + 45,40,30))
        screen.blit(quantity,quantity_rect)


def draw_player(player,screen,position):
    center_x,center_y = position
    width = 450
    height = 130
    pygame.draw.rect(screen,player.color,pygame.Rect(center_x - width/2,center_y - height/2,width,height))
    pygame.draw.rect(screen,black,pygame.Rect(center_x - width/2,center_y - height/2,width,height),3)
    font = pygame.font.Font('freesansbold.ttf', 30)
    name = font.render(player.nombre,True,black,white)
    name_rect = name.get_rect(center = (center_x,center_y - height/3))
    screen.blit(name,name_rect)
    draw_resources(player,screen,(center_x - width/2 + 25,center_y - 25))

def draw_players(players,screen,start,step):
    for number,player in enumerate(players):
        x,y = start
        pos = (x,y + step*number)
        draw_player(player,screen,pos)

def draw_dice(dice,screen):
    pygame.draw.rect(screen,white,pygame.Rect(30,606,70,70))
    pygame.draw.rect(screen,black,pygame.Rect(30,606,70,70),3)
    font = pygame.font.Font('freesansbold.ttf', 50)
    number = font.render(str(dice),True,black,white)
    number_rect = number.get_rect(center = (65,641))
    screen.blit(number,number_rect)
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("DADOS",True,black,white)
    text_rect = text.get_rect(center = (65,590))
    screen.blit(text,text_rect)

def jugar_con_interfaz(jugadores,tablero):
    quit_game = False

    dice = queue.Queue()

    student_dice = juego.tirar_dados

    def tirar_dados_con_queue():
        amount = student_dice()
        dice.put(amount)
        return amount

    juego.tirar_dados = tirar_dados_con_queue

    class Input(threading.Thread):
        def run(self):
            juego.jugar_catan(jugadores,tablero)


    i : threading.Thread = Input()
    i.start()

    pygame.init()
    pygame.display.set_caption('Catán')
    Icon = pygame.image.load('img/game_logo.svg')
    pygame.display.set_icon(Icon)
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 704

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))

    while not quit_game and i.is_alive() :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
        draw_catan_board(tablero.fichas(),screen,(SCREEN_WIDTH/3,SCREEN_HEIGHT/2))
        draw_players(jugadores,screen,(SCREEN_WIDTH*4/5,88),176)
        try:
            dice_number = dice.get(False)
        except queue.Empty:
            dice_number = None
        if dice_number != None:
            draw_dice(dice_number,screen)
        time.sleep(0.25)
    pygame.quit()