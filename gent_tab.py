
def generar_tablero(tablero):
    t1=[]
    import random
    rec={"ladrillo":3,
         "piedra":3,
         "trigo":4,
         "lana":4,
         "madera":4}
    for i in rec:
        t1+=[i]*rec[i]
    random.shuffle(t1)
    a=list(map(lambda x:int(x,16), "2334455668899AABBC"))
    for i in range(len(t1)):
        t1[i]=t1[i],a[i]
    t1.append("")
    random.shuffle(t1)
    a=t1.index("")
    t1[9],t1[a]=t1[a],t1[9]
    tablero=t1

#NO ENTIENDO UNA GOMA ORIBE!!!
#FIRMA -T
                
#generar_tablero()
