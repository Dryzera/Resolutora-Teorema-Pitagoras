""" 
Este módulo está inátivo por conta de alguns problemas envolvendo salvamento, em breve reative-o corrigindo:
1 - colocar qual o tipo de operaçao (cateto ou hipotenusa);
2 - corrigir a forma que é salvada no arquivo json, não criando uma nova estrutura de dados. 
"""

from datetime import datetime
import mylibs.fechar_programa as fechar_programa

class SalvarResultado:
    _PATH_DEFAUT = '.\\historico_de_contas\\historico.txt'
    def __init__(self, resultado) -> None:
        self.resultado = resultado
        __formato = '%d/%m/%Y - %H:%M:%S'
        __data_atual = datetime.now()
        self.hora_atual = datetime.strftime(__data_atual, __formato)

    def _juntar_resultado_hora(self):
        self.salvar_em_db = {f'{self.hora_atual}': self.resultado}
        return self.salvar_em_db
    
    def salvar_json(self):
        juntando_hora_resultado = SalvarResultado(self.resultado)._juntar_resultado_hora()
        with open(SalvarResultado._PATH_DEFAUT, 'a', encoding='utf8') as file:
            file.write(f'\n{juntando_hora_resultado}')

    @staticmethod
    def fechamento_programa():
        fechar_programa.fechar()

class ApagarHistorico:
    @staticmethod
    def apagar():
        with open(SalvarResultado._PATH_DEFAUT, 'w', encoding='utf8') as file:
            file.write(' ')
        