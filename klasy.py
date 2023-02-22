# podstawy o klasie
# programowanie obiektowe umozliwia przedstawienie rzeczy w sposob najbardziej zblizony do swiata realnego
# klasa to taki plan ile okien, drzwi w domu, atrybuty to np. kolory, a metody to otwieranie drzwi
# na podstawie klasy budowniczy moze zbudowac wiele domow
#klasa nie jest obiektem dzialajacym a jedynie jego struktura, planem
# nazwy klas rozpoczynamy z duzej litery
# klas dziedziczy po wbudowanym obiekcie bazowym object
class Zwierzak():
    """wirtualny pupil""" # wpisujemy dok-stringi w klasie, aby w momencie inicjalizacji klasy po najechaniu myszka bylo widac do czego ona sluzy
    def talk(self): # kazda metoda naszej instancji musi miec specjalny pierwszy parametr slef - dostarcza on metodzie sposobu odwolywania sie do obiektu
        print("Czesc, jestem egzemplarzem klasy zwierzak")

azor = Zwierzak()
azor.talk()

# konstruktor - klasy maja dostep do specjalnych metod
# metoda kosntruktor jest bardzo pozyteczny i jest czesto wykorzystywany do nadawania wartosci poczatkowych
class Zwierzak():
    """wirtualny pupil"""
    def __init__(self):
        print("\n\nUrodzil sie nowy zwierzak")

    def talk(self):
        print("Czesc, jestem egzemplarzem klasy zwierzak")

azor = Zwierzak()
azor.talk()

mruczek = Zwierzak()
mruczek.talk()