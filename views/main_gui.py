import PySimpleGUI as sg


class MainWindow:
    def __init__(self, topics):
        self.topic_buttons = [sg.Button(topic) for topic in topics]
        self.layout = [
            [sg.Text('Witaj w generatorze zadań z matematyki!')],
            [sg.Text('Wybierz temat, który chcesz przećwiczyć:')],
            self.topic_buttons
        ]
        self.window = sg.Window('Generator', self.layout)

    # metoda wyświetlająca zadanie
    def render_exercise(self, title, description, results_number):
        layout = [
            [sg.Text(title)],
            [sg.Text(description)],
            [sg.Text('Wyniki podawaj w postaci liczb całkowitych, '
                     'ułamków dziesiętnych lub ułamków niewłaściwych (np. -7/6)')],
            [sg.InputText(size=(15, 1)) for i in range(results_number)],
            [sg.Submit('OK'), sg.Button('Pokaż odpowiedź'), sg.Button('Inne zadanie')]
        ]
        return sg.Window(title, layout)

    def render_correct_answer_notification(self):
        sg.popup('Dobrze!')

    def render_wrong_answer_notification(self):
        sg.popup('Spróbuj jeszcze raz!')

    # metoda wyświetlająca poprawną odpowiedź
    def render_correct_answer_window(self, results):
        string = ''
        for result in results:
            string += f'{result}, '
        sg.popup(string.rstrip(', '))

    def render_no_answer_warning(self):
        sg.popup_error('Nie możesz zostawić pustego pola ani stawiać spacji!')

    def render_string_answer_warning(self):
        sg.popup_error('Odpowiedź nie może zawierać liter!')
