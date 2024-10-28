import math
import unittest

from Newton_Raphson.newton_raphson import newton_rapshon


class TestBiseccion(unittest.TestCase):

    def test_1(self):
        f = lambda x: math.exp(-x) - math.log(x)
        a = 1
        b = 1.5
        er = 0.01
        resultado = Biseccion(f, a, b, er)
        self.assertEqual(resultado[0], 1.3046875)
        self.assertEqual(resultado[1],f(1.3046875))
        self.assertEqual(resultado[2], 0.005988023952095809)

    def test_2(self):
        f = lambda x: x**2 - 4
        a = 0
        b = 3
        er = 0.01
        resultado = Biseccion(f, a, b, er)
        self.assertEqual(resultado[0], 2.00390625)
        self.assertEqual(resultado[1],f(2.00390625))
        self.assertEqual(resultado[2], 0.005847953216374269)
