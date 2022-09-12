class Tablero:
    def __init__(self):
        self.recursos=[]
        self.numeros=[]
        self.generar_tablero()
        
    def generar_tablero(self):
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
            t1[i]=t1[i],a[1]
        t1.append("")
        random.shuffle(t1)
        a=t1.index("")
        t1[9],t1[a]=t1[a],t1[9]
        for i in t1:
            self.recursos,self.numeros=i

#NO ENTIENDO UNA GOMA ORIBE!!!
#FIRMA -T
                
