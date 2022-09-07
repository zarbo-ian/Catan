ORDEN_ESPECIAL = False
import random
from tablero import TableroCatan
def tirar_dados():
    pass



def rellenar_tablero_meta(tablero):
    tablero_num = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    recursos = ["Ladrillo","Ladrillo","Ladrillo","Piedra","Piedra","Piedra","Trigo","Trigo","Trigo","Trigo","Lana","Lana","Lana","Lana","Madera","Madera","Madera","Madera"]
    random.shuffle(tablero_num)
    random.shuffle(recursos)

    for num in tablero_num:


    for rec in recursos:
    
        
    return rec
    return num



def rellenar_tablero(tablero):

    #numero_de_ficha = rellenar_tablero_meta(tablero)
    tablero_num = rellenar_tablero_meta(tablero)
    recursos = rellenar_tablero_meta(tablero)

   
    
    tablero.colocar_numero(numero_de_ficha = tablero_num, numero = tablero_num - 1)
    tablero.colocar_recurso(recursos)
    
    
    #for numero in tablero_num:
    #    print(tablero_num[numero], " es ", recursos[numero])
   # else:
    #    print("10 es Desierto")    
    


    

def jugar_catan(jugadores,tablero):
    pass

tab = TableroCatan()
rellenar_tablero(tab)
