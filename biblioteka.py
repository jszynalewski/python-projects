class Pozycja:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        self.wypozyczona = False

    def wypozycz(self):
        if self.wypozyczona == False:
            self.wypozyczona = True
            print("Wypożyczono")
        else:
            print("Pozycja niedostępna")

    def zwroc(self):
        if self.wypozyczona == True:
            self.wypozyczona = False
            print("Zwrócono")
        else:
            print("Ta pozycja nie była wypożyczona")
    
    def status(self):
        return "wypożyczona" if self.wypozyczona else "dostępna"


    def info(self):
        print(f"Tytuł: {self.tytul} Autor: {self.autor} Status: {self.status()}")

class Ksiazka(Pozycja):
    def __init__(self, tytul, autor, liczba_stron):
        super().__init__(tytul, autor)
        self.liczba_stron = liczba_stron

    def info(self):
        print(f"Tytuł: {self.tytul} Autor: {self.autor} Status: {self.status()} Liczba stron: {self.liczba_stron} ")

class Ebook(Pozycja):
    def __init__(self, tytul, autor, liczba_stron, rozmiar_mb):
        super().__init__(tytul, autor)
        self.liczba_stron = liczba_stron
        self.rozmiar_mb = rozmiar_mb

    def info(self):
        print(f"Tytuł: {self.tytul} Autor: {self.autor} Status: {self.status()} Liczba stron: {self.liczba_stron} Rozmiar mb {self.rozmiar_mb}")


biblioteka = []




while True: 
    print("/n ----BIBLIOTEKA----")
    print("1. Dodaj książkę")
    print("2. Dodaj Ebook")
    print("3. Wyświetl wszystkie")
    print("4. Wypożycz")
    print("5. Zwróć")
    print("6. Wyjście")
    choice = input("Wybierz operację: ")
    match choice:
        case "1":
            tytul = input("Wprowadź tytuł: ")
            autor = input("Wprowadź autora: ")
            try:
                liczba_stron = int(input("Wprowadź liczbę stron: "))
            except ValueError:
                print("Liczba stron musi być liczbą")
                continue
            nowa_książka = Ksiazka(tytul, autor, liczba_stron)
            biblioteka.append(nowa_książka)
        case "2":
            tytul = input("Wprowadź tytuł: ")
            autor = input("Wprowadź autora: ")
            try:
                liczba_stron = int(input("Wprowadź liczbę stron: "))
            except ValueError:
                print("Liczba stron musi być liczbą")
                continue
            try:
                rozmiar_mb = float(input("Wprowadź rozmiar pliku: "))
            except ValueError:
                print("Rozmiar pliku musi być liczbą")
                continue
            nowy_ebook = Ebook(tytul, autor, liczba_stron, rozmiar_mb)
            biblioteka.append(nowy_ebook)
        case "3":
            for pozycja in biblioteka:
                pozycja.info()
        case "4": 
            for i, pozycja in enumerate(biblioteka):
                print(f"{i+1} {pozycja.tytul}")
            try:
                wybor = int(input("Wybierz numer książki: "))
                biblioteka[wybor - 1].wypozycz()
            except ValueError:
                print("Wybór książki polega na podaniu jej id")
            except IndexError:
                print("Niepoprawny index")
        case "5": 
            for i, pozycja in enumerate(biblioteka):
                if pozycja.wypozyczona:
                    print(f"{i+1} {pozycja.tytul}")
            try:
                wybor = int(input("Wybierz numer książki: "))
                biblioteka[wybor - 1].zwroc()
            except ValueError:
                print("Wybór książki polega na podaniu jej id")
            except IndexError:
                print("Niepoprawny index")
        case "6":
            break
        case _:
            print("Zła opcja")



            



