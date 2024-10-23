import math

def Biseccion(funcion,Punto_A,Punto_B,Error_Relativo):
    #Comprobamos que los Extremos del Intervalo tiene signo opuesto,sino existe el punto P salimos de la funcion 
    if (funcion(Punto_A) * funcion(Punto_B) >= 0):
        return print("El Metodo de Biseción no se puede aplicar")
    
    #Calculamos la Mitad entre el punto A y el punto B
    Media = (Punto_A + Punto_B) / 2

    #Imprimimos los Datos Actuales de los Puntos A y B, la Media, Funcion Evaluada en la Media y el Error relativo
    print("--"*80)
    print(f"{'Punto A':>10} {'Punto B':>15} {'Punto Medio':>15} {'F(Media)':>15} {'Error Relativo':>15}")
    print(f"{Punto_A:>10.5f} {Punto_B:>15.5f} {Media:>15.5f} {funcion(Media):>15.5f} {abs(Media - Punto_B) / Media:>15.5f}")

    #Comprobamos si la funcion evaluada llego al punto P o si el error relativo es menor al que se nos indica 
    if funcion(Media) == 0 or abs(Media - Punto_B) / Media < Error_Relativo:
        return print(
            f"\nLa Función Evaluada en el Punto ({Media}) = {funcion(Media)}\n",
            f"El Error relativo es = {abs(Media - Punto_B) / Media}"
        )
    #Aplicamos recursividad, con la condicion de que si el cambio de signo se produce entre Punto A y la Media, retornar cambiando el Punto B
    # Sino retornar cambiando el Punto A    
    return Biseccion(funcion,Punto_A,Media,Error_Relativo) if funcion(Punto_A)*funcion(Media) < 0 else Biseccion(funcion,Media,Punto_B,Error_Relativo)

#Creamos una Funcion que tenga la Funcio que vamos a evaluar 
def Funcion(x):
    return math.exp(-x) - math.log(x,math.e)
    
# ==========================================================
#                       INICIO
# ==========================================================

# Parámetros iniciales
Punto_A = 1  # Punto A del Intervalo
Punto_B = 1.5  # Punto B del Intervalo
Error_Relativo = 0.01  # Error relativo que se nos exige

#Llamamos a la funcion de Biseccion
Biseccion(Funcion,Punto_A,Punto_B,Error_Relativo)
