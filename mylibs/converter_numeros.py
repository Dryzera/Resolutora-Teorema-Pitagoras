class ConverterNumeros:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def converter(self):
        try:
            value_a = float(self.a)
            value_b = float(self.b)
            return value_a, value_b, True
        except ValueError:
            raise ValueError(f'Não foi possivel converter os números enviados. Enviados: ({self.a}, {self.b})')
        

if __name__ == '__main__':
    conversao = ConverterNumeros('4', '3')
    print(conversao.converter())