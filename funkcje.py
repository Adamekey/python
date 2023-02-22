# funkcja to kawalek programu, ktory moze przetworzyc dane / argumenty i moze ale nie musi zwrocic na zewnatrz
# wartosc, ktora mozna wykorzystac w innym miejscu (argument w kolejnych dzialaniach)
# funkcja moze posiadac wlasne zmienne, uzyteczne tylko dla niej
# wciecia pokazuja moc przy funkcjach
def nazwa_funkcji():  # w nawiasie sa argumenty lub parametry
    print("Dzialam w funkcji")

print("Dzialam poza funkcja")
nazwa_funkcji()

# funkcja ktora nic nie zwraca (np. tylko print) - nazywana jest procedura
# Argumenty zwane tez parametrami - potrzebne dla wiekszosci funkcji
# deklarowanie parametrow - sa 3 mozliwosci
# parametry pozycyjne - w naglowku funkcji nazwy zmiennych dla kazdego parametru
def dodawanie(a, b):
    print(f"Wynik: {a + b}")

dodawanie(4, 5)

def odejmowanie(a, b = 0):   # parametry z kluczem (domyslna wartosc) musza byc definiowane na koncu
    print(f"Wynik: {a - b}")

odejmowanie(4)
odejmowanie(4, )

def dzielenie(a, b):
    print(f"Wynik dzielenia: {a/b}")

dzielenie(b = 2, a = 4)

# dowolna zmienna liczba argumentow
def wylicz(*liczba):
    print(f"Ilosc przekazanych parametrow: {liczba}")

wylicz(3,4,5,6,7) # powstanie krotka

#   RETURN
def funkcja2():
    print(f"Hej tutaj Python...")
    return  "W wersji 3.9"

funkcja2()
zmienna = funkcja2()
print(zmienna)

def funkcja3(l1, l2):
    suma = l1 + l2
    print(f"Suma liczb: {suma}")
    iloczyn = l1 * l2
    return iloczyn

d1 = funkcja3(2,6)
print(d1)

# lambda - anonimowa funkcja jednolinijkowa - jedna konkretna czynnosc bez nazwy, uzywana tylko raz lub ograniczona ilosc uzyc
x = int(input("Podaj liczbe:"))
zm = lambda x: x + 1
print(f"Wynik lambdy: {zm(x)}")

print("inny przyklad lambdy")
lista = [1, 3, 5, 7]
print(f"Zastosowanie lambdy w funkcji map: {list(map(lambda x: x * 2, lista))}")

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosly")
print(wiek(15))