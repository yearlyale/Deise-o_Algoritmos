import numpy as np

k=100000
bolsas=[[[],0]]
objetos = np.random.randint(1,20,(k,))

W = 2000

objetos=sorted(objetos,reverse=True)

for o in objetos:
    nb=len(bolsas)
    i=0
    ingresado = False
    while(i<nb and not ingresado):
        if (bolsas[i][1]+o<=W):
            bolsas[i][0].append(o)
            bolsas[i][1]+=o
            ingresado=True
        i+=1
    if(ingresado==False):
        bolsas.append([[o],o])

print("se ocuparon",len(bolsas),"bolsas")
