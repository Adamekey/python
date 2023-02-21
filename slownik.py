# slowniki - sa bardzo wazne, caly python zbudowany jest na slownikach
# taka troche tablica w innych jezykach
# do wartosci na listach uzyskujemy dostep przez liczby - indeksy
# do wartosci w slowniku uzyskujemy dostep poprzez liczby calkowite, lancuchy znakow lub inne obiekty zwane kluczami
# klucze wwskazuja gdzie w slowniku mozna znalezc dana wartosc - klucz jest unikatowy, ale mozna go podmienic
# zarowno listy jak i slowniki moga przechowywac wartosci roznych typow
# wartosci w slownikach nie sa uporzadkowane
x = []  # lista
y ={}   # slownik
y[0] = "Witaj"
y[1] = " Do zobaczenia"
print(y)
print(y[0])     # sama wartosc klucza - klucza juz nie zobaczymy
y = {"pierwszy": "1", 2: "2"}
print(y)
y[0] = "Witaj"
y[1] = " Do zobaczenia"
print(y)
print(f"Zawartosc klucza o nazwie pierwszy to {y['pierwszy']}")
# metody keys zwraca iteracje wszystkich kluczy
print(y.keys())
print(y.values())
print(y.items()) # pokazuje w elegancki sposob krotki slownika klucz-wartosc
del y[2]    # usuwanie
print(y)
print('pierwszy' in y)  # sprawdza czy dany klucz znajduje sie w slowniku
# get zwraca wartosc powiazana z kluczem o ile slownik takowa posiada, gdyby jej nie bylo to mozna ja zastapic wartoscia domyslna
print(y.get('1'))
print(y.get('1', "Brak wartosci"))