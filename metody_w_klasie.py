#
class Licznik():
    ile = 0
    def __init__(self):
        Licznik.ile += 1
        self.ktory = Licznik.ile
        print(f"To jest obiekt numer: {Licznik.ile}")
    def __del__(self):
        Licznik.ile -= 1
        print(f"Niszcze obiekt nr {self.ktory}, pozostalo jeszcze {Licznik.ile}")

    #metoda statyczna
    @staticmethod # dekorator sluzy do modyfikacji funkcji w okreslony sposob
    def policz():
        return Licznik.ile


a = Licznik()
b = Licznik()
c = Licznik()
# a = None
print(f"Liczba obiektow to: {Licznik.policz()}")