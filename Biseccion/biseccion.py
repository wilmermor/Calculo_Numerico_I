import math

def biseccion(f, a, b, er, n, verbose=False):
    """Método de Bisección para aproximar la raíz de una función f(x).

    Args:
        f (function): Función continua a la cual se le busca la raíz.
        a (float): Límite inferior del intervalo inicial.
        b (float): Límite superior del intervalo inicial.
        er (float): Cota máxima del error relativo (0 < er < 1).
        n (int): Número máximo de iteraciones permitidas.
        verbose (bool, optional): Muestra tabla detallada. Defaults to False.

    Returns:
        tuple: Tupla con la aproximación de la raíz y el último error relativo.
               Retorna False si no hay cambio de signo en el intervalo.
    """
    
    if f(a) * f(b) >= 0:
        return False
    
    m_anterior = a
    ei = 1.0
    i = 0
    
    if verbose:
        print("--" * 62)
        print(f"{'Iteracion':>10} {'a':>15} {'b':>15} {'Punto Medio':>15} {'f(a)':>15} {'f(m)':>15} {'Error':>15}")
        print("--" * 62)
    
    while ei > er and i < n:
        m_actual = (a + b) / 2
        ei = abs((m_actual - m_anterior)/m_actual) if i != 0 else 1.0
        
        if verbose:
            print(f"{i:>10} {a:>15.7f} {b:>15.7f} {m_actual:>15.7f} {f(a):>15.7f} {f(m_actual):>15.7f} {ei:>15.7f}")
        
        if f(m_actual) == 0:
            ei = 0.0
            break
        elif f(a) * f(m_actual) < 0:
            b = m_actual
        else:
            a = m_actual
        
        m_anterior = m_actual
        i += 1
    
    return m_actual, ei


if __name__ == "__main__":

    # Ejemplo de uso con salida detallada
    f = lambda x: math.exp(-x) - math.log(x)
    a = 1
    b = 1.5
    er = 0.01
    n = 100
    
    print("Prueba con salida detallada:")
    resultado = biseccion(f, a, b, er, n, verbose=True)
    
    if resultado:
        print("\n" + "--"*62)
        print(f"Raiz aproximada: {resultado[0]:.10f}")
        print(f"Error relativo final: {resultado[1]:.10f}")
    else:
        print("No hay cambio de signo en el intervalo o el metodo no converge")
    
    # Ejemplo de alta precisión sin salida detallada
    er_alto = 1e-10
    n_alto = 1000
    
    print("\nPrueba de alta precision:")
    resultado_alto = biseccion(f, a, b, er_alto, n_alto)
    
    if resultado_alto:
        print("\n" + "--"*62)
        print(f"Raiz aproximada: {resultado_alto[0]:.10f}")
        print(f"Error relativo final: {resultado_alto[1]:.10f}")
    else:
        print("No hay cambio de signo en el intervalo o el metodo no converge")