# program moze miec te same zmienne co funkcja
a = "jeden"
b = "dwa"

def f():
    global a # global jest dostepne tylko dla funkcji
    a = 1
    b = 2
    print(a, b)

print(a) # a jest "jeden"
f()
print(a) # w tym miejscu a zmienia sie na 1
print("drugi przyklad")
def f1():
    global a # global jest dostepne tylko dla funkcji
    a = 1
    # b = 2
    print(a, b)

print(a) # a jest "jeden"
f1()
print(a) # w tym miejscu a zmienia sie na 1
