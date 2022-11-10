class Par:

    def __init__(self, tag, q1, q2):
        self.tag = tag
        self.q1 = q1
        self.q2 = q2

class Jogo:

    def __init__(self, listaPares, tema):
        self.concluido = False
        self.pares = listaPares
        self.paresDescobertos = 0
        self.tema = tema

    def acheiUmPar(self):
        self.paresDescobertos += 1
        if (self.paresDescobertos == 16):
            self.concluido = True

    def checaPar(self, t1, t2):
        for i in self.pares:
            if (i.q1 == t1 and i.q2 == t2) or (i.q1 == t2 and i.q2 == t1):
                self.acheiUmPar()
                if self.concluido == True:
                    return True
                else:
                    return False
        return None
