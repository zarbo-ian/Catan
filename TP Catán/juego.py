ORDEN_ESPECIAL = False
import random
from tablero import TableroCatan
def tirar_dados():
    pass

def rellenar_tablero(tablero):
    tablero_num = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    recursos = ["Ladrillo","Ladrillo","Ladrillo","Piedra","Piedra","Piedra","Trigo","Trigo","Trigo","Trigo","Lana","Lana","Lana","Lana","Madera","Madera","Madera","Madera"]
    random.shuffle(tablero_num)
    random.shuffle(recursos)
    
    
    for numero in tablero_num:
        print(tablero_num[numero], " es ", recursos[numero])
    else:
        print("10 es Desierto")    
    
    

def jugar_catan(jugadores,tablero):
    pass

tab = TableroCatan()
rellenar_tablero(tab)
