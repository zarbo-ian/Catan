ORDEN_ESPECIAL = False
import random
from tablero import TableroCatan



def tirar_dados():
    pass



#def rellenar_tablero_meta(tablero):
   # tablero_num = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
   # recursos = ["Ladrillo","Ladrillo","Ladrillo","Piedra","Piedra","Piedra","Trigo","Trigo","Trigo","Trigo","Lana","Lana","Lana","Lana","Madera","Madera","Madera","Madera"]
    #random.shuffle(tablero_num)
   # random.shuffle(recursos)

    #for indiceNum in range(len(tablero_num)):
        #tablero_num[indiceNum]
        #indiceNum = num
    #    num = tablero[indiceNum]
    #    tablero.colocar_numero(numero_de_ficha = num, numero = num - 1)
    #    return num

    #for indiceRec in range(len(recursos)):
    #    recursos [indiceRec]
    #    indiceRec = rec
     #   tablero.colocar_recurso(rec)
    
      #  return rec
    



def rellenar_tablero(tablero):

    tablero_num = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    recursos = ["Ladrillo","Ladrillo","Ladrillo","Piedra","Piedra","Piedra","Trigo","Trigo","Trigo","Trigo","Lana","Lana","Lana","Lana","Madera","Madera","Madera","Madera"]
    random.shuffle(tablero_num)
    random.shuffle(recursos)

    for indiceNum in range(len(tablero_num)):
        #tablero_num[indiceNum]
        #indiceNum = num
        num = tablero_num[indiceNum]
        tablero.colocar_numero(numero_de_ficha = num, numero = num - 1)
        return num

    for indiceRec in range(len(recursos)):
        rec = recursos [indiceRec]
        #indiceRec = rec
        tablero.colocar_recurso(numero_de_ficha = num, recurso = rec)
    
        return rec

    #numero_de_ficha = rellenar_tablero_meta(tablero)
    #tablero_num = rellenar_tablero_meta(tablero)
    #recursos = rellenar_tablero_meta(tablero)



    #tablero.colocar_numero(numero_de_ficha = tablero_num, numero = tablero_num - 1)
    #tablero.colocar_recurso(recursos)
    
    
    #for numero in tablero_num:
    #    print(tablero_num[numero], " es ", recursos[numero])
   # else:
    #    print("10 es Desierto")    
    

tab = TableroCatan()
rellenar_tablero(tab)
    

def jugar_catan(jugadores,tablero):
    pass

