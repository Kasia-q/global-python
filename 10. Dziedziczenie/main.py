from abc import ABC, abstractmethod

class Figures(ABC):
    def __init__(self, side_A, side_B, height):
        self.sideA = side_A
        self.sideB = side_B
        self.height = height
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def circumference(self):
        pass


class Kwadrat(Figures):
    def area(self):
        a = self.sideA
        result = a * a
        print("Pole kwadratu wynosi:", result)
    
    def circumference(self):
        a = self.sideA
        result = 4 * a
        print("Obwód kwadratu wynosi:", result)


class Prostokat(Figures):
    def area(self):
        a = self.sideA
        b = self.sideB
        result = a * b
        print("Pole prostokąta wynosi:", result)
    
    def circumference(self):
        a = self.sideA
        b = self.sideB
        result = 2 * a + 2 * b
        print("Obwód prostokąta wynosi:", result)


class Trojkat(Figures):
    def area(self):
        a = self.sideA
        h = self.height
        result = (a * h) / 2
        print("Pole trójkąta wynosi:", result)
    
    def circumference(self):
        a = self.sideA
        b = self.sideB
        c = ((a ** 2) + (b ** 2)) ** 0.5
        result = a + b + c
        print("Obwód trójkąta wynosi:", result)


class Rownoleglobok(Figures):
    def area(self):
        a = self.sideA
        h = self.height
        result = a * h
        print("Pole równoległoboku wynosi:", result)
    
    def circumference(self):
        a = self.sideA
        b = self.sideB
        result = 2 * a + 2 * b
        print("Obwód równoległoboku wynosi:", result)


def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Niepoprawna wartość. Wprowadź liczbę całkowitą.")


def get_choice():
    while True:
        choice = get_number_input("Którą operację chcesz wykonać?: ")
        if 0 <= choice <= 4:
            return choice
        else:
            print("Niepoprawny wybór. Wybierz liczbę od 0 do 4.")


while True:
    print("************************************")
    print("Wybierz figurę, której chcesz obliczyć pole i obwód")
    print("1. Kwadrat")
    print("2. Prostokąt")
    print("3. Trójkąt")
    print("4. Równoległobok")
    print("0. Zamknij program")

    choice = get_choice()

    if choice == 1:
        a = get_number_input("Podaj długość boku kwadratu: ")
        figure = Kwadrat(a, 0, 0)
        figure.area()
        figure.circumference()
        
    elif choice == 2:
        a = get_number_input("Podaj długość pierwszego boku: ")
        b = get_number_input("Podaj długość drugiego boku: ")
        figure = Prostokat(a, b, 0)
        figure.area()
        figure.circumference()
    
    elif choice == 3:
        a = get_number_input("Podaj długość pierwszego boku: ")
        b = get_number_input("Podaj długość drugiego boku: ")
        h = get_number_input("Podaj wysokość: ")
        figure = Trojkat(a, b, h)
        figure.area()
        figure.circumference()
        
    elif choice == 4:
        a = get_number_input("Podaj długość pierwszego boku: ")
        b = get_number_input("Podaj długość drugiego boku: ")
        h = get_number_input("Podaj wysokość: ")
        figure = Rownoleglobok(a, b, h)
        figure.area()
        figure.circumference()
        
    elif choice == 0:
        print("******Zakończenie pracy programu******")
        break