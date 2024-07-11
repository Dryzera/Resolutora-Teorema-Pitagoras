import mylibs.cateto as cateto
import mylibs.hipotenusa as hipotenusa
import mylibs.fechar_programa as fechar_programa

operacao = input('O que deseja descobrir?\n\t Cateto: 1\n\t Hipotenusa: 2\n')
operacao_liberada = None
fechar_o_programa = fechar_programa.fechar

try:
    operacao = int(operacao)
except ValueError:
    raise ValueError('Não posso converter letras em números.')

def verifica_operacao(operacao):
    if operacao in (1, 2):
        operacao_liberada = True
        return operacao_liberada
    else:
        print(f'O número digitado não corresponde a cateto nem hipotenusa. Número enviado {operacao}.')
        fechar_o_programa()

operacao_liberada = verifica_operacao(operacao)

if operacao_liberada is True:
    if operacao == 1:
        obtendo_cateto = cateto.ObterNumeros()
        calcular_cateto = cateto.CalcularCateto()
        hipotenusa, cateto = obtendo_cateto.converter()
        print(calcular_cateto.calcular_cateto(hipotenusa, cateto))
        fechar_o_programa()

    elif operacao == 2:
        obtendo_numeros = hipotenusa.ObterNumeros()
        calcular_hipotenusa = hipotenusa.CalcularHipotenusa()
        cateto, cateto2 = obtendo_numeros.converter()
        print(calcular_hipotenusa.calcular_hipotenusa(cateto, cateto2))
        fechar_o_programa()