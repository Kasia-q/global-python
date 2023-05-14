user_age = int(input("Podaj swój wiek: "))
czyA2 = True if input("Czy masz prawo jazdy kat. A2? (t/n): ") \
    in ('t', 'ta', 'tak', 'T') else False
    
odIluA2 = 0


if czyA2:
    odIluA2 = int(input("Jak długo masz A2. Podaj ilość lat: "))
    
        

if user_age >= 24 or odIluA2 >=2:
    print("Możesz przystąpić do egzaminu na prawo jazdy kat. A")
else:
    print("Nie możesz")
    
# do poprawy