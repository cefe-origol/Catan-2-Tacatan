import random

comando = input()
scomando = comando.split()
lad = 1
tri = 1
obe = 1
mad = 1

def Oribe_Dados():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dados = d1 + d2

    return dados

dados = Oribe_Dados()
print(dados)



def Bloque_de_comando(scomando,lad,tri,mad,obe):
    if (scomando[0] == "fin"):
        print("fin")
    elif (scomando[0] == "pas"):
        print("paso")
    elif (scomando[0] == "ase"):
        
        if(lad >= 1 and obe <= 1 and mad >=1 and tri <=1):
            print("constuida")
            print(scomando[1], scomando[2])

        else:
         print("sos pobre")        
        
        print("ase")

    elif (scomando[0] =="cam"):

     if(lad >= 1 and obe <= 1 and mad >=1 and tri <=1):
            print("constuida")
            print(scomando[1], scomando[2])

    else:
        print("sos pobre")
        

    



Bloque_de_comando(scomando,lad,tri,mad,obe)