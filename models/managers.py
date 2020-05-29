from .exercises import *


# Menedżer zadań, pozwala wybierać rodzaje zadań na podstawie ich nazw
class ExerciseManager:
    def __init__(self, string=None):
        self.string = string
        self.topics = ('Równanie liniowe', 'Równanie kwadratowe')

    @property
    def exercise_class(self):
        if self.string == 'Równanie liniowe':
            return LinearEquationExercise
        elif self.string == 'Równanie kwadratowe':
            return QuadraticEquationExercise
        else:
            return NotImplementedError('Takie ćwiczenie na razie nie istnieje')

    @property
    def randomized_exercise(self):
        return self.exercise_class()
