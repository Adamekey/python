x = [1, 2, 3,]
y = [2, "dwa", "2", [1, 2, 3]]
z = []
'''len dlugosc
print(len(x))
print(len(y))
print(len(z))
'''
# indeksy list - wazne
print(x[0])
print(x[2])
print(y[3])
# ujemne indeksowanie odnosi sie do numeracji od konca listy
print(y[-1])
# wycinki na liscie slysing
print(y[1:-1])
print(x[0:2])
print(x[:2]) # mozna tez tak podawac zeby pobralo wszystko od poczatku do pozycji 2

# zmiana indeksu
x[1] = "2"
print(x)
x[len(x):] = [4, 5, 6] # python lapie cala liste i dodaje na koncu elementy mozna uzyc metody .append
print(x)
x.append("7")
print(x)
# scalanie list .extend
x.extend(y)
print(x)
# insert
x.insert(2, "Witaj")
print(x)
# del - usuwanie
del x[1]
print(x)
# remove rowniez usuwanie ale konkretnych wartosci - pierwszego wystapienia danego obiektu, jesli obiektu nie znajdzie wyswietli blad - nalezy go wylapac
x.remove("Witaj")
print(x)
# reverse - zamienia kolejnoscia elementy listy
x.reverse()
print(x)
# sort - sortowanie ale tylko tych samych typow danych ale takich ktore daja sie ze soba porownywac
s = [11, 22, 233, 40]
s.sort()
print(s)
# sorted - zwraca posortowana sekwencje i zwraca parametry, reverse=True
s1 = sorted(s, reverse=True)
print(s1)

# sprawdzanie czy cos sie znajduje True albo False
z = [0]
print(2 in z) # czy 2 znajduje sie w liscie z
print(0 in z)
r = [3] + [55, 56, 57]
print(r)
r = [3] + [55, 56, 57] * 2
print(r)

print(min(r))
print(max(r))

#count liczy wystapienia w liscie
c = z.count(0)
print(c)