import math
import random


def quest1(a):
    for potega in range(0, 6):
        print(math.pow(a, potega))


def quest2(promien):
    print(f"Pole: {round(math.pi * math.pow(promien, 2), 3)}")
    print(f"Obwód: {round(2 * math.pi * promien, 3)}")


def quest3(liczba):
    print(math.fabs(liczba))


def quest4(x, y):
    print(math.sqrt(math.pow((y[0] - x[0]), 2) + math.pow((y[1] - x[1]), 2)))


def quest5():
    moneta = ("Orzeł", "Reszka")
    czy_losowac = input(f"Losuj: 1 Zakończ: Wszystko inne\nCo robisz?: ")
    if czy_losowac == "1":
        print(random.choice(moneta))
        quest5()


def quest6():
    class Moneta:
        def __init__(self):
            self.czy_reszka = random.choice([True, False])

        def __str__(self):
            if self.czy_reszka == True:
                return "Reszka"
            else:
                return "Orzeł"

        def rzut_moneta(self):
            self.czy_reszka = random.choice([True, False])

        def odwroc(self):
            if self.czy_reszka == True:
                self.czy_reszka = False
            else:
                self.czy_reszka = True


def quest7():
    losowa_liczba = random.randint(1, 25)
    print(losowa_liczba)
    for proba in range(15):
        liczba_od_uzytkownika = int(input("Podaj liczbe:"))
        if liczba_od_uzytkownika == losowa_liczba:
            print(f"Dobrze! Ilość prób:{proba + 1}")
            break
        else:
            if proba == 14:
                print("Wszystkie próby zostały wykorzystane!")
            else:
                print("Źle! Spróbuj jeszcze raz!")


def quest8():
    class DuzyLotek:
        def __init__(self):
            self.lista = []
            for miejsce in range(6):
                self.lista.append(random.randint(1, 100))

        def __str__(self):
            return f"{self.lista}"

        def nowe_losowanie(self):
            self.lista.clear()
            for miejsce in range(6):
                self.lista.append(random.randint(1, 100))

        def czy_na_liscie(self, liczba):
            if liczba in self.lista:
                print(f"Liczba {liczba} jest w liscie")
            else:
                print(f"Liczba {liczba} nie jest w liscie")
