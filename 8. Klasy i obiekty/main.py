class Czytelnik:
    id: int = 0

    def __init__(self,
                 imie: str, nazwisko: str, miasto: str, rok_urodzenia: int):
        Czytelnik.id += 1

        self.id = Czytelnik.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.miasto = miasto
        self.rok_urodzenia = rok_urodzenia
        
czytelnik1 = Czytelnik("Wiktoria", "Nowak", "Koszalin", 2001)
czytelnik2 = Czytelnik("Nikodem", "Kamiński", "Koszalin", 1997)
czytelnik3 = Czytelnik("Igor", "Nowicki", "Dąbki", 2004)
czytelnik4 = Czytelnik("Leon", "Mazur", "Darłowo", 1984)
czytelnik5 = Czytelnik("Aleksandra", "Mazurek", "Sianowo", 1993)