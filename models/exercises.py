import random

from constants import eps, max_coeff
from models.equations import PolynomialEquation


class Exercise:
    def __init__(self, title):
        self.title = title

    def check_answer(self, answers):
        check = True
        for result, answer in zip(sorted(self.results), sorted(answers)):
            if result == int(result):
                if not answer == result:
                    check = False
            else:
                if not abs(answer - result) <= eps:
                    check = False
        return check

    @property
    def results(self):
        return [0]


class LinearEquationExercise(Exercise):
    def __init__(self, randomized=True):
        super().__init__('Równanie liniowe')
        self.coefficients = (0, 0, 0, 0)
        if randomized:
            self.randomize()

    def randomize(self):
        a1, b1, a2, b2 = (random.randint(-max_coeff, max_coeff) for i in range(4))
        if a1 == a2:
            a1 += 1
        self.coefficients = a1, b1, a2, b2

    @property
    def description(self):
        return 'Rozwiąż następujące równanie liniowe: ' + self.equation.equation_string

    @property
    def results(self):
        a1, b1, a2, b2 = self.coefficients
        return [(b2 - b1) / (a1 - a2)]

    @property
    def equation(self):
        return PolynomialEquation(self.coefficients, ('x', '', 'x', ''))


# Równanie kwadratowe, losuje
class QuadraticEquationExercise(Exercise):
    def __init__(self, randomized=True):
        super().__init__('Równanie kwadratowe')
        self.coefficients = (0, 0, 0, 0, 0, 0)
        if randomized:
            self.randomize()

    def randomize(self):
        a, x1, x2 = (random.randint(-max_coeff, max_coeff) for i in range(3))
        b = -a * (x1 + x2)
        c = a * x1 * x2
        a1 = random.randint(-abs(a), abs(a))
        a2 = a1 - a
        b1 = random.randint(-abs(b), abs(b))
        b2 = b1 - b
        c1 = random.randint(-abs(c), abs(c))
        c2 = c1 - c
        self.coefficients = a1, b1, c1, a2, b2, c2

    @property
    def description(self):
        return 'Rozwiąż następujące równanie kwadratowe: ' + self.equation.equation_string

    @property
    def results(self):
        a1, b1, c1, a2, b2, c2 = self.coefficients
        x1 = (b2 - b1 - ((b1 - b2) ** 2 - 4 * (a1 - a2) * (c1 - c2)) ** 0.5) / (2 * (a1 - a2))
        x2 = (b2 - b1 + ((b1 - b2) ** 2 - 4 * (a1 - a2) * (c1 - c2)) ** 0.5) / (2 * (a1 - a2))
        return x1, x2

    @property
    def equation(self):
        return PolynomialEquation(self.coefficients, ('x^2', 'x', '', 'x^2', 'x', ''))
