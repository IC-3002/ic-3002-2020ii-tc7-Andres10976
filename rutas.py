import numpy as np

#Esto es solo para no tener que pegar feamente este codigo en la funcion principal
def verificaCasilla( C, x, y ): 
      
    if x >= 0 and x < len(C[0]) and y >= 0 and y < len(C) and C[y][x] == 0: 
        return True
      
    return False
  

def encontrar_ruta(C): 
      
    #Recorrido de la solucion
    recorridoSol = [ [ 0 for j in range(len(C[1])) ] for i in range(len(C)) ] 

    #los 0,0 representan las coordenadas iniciales
    return encontrar_ruta_aux(C, 0, 0, recorridoSol)

# Aqui pasa la magia recursiva que esta bien durita AHHHASODJBAJKSBFAWIOW
def encontrar_ruta_aux(C, x, y, solucion): 
      
    # Se encuentra resultado
    if x == len(C[0]) - 1 and y == len(C) - 1 and C[y][x]== 0: 
        solucion[y][x] = 1
        return solucion
          
    # Verifico que el movimiento sea valido y que no sea peligroso
    if verificaCasilla(C, x, y) == True: 
        # Marco que me movi en la posible solucion
        solucion[y][x] = 1
          
        # Movimiento derecha
        posibleSol = encontrar_ruta_aux(C, x + 1, y, solucion)
        if  posibleSol != []:
            matriz = np.array(posibleSol)
            print(matriz)
            return posibleSol
            
              
        # Movimiento abajo
        posibleSol = encontrar_ruta_aux(C, x, y + 1, solucion)
        if posibleSol != []:
            matriz = np.array(posibleSol)
            print(matriz)
            return posibleSol
          
        solucion[y][x] = 0
    
    return []


