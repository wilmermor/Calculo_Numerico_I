import math

def trapecio(f, a, b, n, verbose=False):
    """Aproxima el valor de una integral definida usando la regla del trapecio.
    
    Divide el intervalo en subintervalos y aproxima el área bajo la curva
    mediante trapecios en cada subintervalo.

    Args:
        f (function): Función a integrar.
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        n (int): Número de subintervalos para la aproximación.
        verbose (bool, optional): Muestra tabla detallada. Defaults to False.

    Returns:
        float: Aproximación de la integral definida.
        
    Raises:
        ValueError: Si n no es un entero positivo.
    """
    if n <= 0:
        raise ValueError("n debe ser un entero positivo")
    
    h = (b - a) / n
    acumulador = 0.0
    x_actual = a
    
    if verbose:
        print("--" * 85)
        print(f"{'Iteracion':>10} {'x_i':>15} {'f(x_i)':>15} {'x_i+1':>15} {'f(x_i+1)':>15} {'Área Trapecio':>15} {'Área Total':>15}")
        print("--" * 85)
    
    for i in range(n):
        x_siguiente = x_actual + h
        area = (f(x_actual) + f(x_siguiente)) * h / 2
        acumulador += area
        
        if verbose:  
            print(f"{i:>10} {x_actual:>15.7f} {f(x_actual):>15.7f} {x_siguiente:>15.7f} {f(x_siguiente):>15.7f} {area:>15.7f} {acumulador:>15.7f}")
        
        x_actual = x_siguiente
    
    return acumulador

if __name__ == "__main__":
    # Ejemplo de uso
    f = lambda x: 2 / (3 * x + 1)
    a = 1
    b = 2
    n = 5
    
    # Prueba con salida detallada 
    print("Prueba con salida detallada:")
    resultado = trapecio(f, a, b, n, verbose=True)
    print(f"\nAproximación con 5 subintervalos: {resultado:.10f}\n")
    
    # Prueba de alta precisión
    n = 100_000_000
    resultado = trapecio(f, a, b, n=n)
    print(f"Aproximación con {n} subintervalos: {resultado:.10f}")