'''
IF
if warunek <0:
    instrukcja
elif warunek >0:
    instrukcja
else:
    instrukcja

MATCH
match zmienna:
    case wzorzec 1:
        instrukcja
    case wzorzec 2:
        instrukcja
    case _:
        instrukcja
'''
punkty = 50

if punkty >= 65:
    print("Ocena pozytywna")
else:
    print("Ocena negatywna")

saldo = 90

if saldo >= 0:
    print("Saldo dodatnie 0!")
elif saldo == 80:
    print("Saldo jest rowne 80")
    if saldo == 200:
        print("Saldo jest 200")
elif saldo >= 90:
    print("Saldo jest wieksze badz rowne 90")
elif saldo < 0:
    print("Saldo jest mniejsze od 0")
else:
    print("Nasze slado jest powyzej 0")
# if'y wykonywane sa po kolei wiec kolejne linijki nie sa wykonywane jesli warunek wyzej jest spelniony

#zagniezdzanie warunkow
warunek = True
warunek2 = True
if warunek:
    print("TAK")
    if warunek2:
        print("TAK po raz drugi")

warunek = True
warunek2 = False
if warunek:
    print("TAK")
    if warunek2:
        print("TAK po raz drugi")
    else:
        print("Info nr 2")
else:
    print("Info nr 1")