from os import path

dir_path = path.dirname(__file__)
nazwa_pliku = 'tekst.txt'
data_path = path.join(dir_path, nazwa_pliku)


if not path.exists(data_path):
    exit()

with open(data_path, 'r', encoding='utf-8') as plik:
    lines = plik.readlines()
    plik.close()

    slowa = []
    for line in lines:
        slowa += line.split()
    
    for i in range(len(slowa)):
        if "." in slowa[i]:
            slowa[i] = slowa[i].replace(".", "")
        if "," in slowa[i]:
            slowa[i] = slowa[i].replace(",", "")
        if ";" in slowa[i]:
            slowa[i] = slowa[i].replace(";", "")

    print(f"Liczba słów w tym tekście: {len(slowa)}")
    
    konc_litera = []
    for slowo in slowa:
        litera = slowo[-1]
        if litera not in konc_litera and litera.isalpha():
            konc_litera.append(litera)
            
    stats = {}
    for litera in konc_litera:
        stats[litera] = sum(slowo.endswith((litera)) for slowo in slowa)
        
    print(stats) 