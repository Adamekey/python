# dwie petle wystarczajace do pracy z programowaniem for i while
# for program powtarza petle z gory okreslona ilosc razy
# while python powtarza kod w petli dopoki warunek pozostaje prawda
'''
print("1")
print("2")
print("3")
print("4")
print("5")
'''
'''
lista = [1, 2, 3, 4, 5]
slowo = "Adam"

for i in lista:
    print(i)
for i in slowo:
    print(i)
'''
licznik = 0
#while licznik < 10:
#    print(licznik)
#    licznik += 1

while True:
    licznik = licznik + 1
    print(licznik)
    if licznik > 7:
        print("Wychodzimy z petli... breakiem")
        break #hamulec dla petli
print("Petla zostala zakonczona")

num = 10
while num < 20:
    num = num + 1
    if num == 15:
        continue
    print("Aktualny numer", num)
print("Poza petla")