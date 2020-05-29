from models.exercises import *


class ExerciseManager:
    def __init__(self, string):
        self.string = string

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
