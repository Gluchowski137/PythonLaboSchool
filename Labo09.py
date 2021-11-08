import random


def quest1():
    class Wagon:
        def __init__(self, nr_wagonu, maks_miejsc=80):
            self.lista_pasazerow = []
            self.lista_wolnych_miejsc = [liczba for liczba in range(1, maks_miejsc + 1)]
            self.maks_miejsc = maks_miejsc
            self.nr_wagonu = nr_wagonu
            self.miejsc_w_wagonie = 0

        def wyswietl_dostepne_miejsca(self):
            print(self.lista_wolnych_miejsc)

        def zwroc_ile_zajetych(self):
            return self.miejsc_w_wagonie

        def zwroc_miesjce(self):
            if len(self.lista_wolnych_miejsc) != 0:
                return random.choice(self.lista_wolnych_miejsc)
            else:
                return -1

        def __str__(self):
            return f"{self.nr_wagonu} {self.maks_miejsc} {self.miejsc_w_wagonie} {self.lista_wolnych_miejsc}"

        def wyswietl_pasazerow(self):
            print([pasazer.imie for pasazer in self.lista_pasazerow])

        def podaj_czy_wolne_miesca(self):
            if len(self.lista_wolnych_miejsc) != 0:
                return False
            else:
                return True

        def czy_wolne(self, nr_miejsca):
            if nr_miejsca in self.lista_wolnych_miejsc:
                return True
            else:
                return False

        def usun_pasazera(self, pasazer):
            if pasazer in self.lista_pasazerow:
                self.lista_pasazerow.remove(pasazer)
                self.lista_wolnych_miejsc.append(pasazer.miejsce)
                print(f"Usunieto pasazera {pasazer.imie} z wagonu nr {self.nr_wagonu}")
            else:
                print("Nie mozna usunac pasazera ktory nie zostal dodany")

        def dodaj_pasazera(self, *pasazery):
            for pasazer in pasazery:
                self.lista_pasazerow.append(pasazer)

        def __del__(self):
            print("Wywołano destruktor dla Wagon")

    class Pasazer():

        def __init__(self, imie, nazwisko, nr_wagonu, miejsce):
            self.imie = imie
            self.nazwisko = nazwisko
            self.__nr_wagonu = nr_wagonu
            self.miejsce = miejsce
            if self.__nr_wagonu == 1:
                wagony[0].dodaj_pasazera(self)
            elif self.__nr_wagonu == 2:
                wagony[1].dodaj_pasazera(self)
            else:
                print("Nie ma takiego wagonu")

        @staticmethod
        def stworz_pasazera(imie, nazwisko, nr_wagon, miejsce):
            zapelnione = 0
            for wagon in wagony:
                if len(wagon.lista_wolnych_miejsc) == 0:
                    zapelnione += 1
            if zapelnione != len(wagony):
                if len(wagony[nr_wagon - 1].lista_wolnych_miejsc) != 0:
                    if miejsce in wagony[nr_wagon - 1].lista_wolnych_miejsc:
                        for miejsce_wolne in wagony[nr_wagon - 1].lista_wolnych_miejsc:
                            if miejsce_wolne == miejsce:
                                wagony[nr_wagon - 1].lista_wolnych_miejsc.remove(miejsce_wolne)
                                for wagon in wagony:
                                    wagon.miejsc_w_wagonie += 1
                                return Pasazer(imie, nazwisko, nr_wagon, miejsce)
                    else:
                        nowe_miesjce = random.choice(wagony[nr_wagon - 1].lista_wolnych_miejsc)
                        print(
                            f"{imie} miejsce {miejsce} jest zajete lub jest nieprawidłowe. Miejsce o nr {nowe_miesjce} zostało tobie przydzielone")
                        miejsce = nowe_miesjce
                        wagony[nr_wagon - 1].lista_wolnych_miejsc.remove(miejsce)
                        for wagon in wagony:
                            wagon.miejsc_w_wagonie += 1
                        return Pasazer(imie, nazwisko, nr_wagon, miejsce)
                else:
                    print(f"{imie} Nie ma miejsc w tym wagonie")
                    for wagon in wagony:
                        if len(wagon.lista_wolnych_miejsc) != 0:
                            nowe_miesjce = random.choice(wagon.lista_wolnych_miejsc)
                            print(
                                f"{imie} został tobie przydzielony wagon o nr {wagon.nr_wagonu} z miesjcem o nr {nowe_miesjce}")
                            miejsce = nowe_miesjce
                            nr_wagon = wagon.nr_wagonu
                            wagony[nr_wagon - 1].lista_wolnych_miejsc.remove(miejsce)
                            for wagon in wagony:
                                wagon.miejsc_w_wagonie += 1
                            return Pasazer(imie, nazwisko, nr_wagon, miejsce)
            else:
                print(f"{imie} wszystkie wagony są zapełnione wybierz się znami kiedy indziej")

        def zwroc_numer_wagonu(self):
            return self.__nr_wagonu

        def __str__(self):
            return f"{self.imie} {self.nazwisko} {self.__nr_wagonu} {self.miejsce}"

        def __del__(self):
            print("Wywołano destruktor dla Pasażer")

    wagony = [Wagon(1, 0), Wagon(2, 2)]
    pasazer1 = Pasazer.stworz_pasazera("Wojtek", "kowalski", 1, 20)
    pasazer2 = Pasazer.stworz_pasazera("Kamil", "kowalski", 1, 7)
    pasazer3 = Pasazer.stworz_pasazera("maciek", "kowalski", 2, 10)

    wagony[1].wyswietl_pasazerow()
    print(wagony[0].zwroc_ile_zajetych())
    print(wagony[0].czy_wolne(3))
    print(pasazer1)
    Wagon.usun_pasazera(wagony[Pasazer.zwroc_numer_wagonu(pasazer1) - 1], pasazer3)


quest1()
