class Czytelnik:
    id: int = 0

    def __init__(self,
                 imie: str, nazwisko: str, miasto: str, rok_urodzenia: int):
        Czytelnik.id += 1

        self.__id = Czytelnik.id
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__miasto = miasto
        self.__rok_urodzenia = rok_urodzenia

    def pobierz_id(self):
        return self.__id
    def pobierz_imie(self):
        return self.__imie
    def pobierz_nazwisko(self):
        return self.__nazwisko
    def pobierz_miasto(self):
        return self.__miasto
    def pobierz_rok_urodzenia(self):
        return self.__rok_urodzenia
    
czytelnik1 = Czytelnik("Wiktoria", "Nowak", "Koszalin", 2001)
czytelnik2 = Czytelnik("Nikodem", "Kamiński", "Koszalin", 1997)
czytelnik3 = Czytelnik("Igor", "Nowicki", "Dąbki", 2004)
czytelnik4 = Czytelnik("Leon", "Mazur", "Darłowo", 1984)
czytelnik5 = Czytelnik("Aleksandra", "Mazurek", "Sianowo", 1993)

print(czytelnik1.pobierz_id(), ".", czytelnik1.pobierz_imie(), czytelnik1.pobierz_nazwisko())