import math

def newton_rapshon(funcion,punto_a,punto_b,error_relativo):
    """Este metodo de newton rapshon consiste en aproximar una funcion f(x)
        al punto p (raiz o cero) de f(x), mediante la generacion de una sucesion
        {xi} tal que xi+1 = xi - f(xi)/f'(xi) ; f'(xi)!=0

    Args:
        funcion (_type_): _description_
        punto_a (_type_): _description_
        punto_b (_type_): _description_
        error_relativo (_type_): _description_

    Returns:
        _type_: _description_
    """    
    xi = (punto_a + punto_b) / 2
    i = 0
    error_i = 1.00
    resul = 0.00
    if derivar_funcion(funcion,xi) != 0:
        
        while(error_i > error_relativo):

            resul = xi - (funcion(xi)/derivar_funcion(funcion,xi))
            error_i = abs((resul - xi) / resul)
            print("--"*50)
            print(f"{'Iteración':>10} {'xi':>20} {'xi + 1':>20} {'Error Relativo':>20}")
            print(f"{i:>10} {xi:>20.7} {resul:>20.7} {error_i:>20.7}")
            xi = resul
            i +=1
        return xi,error_i
    return False

    
def derivar_funcion(f, x, h=1e-5):
    """Este metodo deriva una funcion, utilizando la formula 
        de la pendiente de la recta tangente 

    Args:
        f (_type_): Función a derivar.
        x (_type_): Punto en el cual se evalúa la derivada.
        h (_type_, optional): Una aproximacion de 0. Defaults to 1e-5.

    Returns:
        _type_: Valor aproximado de la derivada.
    """    
    return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == "__main__":

    # Testing...

    f = lambda x: x**2 - 4
    a = 0
    b = 3
    er = 0.01
    result = newton_rapshon(f,a,b,er)
    if result != False:
        print(f"\nResultado de f(x)= {result[0]}")
        print(f"Error Relativo = {result[1]}")
    else:
        print("La derivada es igual a cero")