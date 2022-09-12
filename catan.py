import random
from clases import *

#Modo de prueba 1 es on 0 es off
test_mode = 1

#Lee el comando que manda el usuario y lo divide en partes
comando = input()
scomando = comando.split()

#Que jugador esta jugando
turno = Jugador("jose", (255,255,255))

if (test_mode == 1):
    #recursos puestos con fines de pruebas
    pablo = 999
    lad = pablo
    tri = pablo
    obe = pablo
    mad = pablo
    pie = pablo

elif (test_mode == 0):
    #recursos del jugador de turno 
    pablo = turno.inventario
    lad = pablo["ladrillo"]
    tri = pablo["trigo"]
    obe = pablo["lana"]
    mad = pablo["madera"]
    pie = pablo["piedra"]


#son las cartas de desarollo PUNTO DE VICTORIA; MONOPOLIO; RECURSOS; CAMINO; CABALLEROS
devcard=["victor","mono","recurso","camino","arturo"]

#GENERA EL OUTPUT DE LOS DADOS
def Oribe_Dados():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dados = d1 + d2

    return dados

#PIRNTEA LOS DAODS
dados = Oribe_Dados()
print(dados)


#SE ENCARGA DE INTEPRETAR LOS COMANDOS DE USUARIO
def Bloque_de_comando(scomando,lad,tri,mad,obe):
   
   #TERMINA LA PARTIDA
    if (scomando[0] == "fin"):
        print("fin")
    
    #PASA EL TURNO
    elif (scomando[0] == "pas"):
        print("paso")
    #CREA UNA CASA
    elif (scomando[0] == "ase"):
        
        if(lad >= 1 and obe <= 1 and mad >=1 and tri <=1):
            print("constuida")
            print(scomando[1], scomando[2])
            return scomando[1], scomando[2],"construir_ase"

        else:
         print("sos pobre")        
        
        print("ase")
  
    #CREA UN CAMINO
    elif (scomando[0] =="cam"):

     if(lad >= 1 and obe <= 1 and mad >=1 and tri <=1):
            print("constuida")
            print(scomando[1], scomando[2])
            return scomando[1], scomando[2],"construir_cam"

     else:
          print("sos pobre")

    #COMPRA LA CARTA DE DESAROLLO
    elif (scomando[0] == "devcard" and obe >= 1 and tri >= 1 and pie >= 1):
         random = random.randint(0, 4)
         devcard[random]
         return devcard
         
         

    


#ES PARA PROBAR LOS COMANDOS
Bloque_de_comando(scomando,lad,tri,mad,obe)