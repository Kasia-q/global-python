import module

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
        module.dodawanie(a, b)
    elif choice == 2:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        module.odejmowanie(a, b)
    elif choice == 3:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        module.mnozenie(a, b)
    elif choice == 4:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        module.dzielenie(a, b)
    elif choice == 0:
        print("******Zakończenie pracy programu******")
        break

