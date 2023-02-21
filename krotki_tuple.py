# krotki - struktury danych bardzo podobne do list, ale nie podlegaja modyfikacji po utworzeniu
# przydatne np do stanowienia kluczy w slowniku,
# dziala slysing zeby wyciac fragment krotki i uzyc w innym fragmencie programu, ale nie da sie nic zmienic
x = (1, 2, 3)
# wszystkie dostepne operacje pycharm podpowie jak zrobimy "x."
print(x[1])
# w krotkach jednoelementowych dodajemy przecinek, aby byla poprawnie zdefiniowana - nie jako zmienna
y = (3,)
print(y)
(jeden, dwa, trzy, cztery) = (1, 2, 3, 4) # jedna linia kodu przypisalismy 4 zmienne
print(jeden)

z = (1, 2, 3, 4)
a, b, *c = z # z krotki z przepisujemy 1 i 2 jako a i b, a wszystko co po * jako c
print (a, b, c)
a, *b, c = z
print (a, b, c)
a, *b, c, d, e = z # jesli zabraknie elementow to w miejscu * robi sie lista z jednym elementem jesli taki pozostal lub pusta lista []
print (a, b, c, d, e)