import mylibs.converter_numeros as converter_numeros
import mylibs.salvar_historico as salvar_historico
from math import sqrt



class ObterNumeros():
    def __init__(self):
        self.cateto = input('Digite o valor do cateto: ')
        self.cateto2 = input('Digite o valor do outro cateto: ')
        self._resultado_conversao = False

    
    def converter(self):
        cateto, cateto2, self._resultado_conversao = converter_numeros.ConverterNumeros(
            self.cateto, self.cateto2).converter()
        return cateto, cateto2

class CalcularHipotenusa():
    def __init__(self):
        super().__init__()

    def calcular_hipotenusa(self, cateto, cateto2):
        self.cateto = cateto**2
        self.cateto2 = cateto2**2
        x = self.cateto + self.cateto2
        try:
            x = sqrt(x)
        except ValueError:
            raise ValueError('O valor obtido é negativo, não consigo retirar a raiz quadrada.')
        salvar_historico.SalvarResultado(x).salvar_json()
        return f'O valor da hipotenusa é: {x}'
        