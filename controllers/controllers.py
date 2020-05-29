from views.main_gui import MainWindow
from models.managers import ExerciseManager


class MainGUIController:
    def __init__(self):
        self.exercise_manager = ExerciseManager()
        self.topics = self.exercise_manager.topics
        self.main_window = MainWindow(self.topics)

    # metoda obsługująca główne okno aplikacji
    def run(self):
        while True:
            event, values = self.main_window.window.read()
            if event in (None, 'Cancel'):
                break
            if event in self.topics:
                self.handle_topic_click(event)
        self.main_window.window.close()

    # metoda obsługująca rozwiązywanie zadania
    def handle_topic_click(self, string):
        self.main_window.window.hide()
        self.exercise_manager.string = string

        exercise_window, results, exercise = self.new_exercise()
        while True:
            event, values = exercise_window.read()
            if event in (None, 'Cancel'):
                break
            elif event == 'OK':
                answers = list(values.values())
                try:
                    answers = [float(eval(answer)) for answer in answers]
                    if exercise.check_answer(answers):
                        self.main_window.render_correct_answer_notification()
                        exercise_window, results, exercise = self.new_exercise(exercise_window)
                    else:
                        self.main_window.render_wrong_answer_notification()
                except SyntaxError:
                    self.main_window.render_no_answer_warning()
            elif event == 'Pokaż odpowiedź':
                self.main_window.render_correct_answer_window(results)
            elif event == 'Inne zadanie':
                exercise_window, results, exercise = self.new_exercise(exercise_window)
        exercise_window.close()
        self.main_window.window.un_hide()

    # metoda wybierająca nowe zadanie
    def new_exercise(self, exercise_window=None):
        exercise = self.exercise_manager.randomized_exercise
        if exercise_window:
            exercise_window.close()
        exercise_window = self.main_window.render_exercise(exercise.title, exercise.description,
                                                           len(exercise.results))
        results = exercise.results
        return exercise_window, results, exercise


c = MainGUIController()
c.run()
