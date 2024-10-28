import math

def newton_rapshon(funcion,punto_a,punto_b,error_relativo):
    """Esta funcion 

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
    """
    Aproxima la derivada de la función f en el punto x usando diferencias finitas.
    
    :para f: Función a derivar.
    :para x: Punto en el cual se evalúa la derivada.
    :para h: Paso pequeño para la aproximación.
    :return: Valor aproximado de la derivada.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == "__main__":

    # Testing...

    f = lambda x: math.exp(x) - 3*x**2
    a = 0
    b = 1
    er = 0.02
    result = newton_rapshon(f,a,b,er)
    if result != False:
        print(result[0])
        print(result[1])
    else:
        print("la derivada da error")