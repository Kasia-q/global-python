import random


print("Zgadnij liczbę podaną przez komputer.")

play = True
while play == True:
    tries = 1
    number = random.randint(1,100)
    guess = int(input("Podaj liczbę: "))

    while guess != number:
        if guess > number:
            guess = int(input("Za dużo, zgaduj dalej: "))
            tries += 1
        elif guess < number:
            guess = int(input("Za mało, zgaduj dalej: "))
            tries += 1
            
    print(f"Gratulacje, liczba to {number}. Ilość prób: {tries}")
        
    if input("Czy chcesz zagrać ponownie? (tak/nie): ") != "tak":
        play = False

