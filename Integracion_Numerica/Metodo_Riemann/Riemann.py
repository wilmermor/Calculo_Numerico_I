import math

def Riemann(funcion, xn, x0, n):
    """Método de Riemann para aproximar integrales."""
    h = (xn - x0) / n
    x_i = x0
    At = 0.0
    while x_i < xn:
        A = funcion(x_i) * h
        At += A
        x_i += h
    return At

if __name__ == "__main__":
    f = lambda x: 2 / (3 * x + 1)
    xn = 2
    x0 = 1
    n = 100000000
    print(Riemann(f, xn, x0, n))
