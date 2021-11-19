import math


# how to made exception for NameError TypeError in def method not when method is called
def quest1():
    def quest1(a):
        try:
            if isinstance(a, float):
                raise ValueError
            else:
                for potega in range(0, 6):
                    print(math.pow(a, potega))
        except (TypeError, ValueError):
            print("Only integer numbers are allowed!")

    def quest2(promien):
        try:
            print(f"Pole: {round(math.pi * math.pow(promien, 2), 3)}")
            print(f"Obwód: {round(2 * math.pi * promien, 3)}")
        except TypeError:
            print("Only numbers are allowed!")

    def quest3(liczba):
        try:
            print(math.fabs(liczba))
        except TypeError:
            print("Only numbers are allowed!")

    def quest4(x, y):
        try:
            print(math.sqrt(math.pow((y[0] - x[0]), 2) + math.pow((y[1] - x[1]), 2)))
        except TypeError:
            print("You need to pass points with numbers!")


def quest2():
    pass


def quest3():
    lista = []
    while True:
        element = input("Type element to add to list:")
        if element != "":
            lista.append(element)
        else:
            break

    try:
        index = int(input("Pass the index:"))
        if not isinstance(index, int):
            raise ValueError
    except ValueError:
        print("Only integer numbers are allowed for index")
    else:
        try:
            print(lista[index])
        except IndexError:
            print("The number is out of the list range!")


def quest4():
    class Pracownik:
        def __init__(self, imie, nazwisko, zawod, rok_zatrudnienia=2020, wynagrodzenie_podstawowe=2500):
            try:
                if imie.isalpha() and nazwisko.isalpha() and zawod.isalpha():
                    self.imie = imie
                    self.nazwisko = nazwisko
                    self.zawod = zawod
                else:
                    raise ValueError
            except (ValueError, AttributeError):
                print("imie,nazwisko,zawod muszą być napisamy i nie być puste")

            try:
                if wynagrodzenie_podstawowe >= 0 and not isinstance(wynagrodzenie_podstawowe, str):
                    self.wynagrodzenie_podstawowe = wynagrodzenie_podstawowe
                else:
                    raise ValueError
            except (ValueError, TypeError):
                print("Wynagrodzenie musi być liczbą oraz nie byc mniejsza od zera")

            try:
                if isinstance(rok_zatrudnienia, int) and rok_zatrudnienia >= 0:
                    self.rok_zatrudnienia = rok_zatrudnienia
                else:
                    raise ValueError
            except (ValueError, TypeError):
                print("Rok_zatrudnienia musi byc liczba calkowita nie mniejsza od zera")

        def zwroc_wynagrodzenie_podstawowe(self):
            return self.wynagrodzenie_podstawowe

        def oblicz_staz_pracy(self):
            return 2020 - self.rok_zatrudnienia

        def oblicz_wynagrodzenie(self):
            wynagrodzenie_dodatkowe = self.wynagrodzenie_podstawowe
            if self.oblicz_staz_pracy() >= 3:
                for lata in range(self.oblicz_staz_pracy()):
                    wynagrodzenie_dodatkowe += round(int(self.wynagrodzenie_podstawowe * 0.01), 0)
            return wynagrodzenie_dodatkowe

        def __str__(self):
            return f"Pracownik:{self.imie} {self.nazwisko} Zawód:{self.zawod} Staż pracy:{self.oblicz_staz_pracy()}/" \
                   f" Wynagordzenie: {self.oblicz_wynagrodzenie()}"

    class PracownikZNadgodzinami(Pracownik):
        def __init__(self, imie, nazwisko, zawod, rok_zatrudnienia=2020, wynagrodzenie_podstawowe=2500,
                     stawka_za_godzine=20, liczba_godzin=0):
            super().__init__(imie, nazwisko, zawod, rok_zatrudnienia, wynagrodzenie_podstawowe)
            self.stawka_za_godzine = stawka_za_godzine
            self.liczba_godzin = liczba_godzin

        def dodaj_kolejna_godzine(self):
            self.liczba_godzin += 1

        def zeruj_liczbe_godzin(self):
            self.liczba_godzin = 0

        def oblicz_wynagrodzenie_nadgodziny(self):
            return self.stawka_za_godzine * self.liczba_godzin

        def oblicz_pelne_wynagrodzenie(self):
            return self.oblicz_wynagrodzenie() + self.oblicz_wynagrodzenie_nadgodziny()

        def __str__(self):
            return f"Pracownik: {self.imie} {self.nazwisko} Zawód: {self.zawod} Staż pracy:/" \
                   f"{self.oblicz_staz_pracy()} Wynagordzenie: {self.oblicz_pelne_wynagrodzenie()}"


def quest5():
    def calculator(x, y=1):
        try:
            if not isinstance(x, str) and not isinstance(y, str):
                print(f"{x} + {y} = {x + y}")
                print(f"{x} - {y} = {x - y}")
                print(f"{x} * {y} = {x * y}")
                if x == 0 or y == 0:
                    print(print(f"{x} / {y} = 0"))
                else:
                    print(f"{x} / {y} = {x / y}")
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("0")

    calculator(3)


def quest6():
    def mniej_niz(waga, waga_paczki):
        global lzejszepaczki
        try:
            if not isinstance(waga, str) and waga >= 0 and isinstance(waga_paczki, list) and len(waga_paczki) != 0:
                for waga_pacz in waga_paczki:
                    if not isinstance(waga_pacz, str) and waga_pacz >= 0:
                        pass
                    else:
                        raise ValueError
                lzejszepaczki = [paczka for paczka in waga_paczki if paczka < waga]
                print(lzejszepaczki)
                index = input("Podaj Wartosc by poznac jej index w liscie:")
                if not index.isalpha() and int(index) >= 0:
                    if int(index) in waga_paczki:
                        print("W wagach paczek indeks ma nr", waga_paczki.index(int(index)))
                    else:
                        print("Nie ma takiej wartosci w wagach paczek")
                    if int(index) in lzejszepaczki:
                        print("W liscie lzejszych paczek indeks ma nr", lzejszepaczki.index(int(index)))
                    else:
                        print("Nie ma takiej wartosci w liscie lzejszych paczek")
                else:
                    raise ValueError
            else:
                raise ValueError
        except (ValueError):
            print("Podano złe dane")
