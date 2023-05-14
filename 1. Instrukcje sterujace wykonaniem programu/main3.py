import random


guess = int(input("Zgadnij liczbę podaną przez komputer. Podaj liczbę: "))
number = random.randint(1,100)
tries = 1


while guess != number:
    if guess > number:
        guess = int(input("Za dużo, zgaduj dalej: "))
        tries += 1
    else:
        guess = int(input("Za mało, zgaduj dalej: "))
        tries += 1
print(f"Gratulacje, liczba to {number}. Ilość prób: {tries}")
    
    