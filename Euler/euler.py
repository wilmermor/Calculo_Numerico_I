import math

def euler(f, t_inicial, w_inicial, t_final, n, verbose=False):
    """Aproxima la solución de una EDO usando el método de Euler.
    
    Utiliza el método de Euler para resolver ecuaciones diferenciales ordinarias
    de primer orden con valor inicial: w' = f(t, w).

    Args:
        f (function): Función derivada dw/dt = f(t, w).
        t_inicial (float): Valor inicial de t.
        w_inicial (float): Valor inicial de w correspondiente a t_inicial.
        t_final (float): Valor final de t donde se desea aproximar w.
        n (int): Número de pasos (subintervalos) para la aproximación.
        verbose (bool, optional): Muestra tabla detallada. Defaults to False.

    Returns:
        float: Aproximación de w en t_final.
        
    Raises:
        ValueError: Si n no es un entero positivo.
    """
    if n <= 0:
        raise ValueError("n debe ser un entero positivo")
    
    h = (t_final - t_inicial) / n  # Tamaño del paso
    t_actual = t_inicial
    w_actual = w_inicial
    
    if verbose:
        print("--" * 70)
        print(f"{'Iteracion':>10} {'t_i':>15} {'w_i':>15} {'f(t_i,w_i)':>15} {'h':>15} {'w':>15} {'w_i+1':>15}")
        print("--" * 70)
    
    for i in range(n):
        pendiente = f(t_actual, w_actual)  # f(t_i, w_i)
        delta_w = h * pendiente            # Δw = h * f(t_i, w_i)
        w_siguiente = w_actual + delta_w   # w_{i+1} = w_i + Δw
        
        if verbose:
            print(f"{i:>10} {t_actual:>15.7f} {w_actual:>15.7f} {pendiente:>15.7f} {h:>15.7f} {delta_w:>15.7f} {w_siguiente:>15.7f}")
        
        t_actual += h  # Actualizar t para la siguiente iteración
        w_actual = w_siguiente  # w_i pasa a ser w_{i+1}
    
    return w_actual

if __name__ == "__main__":
    # Ejemplo 1: Salida detallada con EDO dw/dt = t + w
    print("Prueba con salida detallada:")
    f = lambda t, w: t + w  # Función f(t, w) = t + w
    resultado = euler(f, 0.0, 1.0, 1.0, 10, verbose=True)
    print(f"\nAproximación de w(1.0) con 10 pasos: {resultado:.6f}")
    
    # Ejemplo 2: Alta precisión con EDO dw/dt = -2tw
    print("\n" + "--"*70)
    print("Prueba de alta precisión:")
    f2 = lambda t, w: -2 * t * w  # Solución exacta: w(t) = e^(-t²)
    resultado_alto = euler(f2, 0.0, 1.0, 1.5, 100000)
    exacto = math.exp(-(1.5)**2)
    print(f"Aproximacion de w(1.5) con 100,000 pasos: {resultado_alto:.10f}")
    print(f"Valor exacto w(1.5): {exacto:.10f}")
    print(f"Diferencia: {abs(resultado_alto - exacto):.2e}")