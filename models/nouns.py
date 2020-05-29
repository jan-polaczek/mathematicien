import random


# Klasa pozwalająca na wybieranie losowych rzeczowników do zadań z treścią
# oraz odmienianie ich przez przypadki.
# Na razie nieimplementowana.
class NounBase:
    def __init__(self):
        self.nouns = {}
        self.push('piłka', 'piłki', 'piłce', 'piłkę', 'piłce', 'piłką',
                  'piłki', 'piłek', 'piłkom', 'piłki', 'piłkach', 'piłkami')
        self.push('kulka', 'kulki', 'kulce', 'kulkę', 'kulce', 'kulką',
                  'kulki', 'kulek', 'kulkom', 'kulki', 'kulkach', 'kulkami')

    def push(self, s_nom, s_gen, s_dat, s_acc, s_loc, s_ins, p_nom, p_gen, p_dat, p_acc, p_loc, p_ins):
        self.nouns[s_nom] = {
            'singular': {
                'nominative': s_nom,
                'genitive': s_gen,
                'dative': s_dat,
                'accusative': s_acc,
                'locative': s_loc,
                'instrumental': s_ins
            },
            'plural': {
                'nominative': p_nom,
                'genitive': p_gen,
                'dative': p_dat,
                'accusative': p_acc,
                'locative': p_loc,
                'instrumental': p_ins
            }
        }

    def random(self):
        key, value = random.choice(list(self.nouns.items()))
        return value

