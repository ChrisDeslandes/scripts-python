class Probabilidade:

    @classmethod
    def fatorial(cls, x):
        if x < 0: return 0
        return x * cls.fatorial(x - 1) if x > 1 else 1

    @classmethod
    def arranjo(cls, x, y):
        return 0 if x < y else int(cls.fatorial(x)/(cls.fatorial(x - y)))

    @classmethod
    def combinacao(cls, x, y):
        return 0 if x < y else int(cls.fatorial(x)/(cls.fatorial(x - y) * cls.fatorial(y)))
