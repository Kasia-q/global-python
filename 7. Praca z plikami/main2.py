from os import path
import random

combination_list = int(input("Podaj ilość kombinacji: "))
names = []
surnames = []
dir_path = path.dirname(__file__)
nazwa_pliku = 'imiona.txt'
data_path = path.join(dir_path, nazwa_pliku)


with open(data_path, 'r', encoding='utf-8') as plik:
    linie = plik.readlines()
    lista_imion = linie
    for i in range(0, len(lista_imion)-1, +1):
        lista_imion[i].split()
        lista_imion[i] = "".join(lista_imion[i][:-1])
        names.append(lista_imion[i])

dir_path = path.dirname(__file__)
nazwa_pliku = 'nazwiska.txt'
data_path = path.join(dir_path, nazwa_pliku)
with open(data_path, 'r', encoding='utf-8') as plik:
    linie = plik.readlines()
    lista_nazwisk = linie
    for i in range(0, len(lista_nazwisk)-1, +1):
        lista_nazwisk[i].split()
        lista_nazwisk[i] = "".join(lista_nazwisk[i][:-1])
        surnames.append(lista_nazwisk[i])

i = 1
losowe_dane = []
while i != combination_list:
    random_name = random.choice(names)
    random_surname = random.choice(surnames)
    kombinacja = random_name + " " + random_surname
    if kombinacja in losowe_dane:
        continue
    else: 
        losowe_dane.append(kombinacja)
        i += 1

with open("losowe_imiona.txt", "w", encoding='utf-8') as plik:
    for random_name in losowe_dane:
        plik.write(random_name + ', ')

with open("losowe_imiona.txt", 'r', encoding='utf-8') as plik:
    linie = plik.readlines()
    print(linie) 