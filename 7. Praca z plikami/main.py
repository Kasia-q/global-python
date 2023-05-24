from os import path

dir_path = path.dirname(__file__)
nazwa_pliku = 'tekst.txt'
data_path = path.join(dir_path, nazwa_pliku)

with open(data_path, 'r', encoding='utf-8') as plik:
    lines = plik.readlines()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "u", "p", "r", "s", "t", "u", "w", "y", "z", "x"]
    result = 0

    x = lines[0].split()
    y = lines[2].split()
    z = lines[4].split()
    lista_slow = x + y + z
    
    for i in range(0, len(lista_slow)-1, +1):
        lista_slow[i].split()
        if lista_slow[i].endswith(",") or lista_slow[i].endswith("."):
            lista_slow[i].split()
            lista_slow[i] = ''.join(lista_slow[i][:-1])
    print(lista_slow)
    print(f"Liczba słów w tym tekście: {len(lista_slow)}")
    
    for i in alphabet:
        for j in lista_slow:
            if j.endswith(i):
                result = result + 1
            else:
                continue
        if result > 0:
            print(f"Liczba wyrazów kończąca się na literę {i}: {result}")
            result = 0
        else:
            result = 0