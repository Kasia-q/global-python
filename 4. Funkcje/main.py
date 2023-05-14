def dodawanie(a:float,b:float):
    '''pobiera liczby od użytkownika i wyświetla ich sumę'''
    wynik:float = a + b
    print(f"{a} + {b} = {wynik}")
    print("************************************")

def odejmowanie(a:float,b:float):
    '''pobiera liczby od użytkownika i wyświetla ich różnicę'''
    wynik:float = a - b
    print(f"{a} - {b} = {wynik}")
    print("************************************")

def mnozenie(a:float,b:float):
    '''pobiera liczby od użytkownika i wyświetla ich iloczyn'''
    wynik:float = a * b
    print(f"{a} * {b} = {wynik}")
    print("************************************")

def dzielenie(a:float,b:float):
    '''pobiera liczby od użytkownika i wyświetla ich iloraz'''
    if b == 0:
        print("Mnożenie przez 0 jest niemożliwe.")
        exit
    wynik:float = a / b
    print(f"{a} : {b} = {wynik}")
    print("************************************")


while True:
    print("************************************")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("0. Zamnknij program")

    choice = int(input("Którą operację chcesz wykonać?: "))

    if choice == 1:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        dodawanie(a, b)
    elif choice == 2:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        odejmowanie(a, b)
    elif choice == 3:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        mnozenie(a, b)
    elif choice == 4:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        dzielenie(a, b)
    elif choice == 0:
        print("******Zakończenie pracy programu******")
        break



