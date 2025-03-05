
import math

def suma_riemann(f, a, b, n, verbose=False):
    """Aproxima el valor de una integral definida usando el método de Riemann.
    
    Utiliza la suma de áreas de rectángulos con altura determinada por el valor
    de la función en el extremo izquierdo de cada subintervalo.

    Args:
        f (function): Función a integrar.
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        n (int): Número de subintervalos para la aproximación.
        verbose (bool, optional): Muestra tabla detallada. Defaults to False.

    Returns:
        float: Aproximación de la integral definida.
    """
    if n <= 0:
        raise ValueError("n debe ser un entero positivo")
    
    h = (b - a) / n
    acumulador = 0.0
    x_actual = a
    
    if verbose:
        print("--" * 70)
        print(f"{'Iteración':>10} {'x_i':>15} {'f(x_i)':>15} {'Ancho':>15} {'Área':>15} {'Área Total':>15}")
        print("--" * 70)
    
    for i in range(n):
        area = f(x_actual) * h
        acumulador += area
        
        if verbose:
            print(f"{i:>10} {x_actual:>15.7f} {f(x_actual):>15.7f} {h:>15.7f} {area:>15.7f} {acumulador:>15.7f}")
        
        x_actual += h
    
    return acumulador

if __name__ == "__main__":
    # Ejemplo de uso
    f = lambda x: 2 / (3 * x + 1)
    a = 1
    b = 2
    n = 10000 
    
    # Prueba con salida detallada
    print("Prueba con salida detallada:")
    resultado = suma_riemann(f, a, b, n=n, verbose=True)
    print(f"\nAproximación con {n} subintervalos: {resultado:.10f}\n")
    
    # Prueba de alta precisión
    n = 100_000_000
    resultado = suma_riemann(f, a, b, n=n)
    print(f"Aproximación con {n} subintervalos: {resultado:.10f}")