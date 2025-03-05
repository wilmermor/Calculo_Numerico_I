import math

def newton_raphson(f, a, b, er, verbose=False):
    """Método de Newton-Raphson para aproximar raíces de funciones.
    
    Encuentra una aproximación a la raíz de f(x) mediante iteraciones:
    x_{i+1} = x_i - f(x_i)/f'(x_i)

    Args:
        f (function): Función a la que se le busca la raíz
        a (float): Límite inferior del intervalo inicial
        b (float): Límite superior del intervalo inicial
        er (float): Error relativo máximo permitido (0 < er < 1)
        verbose (bool, optional): Muestra tabla de iteraciones. Default False

    Returns:
        tuple: (Aproximación de la raíz, error relativo final) si éxito
        bool: False si la derivada es cero, no hay convergencia o error

    Raises:
        ValueError: Si los parámetros de entrada son inválidos
    """
    # Validación de parámetros
    if er <= 0:
        raise ValueError("El error relativo debe ser mayor que cero")
    
    xi = (a + b) / 2  # Punto inicial medio del intervalo
    error_actual = 1.0
    max_iteraciones = 1000  # Máximo de iteraciones para prevenir bucles infinitos
    contador_iteraciones = 0
    
    # Calcula la derivada inicial
    try:
        df = derivar_funcion(f, xi)
    except Exception as e:
        raise ValueError(f"Error en cálculo de derivada inicial: {str(e)}")

    if df == 0:
        if verbose:
            print("Derivada inicial cero - metodo no aplicable")
        return False
    
    if verbose:
        print("--" * 78)
        print(f"{'Iteracion':>10} {'x_i':>18} {'f(x_i)':>18} {'f\'(x_i)':>18} {'Error':>18}" )
        print("--" * 78)

    while error_actual > er and contador_iteraciones < max_iteraciones:
        try:
            df = derivar_funcion(f, xi)
        except Exception as e:
            if verbose:
                print(f"Error en calculo de derivada durante iteraciones: {str(e)}")
            return False
            
        if df == 0:
            if verbose:
                print(f"Derivada cero en iteracion {contador_iteraciones} - metodo detenido")
            return False
            
        xi_siguiente = xi - f(xi) / df
        if xi_siguiente == 0:
            error_actual = abs(xi_siguiente - xi)
        else:
            error_actual = abs((xi_siguiente - xi) / xi_siguiente)
        
        if verbose:
            print(f"{contador_iteraciones:>10} {xi:>18.10f} {f(xi):>18.10f} {df:>18.10f} {error_actual:>18.10f}")

        if error_actual <= er:
            break
            
        xi = xi_siguiente
        contador_iteraciones += 1

    if contador_iteraciones >= max_iteraciones:
        if verbose:
            print("Maximo de iteraciones alcanzado sin converger")
        return False

    return xi, error_actual

def derivar_funcion(f, x, h=1e-8):
    """Calcula la derivada numérica de una función en un punto
    
    Args:
        f (function): Función a derivar
        x (float): Punto donde se evalúa la derivada
        h (float, optional): Valor de h para diferencia centrada. Default 1e-8
        
    Returns:
        float: Aproximación numérica de f'(x)
        
    Raises:
        ValueError: Si no se puede calcular la derivada
    """
    try:
        return (f(x + h) - f(x - h)) / (2 * h)
    except Exception as e:
        raise ValueError(f"Error al calcular derivada: {str(e)}")

if __name__ == "__main__":

    # Prueba con salida detallada
    print("Prueba con salida detallada:")
    f = lambda x: x**2 - 4
    a = 0
    b = 3
    er = 0.01
    resultado = newton_raphson(f, a, b, er, verbose=True)
    
    if resultado:
        print("\n" + "--"*78)
        print(f"Raiz: {resultado[0]:.15f}")
        print(f"Error: {resultado[1]}")
    
    # Prueba de alta precisión
    print("\nPrueba de alta precision:")
    resultado = newton_raphson(lambda x: x**2 - 4, 0, 3, er=1e-20)
    if resultado:
        print(f"Raiz: {resultado[0]:.25f}")
        print(f"Error: {resultado[1]}")