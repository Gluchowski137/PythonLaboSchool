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


def quest2():
    class Samolot:
        liczba_samolotow = 0

        def __init__(self, nr_id, maks_miejsc_1_klasa=40, maks_miejsc_2_klasa=120):
            self.lista_pasazerow_1_klasa = []
            self.lista_pasazerow_2_klasa = []
            self.maks_miejsc_1_klasa = maks_miejsc_1_klasa
            self.maks_miejsc_2_klasa = maks_miejsc_2_klasa
            self.nr_id = nr_id
            self.lista_wolnych_miejsc_1kl = [miejsce for miejsce in range(1, self.maks_miejsc_1_klasa)]
            self.lista_wolnych_miejsc_2kl = [miejsce for miejsce in range(1, self.maks_miejsc_2_klasa)]
            self.liczba_samolotow += 1

        def wyswietl_dostepne_miesjca_1kl(self):
            self.lista_wolnych_miejsc_1kl.sort()
            print(self.lista_wolnych_miejsc_1kl)

        def wyswietl_dostepne_miesjca_2kl(self):
            self.lista_wolnych_miejsc_2kl.sort()
            print(self.lista_wolnych_miejsc_2kl)

        def zwroc_ile_zajetych_1kl(self):
            return len(self.lista_pasazerow_1_klasa)

        def zwroc_ile_zajetych_2kl(self):
            return len(self.lista_pasazerow_2_klasa)

        def zwroc_miesjce_1kl(self):
            return random.choice(self.lista_wolnych_miejsc_1kl) if self.podaj_czy_wolne_miejsca_1kl() else -1

        def zwroc_miesjce_2kl(self):
            return random.choice(self.lista_wolnych_miejsc_2kl) if self.podaj_czy_wolne_miejsca_2kl() else -1

        def dodaj_pasazera(self, pasazer):
            if pasazer.klasa == 1:
                self.lista_pasazerow_1_klasa.append(pasazer)
                self.lista_wolnych_miejsc_1kl.remove(pasazer.miejsce)
            else:
                self.lista_pasazerow_2_klasa.append(pasazer)
                self.lista_wolnych_miejsc_2kl.remove(pasazer.miejsce)

        def __str__(self):
            return f"{self.nr_id} Wszyskie miesjca:{len(self.lista_pasazerow_1_klasa) + len(self.lista_pasazerow_2_klasa)} Zajete: 1klasa{len(self.lista_pasazerow_1_klasa)} 2klasa {len(self.lista_pasazerow_2_klasa)} Wolne: 1klasa {len(self.lista_wolnych_miejsc_1kl)} 2klasa {len(self.lista_wolnych_miejsc_2kl)}"

        def wyswietl_pasazerow_1kl(self):
            print([pasazer.imie for pasazer in self.lista_pasazerow_1_klasa])

        def wyswietl_pasazerow_2kl(self):
            print([pasazer.imie for pasazer in self.lista_pasazerow_2_klasa])

        def wyswietl_pasazerow(self):
            print([pasazer.imie for pasazer in self.lista_pasazerow_1_klasa],
                  [pasazer.imie for pasazer in self.lista_pasazerow_2_klasa])

        def podaj_czy_wolne_miejsca_1kl(self):
            return True if len(self.lista_wolnych_miejsc_1kl) != 0 else False

        def podaj_czy_wolne_miejsca_2kl(self):
            return True if len(self.lista_wolnych_miejsc_2kl) != 0 else False

        def czy_wolne(self, nr, klasa):
            if klasa == 1:
                return True if nr in self.lista_wolnych_miejsc_1kl else False
            else:
                return True if nr in self.lista_wolnych_miejsc_2kl else False

        def usun_pasazera(self, pasazer):
            if pasazer.klasa == 1:
                self.lista_pasazerow_1_klasa.remove(pasazer)
                self.lista_wolnych_miejsc_1kl.append(pasazer.miejsce)
            else:
                self.lista_pasazerow_2_klasa.remove(pasazer)
                self.lista_wolnych_miejsc_2kl.append(pasazer.miejsce)

        def __del__(self):
            print("Wywołano destruktor dla Samolot")

    class PasazerSamolotu:
        def __init__(self, imie, nazwisko, miejsce, klasa, samolot):
            self.imie = imie
            self.nazwisko = nazwisko
            self.miejsce = miejsce
            self.klasa = klasa
            self.samolot = samolot
            Samolot.dodaj_pasazera(samolot, self)

        def zwroc_numer_miejsca(self):
            return self.miejsce

        def __str__(self):
            return self.imie, self.nazwisko, "Miejsce", self.miejsce, "Klasa", self.klasa

        def __del__(self):
            print("Wywołano destruktor dla PasażerSamolotu")

    class Lot:

        def __init__(self, cena_klasa_1, cena_klasa_2):
            self.cena_klasa_1 = cena_klasa_1
            self.cena_klasa_2 = cena_klasa_2
            self.samoloty = []
            self.przychod_za_lot = 0
            self.wszyscy_pasazerowie = []

        def oblicz_cene_biletu(self, pasazer):
            if pasazer.klasa == 1:
                print(f"Pasazer {pasazer.imie} {pasazer.nazwisko} musi zaplaci {self.cena_klasa_1} zł za bilet")
                return self.cena_klasa_1
            else:
                print(f"Pasazer {pasazer.imie} {pasazer.nazwisko} musi zaplaci {self.cena_klasa_2} zł za bilet")
                return self.cena_klasa_2

        def zwroc_pasazera_o_imieniu_i_nazwisku(self, imie, nazwisko):
            for pasazer in self.wszyscy_pasazerowie:
                if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
                    return pasazer

        def ile_samolotow(self):
            print(len(self.samoloty))

        def stworz_samolot(self, nr_id, maks_miejsc_1_klasa=40, maks_miejsc_2_klasa=120):
            self.samoloty.append(Samolot(nr_id, maks_miejsc_1_klasa, maks_miejsc_2_klasa))

        def stworz_pasazera_samolotu(self, imie, nazwisko, miejsce, klasa, samolot):
            self.wszyscy_pasazerowie.append(
                PasazerSamolotu(imie, nazwisko, miejsce, klasa, self.zwroc_samolot_po_nr_id(samolot)))

        def usun_pasazera(self, pasazer):
            Samolot.usun_pasazera(pasazer.samolot, pasazer)
            self.wszyscy_pasazerowie.remove(pasazer)

        def zwroc_przychod_za_lot(self):
            for pasazer in self.wszyscy_pasazerowie:
                self.przychod_za_lot += self.oblicz_cene_biletu(pasazer)
            return self.przychod_za_lot

        def zwroc_samolot_po_nr_id(self, nr_id):
            for samolot in self.samoloty:
                if samolot.nr_id == nr_id:
                    return samolot

        def __del__(self):
            print("Wywołano destruktor dla Lot")

    lot = Lot(500, 100)
    lot.stworz_samolot(320)
    lot.stworz_samolot(123)
    lot.stworz_pasazera_samolotu("wojtek", "Kowalski", 3, 1, 320)
    lot.stworz_pasazera_samolotu("robert", "walski", 5, 2, 123)
    lot.stworz_pasazera_samolotu("kamil", "alski", 3, 2, 320)
    lot.stworz_pasazera_samolotu("Stasiek", "Kowal", 4, 1, 123)
    print(lot.zwroc_przychod_za_lot())
    lot.oblicz_cene_biletu(lot.zwroc_pasazera_o_imieniu_i_nazwisku("kamil", "alski"))
    lot.ile_samolotow()
    Samolot.wyswietl_pasazerow_1kl(lot.zwroc_samolot_po_nr_id(123))
    Samolot.wyswietl_pasazerow(lot.zwroc_samolot_po_nr_id(320))
    print(Samolot.czy_wolne(lot.zwroc_samolot_po_nr_id(320), 4, 2))
    lot.usun_pasazera(lot.zwroc_pasazera_o_imieniu_i_nazwisku("Stasiek", "Kowal"))
    Samolot.wyswietl_dostepne_miesjca_1kl(lot.zwroc_samolot_po_nr_id(123))
