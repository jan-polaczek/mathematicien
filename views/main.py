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

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                break
            if event == 'pochodne':
                self.window.layout = [sg.Text('Ha!')]
        self.window.close()


window = MainWindow(['funkcja kwadratowa', 'funkcja liniowa', 'pochodne'])
window.run()