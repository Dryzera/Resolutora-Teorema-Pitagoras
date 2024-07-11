import mylibs.converter_numeros as converter_numeros
from math import sqrt
import mylibs.salvar_historico as salvar_historico

class ObterNumeros():
    def __init__(self):
        self.hipotenusa = input('Digite o valor da hipotenusa: ')
        self.cateto = input('Digite o valor de um cateto: ')
        self._resultado_conversao = False

    
    def converter(self):
        hipotenusa, cateto, self._resultado_conversao = converter_numeros.ConverterNumeros(
            self.hipotenusa, self.cateto).converter()
        return hipotenusa, cateto

class CalcularCateto():
    def __init__(self):
        super().__init__()

    def calcular_cateto(self, hipotenusa, cateto):
        self.hipotenusa = hipotenusa**2
        self.cateto = cateto**2
        x = self.hipotenusa - self.cateto
        try:
            x = sqrt(x)
        except ValueError:
            raise ValueError('O valor obtido é negativo, não consigo retirar a raiz quadrada.')
        salvar_historico.SalvarResultado(x).salvar_json()
        return f'O valor do cateto x é: {x}'