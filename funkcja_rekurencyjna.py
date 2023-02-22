# rekurencja - maly magik
# rekurencja - kiedy funkcja wywoluje sama siebie
# np. ciag fibonacciego
def suma_for(liczba):
    suma = 0
    for i in range(liczba + 1):
        suma = suma + i
    return suma

zm = suma_for(5)
print(f"Wynik: {zm}")

def suma_rek(liczba):
    if liczba == 0: return 0
    return liczba + suma_rek(liczba -1)

zm2 = suma_rek(5)
print(f"Wynik2: {zm2}")