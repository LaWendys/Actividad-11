import math 

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    a = (x_2 - x_1)*(x_2 - x_1)
    b = (y_2 - y_1)*(y_2 - y_1)
    
    c = a + b
    
    distancia = math.sqrt(c)
    
    return distancia

def puntosCercanos(puntos:list)->list: 
    resultado=[]
    for puntoi in puntos:
        x1 = puntoi[0]
        y1 = puntoi[1]
        min = 1000
        cercano = (0,0)
        for puntoj in puntos:
            if puntoi != puntoj:
                x2 = puntoj[0]
                y2= puntoj[1]
                dis = distancia_euclidiana(x1, y1, x2, y2)
                if dis < min:
                    min = dis
                    cercano = (x2, y2)
        resultado.append((puntoi, cercano))
    return resultado