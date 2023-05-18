def dodawanie(a,b):
    '''pobiera liczby od użytkownika i wyświetla ich sumę'''
    wynik = a + b
    print(f"{a} + {b} = {wynik}")
    print("************************************")

def odejmowanie(a,b):
    '''pobiera liczby od użytkownika i wyświetla ich różnicę'''
    wynik = a - b
    print(f"{a} - {b} = {wynik}")
    print("************************************")

def mnozenie(a,b):
    '''pobiera liczby od użytkownika i wyświetla ich iloczyn'''
    wynik = a * b
    print(f"{a} * {b} = {wynik}")
    print("************************************")

def dzielenie(a,b):
    '''pobiera liczby od użytkownika i wyświetla ich iloraz'''
    if b == 0:
        print("Mnożenie przez 0 jest niemożliwe.")
        exit
    wynik = a / b
    print(f"{a} : {b} = {wynik}")
    print("************************************")
