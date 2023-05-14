word = input("Podaj słowo: ")
if word[::-1].lower() == word.lower():
    print(f"Słowo jest palindromem.")
else:
    print(f"Słowo nie jest palindromem.")