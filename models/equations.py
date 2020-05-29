

class PolynomialEquation:
    def __init__(self, coefficients, symbols):
        self.coefficients = coefficients
        self.symbols = symbols

    @property
    def equation_string(self):
        string = ''
        for idx, (symbol, coefficient) in enumerate(zip(self.symbols, self.coefficients)):
            if idx == len(self.symbols) / 2:
                string += ' = '
            if coefficient != 0:
                if coefficient > 0 and idx != len(self.symbols) / 2:
                    string += ' + '
                string += f'{coefficient}{symbol}'
        return string.replace('-', ' - ').lstrip(' +')
