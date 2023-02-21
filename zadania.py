txt = '''
Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’,
liczby podzielne przez 5, zastąp słowem ‘Buzz’,
natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.
'''
print(txt)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
txt = '''
Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście.
'''
print(txt)

lista = [ 10, 4, 6, 8, 22, 101]
print(min(lista))
print(max(lista))
# posortujemy liste
lista.sort()
print(lista)

txt = '''
Bardzo popularnym zadaniem, szlifującym nasz język, jest program do analizy ciągu znaków, czyli przykładowo zliczenia liczby słów czy też znaków.
Mamy podany ciąg S. Np „Ala ma kota”. W ramach zadania możemy zostać poproszeni o jedno, lub więcej z poniższych:
1. zliczyć wyrazy. W naszym przypadku będzie ich 3
2. zliczyć litery. Będzie ich 9
3. zbadać częstotliwość występowania liter. a – 3, l – 1, m 1, k – 1, t – 1
'''
print(txt)
s = 'Ala ma kota'
print(s)
print(f"Zadanie 1:\n")
l = " "
j = 0
for i in s:
    if i is l:
        j += 1
print(f"Mamy {j+1} wyrazow\n")

print(f"Zadanie 2:\n")
k = 0
for i in s:
    k += 1
print(f"Jest {k - j} liter\n")

print(f"Zadanie 3:\n")
a = "a"
j = 0
for i in s:
    if i == a:
        j += 1
print(f"Mamy {j} liter/y a.\n")
