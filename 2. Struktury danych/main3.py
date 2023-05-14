list = ['burak', 'cukinia', 'pomidor', 'cytryna', 'ananas', 'papryka', 'dynia']

letter = input("Podaj literę: ")

for element in list:
    if element.startswith(letter):
        print(element, end=" ")