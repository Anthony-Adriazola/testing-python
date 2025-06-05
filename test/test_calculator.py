import unittest

from src.calculator import suma, resta

class CalculatorTest(unittest.TestCase): 

    #Prueba unitaria par la funcion suma
    def test_sum(self):
        print("Probando la funcion suma")
        self.assertEqual(suma(4, 3), 7)

    #Prueba unitaria para la funcion resta
    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

if __name__ == '__main__':
    unittest.main()