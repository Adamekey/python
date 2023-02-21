licznik = 12
user = 'Tomek'

#wypisz tekst: "Czesc Tomek, masz 12 wiadomosci w skrzynce"

tekst = '''
        Tutaj tytul
    tutaj tresc artykulu
        podpis
        
'''
print(tekst)

print('Czesc %s' % user) #%s zainicjowal string user sa tez %d i %f
print('Czesc %s, masz %d wiadomosci w skrzynce' %(user, licznik))
print('Czesc %(name)s, masz %(count)d wiadomosci w skrzynce' % {'name': user, 'count': licznik})

print('Czesc {}, masz {} wiadomosci w skrzynce' .format(user, licznik))
print('Czesc {name}, masz {count} wiadomosci w skrzynce' .format(name=user, count=licznik)) #nowa metoda

#interpolaca lancuchow
print(f'Czesc {user}, masz {licznik} wiadomosci w skrzynce')
print(f'Masz wiadomosci w skrzynce: {licznik+3} lub {10+5}')
