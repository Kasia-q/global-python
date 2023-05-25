class Figures:
   def __init__(self, side_A, side_B, height):
      self.sideA = side_A
      self.sideB = side_B
      self.height = height
    
   def kwadrat(self):
       '''Mnoży bok 'a' przez bok 'a' aby uzyskać pole kwadratu'''
       a = self.sideA
       result  = a * a
       return print("Pole kwadratu wynosi:", result)
   
   def prostokat(self):
       '''Mnoży bok 'a' przez bok 'b' aby uzyskać pole prostokąta'''
       a = self.sideA
       b = self.sideB
       result = a * b
       return print("Pole prostokąta wynosi:", result)
   
   def trojkat(self):
       '''Mnoży bok 'a' przez wysokość 'h' i dzieli poprzez 2 aby uzyskać pole trójkąta'''
       a = self.sideA
       h = self.height
       result = (a * h)/2
       return print("Pole trójkąta wynosi:", result)
   
   def rownoleglobok(self):
       '''Mnoży bok 'a' przez wysokość 'h' aby uzyskać pole równoległoboku'''
       a = self.sideA
       h = self.height
       result = a * h
       return print("Pole równoległoboku wynosi:", result)




class Circumference(Figures):
    
    def circ_kwadratu(self):
        '''Mnoży bok 'a' przez 4'''
        a  = self.sideA
        result  = 4 * a
        return print("Obwod kwadratu wynosi:", result)
   
    def circ_prostokata(self):
        '''mnoży bok 'a' przez 2 i dodaje do pomnożonego przez 2 boku 'b' '''
        a = self.sideA
        b = self.sideB
        result = 2 * a + 2 * b
        return print("Obwod prostokąta wynosi:", result)
   
    def circ_trojkata(self):
        '''oblicza bok 'c' i dodaje wszystkie boki do siebie'''
        a = self.sideA
        b = self.sideB
        c = ((a ** 2) + (b ** 2)) ** 0.5
        result = a + b + c
        return print("Obwód trójkąta wynosi:", result)
   
    def circ_rownolegloboku(self):
        '''mnoży bok 'a' przez 2 i dodaje do pomnożonego przez 2 boku 'b' '''
        a = self.sideA
        b = self.sideB
        result = 2 * a + 2 * b
        return print("Obwód równoległoboku wynosi:", result)
   

   



while True:
    print("************************************")
    print("Wybierz figurę, której chcesz obliczyć pole i obwód")
    print("1. Kwadrat")
    print("2. Prostokąt")
    print("3. Trójkąt")
    print("4. Równoległobok")
    print("0. Zamnknij program")

    choice = int(input("Którą operację chcesz wykonać?: "))

    if choice == 1:
        a = int(input("Podaj długość boku kwadratu: "))
        area = Figures(a, 0, 0)
        circ = Circumference(a, 0, 0)
        area.kwadrat()
        circ.circ_kwadratu()
        
    elif choice == 2:
        a = int(input("Podaj długość pierwszego boku: "))
        b = int(input("Podaj długość drugiego boku: "))
        area = Figures(a, b, 0)
        circ = Circumference(a, b, 0)
        area.prostokat()
        circ.circ_prostokata()
    
    elif choice == 3:
        a = int(input("Podaj długość pierwszego boku: "))
        b = int(input("Podaj długość drugiego boku: "))
        h = int(input("Podaj wysokość: "))
        area = Figures(a, 0, h)
        circ = Circumference(a, b, 0)
        area.trojkat()
        circ.circ_trojkata()
        
    elif choice == 4:
        a = int(input("Podaj długość pierwszego boku: "))
        b = int(input("Podaj długość drugiego boku: "))
        h = int(input("Podaj wysokość: "))
        area = Figures(a, 0, h)
        circ = Circumference(a, b, 0)
        area.rownoleglobok()
        circ.circ_rownolegloboku()
        
    elif choice == 0:
        print("******Zakończenie pracy programu******")
        break
