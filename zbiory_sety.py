# kolekcja obiektow z zapewniona niepowtarzalnoscia
# elementy zbioru musza byc niezmienne i musi byc mozliwe wyliczenie z nich wartosci hasha
# liczby calkowite zmienno przecinkowe i krotki moga byc elementem zbioru, ale listy slowniki i zbiory juz nie
# oprocz operacji charakterystycznych dla kolekcji zbiory maja kilka charakterystycznych dla siebie dzialan

x = set([1, 2, 3, 4, 2, 2, 1])
print(x)    # zbior jest unikalny - wszelkie duplikaty sa z niego usuwane - powtarzajaca sie dwojki nie zostaja wyswietlone
# setow nie sortujemy bo sortuja sie odgornie
print("Add")
x.add(5)
print(x)
print("Remove")
x.remove(1)
print("2 in x")
print(x)
print(2 in x)
x = set([1, 2, 3, 4, 2, 2, 1])
y = set([1, 7, 8, 9])
print(x | y)    # suma zbiorow x i y
print(x & y)    # czesc wspolna
print(x ^ y)    # roznica symetryczna zbiorow - elementy, ktore wystepuja w jednym lub drugim zbiorze, ale nie w obu
# frozenset - zbior nieedytowalny, niezmienny
z = frozenset(x)
print(z)
# z.add(3) teraz nie zadziala na frozenset

