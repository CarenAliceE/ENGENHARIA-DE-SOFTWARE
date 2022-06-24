class Teste(unittest.TestCase):

    def setup(self):
        self.Calculadora = ('Calculadora')

    def teste_soma(self):
        self.calc = Calculadora()
        resultado = self.calc.soma(6, 6)
        esperado = 12
        self.assertEqual(resultado, esperado)

    def teste_sub(self):
        self.calc = Calculadora()
        resultado = self.calc.sub(20, 10)
        esperado = 10
        self.assertEqual(resultado, esperado)

    def teste_multi(self):
        self.calc = Calculadora()
        resultado = self.calc.mult(3, 3)
        esperado = 9
        self.assertEqual(resultado, esperado)

    def teste_div(self):
        self.calc = Calculadora()
        resultado = self.calc.div(4, 2)
        esperado = 2
        self.assertEqual(resultado, esperado)


if _name_ == '_main_':
    unittest.main()