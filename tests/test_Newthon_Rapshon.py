import math
import unittest

from Newton_Raphson.newton_raphson import newton_rapshon


class TestBiseccion(unittest.TestCase):

    def test_1(self):
        print("\n\n\n")
        print("**"*25+" TEST 1 "+"**"*25)
        print("\n\n\n")
        f = lambda x: math.exp(-x) - math.log(x)
        a = 0
        b = 1
        er = 0.02
        resultado = newton_rapshon(f,a,b,er)
        print(f"\nResultado de f(x)= {self.assertEqual(resultado[0],1.3097993813968591)}")
        print(f"Error Relativo = {self.assertEqual(resultado[1],0.0005371897366562572)}")

    def test_2(self):
        print("\n\n\n")
        print("**"*25+" TEST 2 "+"**"*25)
        print("\n\n\n")
        f = lambda x: x**2 - 4
        a = 0
        b = 3
        er = 0.01
        resultado = newton_rapshon(f,a,b,er)
        self.assertEqual(resultado[0],2.0000006938662187)
        self.assertEqual(resultado[1],0.000832986111283388)
        
        

        