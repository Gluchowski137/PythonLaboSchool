def quest1():
    class Konto:
        def __init__(self, imie, nazwisko, nr_konta, saldo, debet=0):
            self.imie = imie
            self.nazwisko = nazwisko
            self.nr_konta = nr_konta
            self.saldo = 0
            self.debet = debet
            self.oprocentowanie = 2

        def wyswietl(self):
            print(
                f"Imie: {self.imie}\nNazwisko: {self.nazwisko}\nNrKonta: {self.nr_konta}\nSaldo: {self.saldo}\nDebet: {self.debet}\nOprocentowanie: {self.oprocentowanie}%")

        def zwroc_stan_konta(self):
            return self.saldo

        def zwieksz_saldo(self, kwota):
            self.saldo += kwota
            print(f"Stan konta został zwiekszony o {kwota} teraz wynosi {self.saldo}")

        def czy_mozliwa_wyplata(self, kwota):
            if self.saldo - kwota >= -1 * self.debet:
                return True
            else:
                return False

        def wyplac(self, kwota):
            if self.czy_mozliwa_wyplata(kwota):
                self.saldo -= kwota
                print("Wypłacono")
            else:
                print("Nie mozna wyplacic")

        def zwroc_dane(self):
            print(f"{self.imie} {self.nazwisko} {self.nr_konta} {self.saldo} {self.debet}")

        def czy_debet(self):
            if self.saldo < 0:
                return True

        def oblicz_odsetki(self):
            return round(self.saldo * self.oprocentowanie / 100, 2)

    konta = [Konto("Wojciech", "Kowalski", 12345, 100, 300), Konto("Gabi", "Love", 112345, 33333, 333)]

    for konto in konta:
        Konto.wyswietl(konto)
    for konto in konta:
        Konto.zwroc_dane(konto)
    print(Konto.czy_mozliwa_wyplata(konta[0], 3000))
    Konto.zwieksz_saldo(konta[0], 250)
    Konto.wyplac(konta[0], 300)
    for konto in konta:
        print(konto.imie, konto.saldo - Konto.oblicz_odsetki(konto))

    for konto in konta:
        konto.oprocentowanie = 10

    for konto in konta:
        print(f"Konto: {konto.imie}")
        print(f"Debet wynosi: {konto.debet}")
        if Konto.czy_debet(konto):
            print("Na tym koncie jest debet")
        else:
            print("Na tym koncie nie ma debetu")


def quest2():
    class Produkt:
        def __init__(self, nazwa, cena_netto):
            self.nazwa = nazwa
            self.cena_netto = cena_netto
            self.vat = 23

        def zwroc_cene_brutto(self):
            return self.cena_netto - self.cena_netto * self.vat / 100

        def zwroc_cene_netto(self):
            return self.cena_netto

        def wyswietl(self):
            print(self.__dict__)

        def nalicz_rabat(self, procent):
            self.cena_netto -= self.cena_netto * procent / 100

        def czy_tanszy(self, kwota):
            if self.zwroc_cene_brutto() < kwota:
                return True
            else:
                return False

        def zmien_cene(self, cena):
            self.cena_netto = cena

        def zwroc_wszytkie_dane(self):
            return f"{self.nazwa} {self.cena_netto} {self.zwroc_cene_brutto()}"

    produkty = [Produkt("ziemniak", 20), Produkt("Cola", 5), Produkt("Kask", 35)]

    for produkt in produkty:
        print("Brutto: ", produkt.zwroc_cene_brutto())
        print(f"Netto: {produkt.zwroc_cene_netto()}")
        produkt.wyswietl()
        produkt.nalicz_rabat(20)
        print(produkt.czy_tanszy(15))
        produkt.zmien_cene(100)
        print(produkt.zwroc_wszytkie_dane())
        print("----------------------")


def quest3():
    class Prostokat:
        def __init__(self, a=1, b=1):
            self.a = a
            self.b = b

        def podaj_krotszy_bok(self):
            if self.a < self.b:
                return self.a
            else:
                return self.b

        def podaj_dluzszy_bok(self):
            if self.a > self.b:
                return self.a
            else:
                return self.b

        def zmien(self, a, b):
            self.a = a
            self.b = b

        def zwroc_pole(self):
            return self.a * self.b

        def zwroc_obwod(self):
            return self.a * 2 + self.b * 2

        def czy_kawdrat(self):
            if self.a == self.b:
                return True
            else:
                return False

        def wyswietl(self):
            print(self.a, self.b, self.zwroc_pole(), self.zwroc_obwod(), self.czy_kawdrat())

    prostokaty = [Prostokat(5, 3), (Prostokat(3, 6))]
    prostokaty[1].zmien(6, 6)
    for prostokat in prostokaty:
        prostokat.wyswietl()


def quest4():
    class Samochod:
        def __init__(self, marka, model, spalanie, predkosc_maksymalna, predkosc_aktualna, pojemnosc_zbiornika_paliwa,
                     stan_paliwa, numer_rejestracyjny, rocznik=2020, przebieg=0):
            self.marka = marka
            self.model = model
            self.spalanie = spalanie
            self.predkosc_maksymalna = predkosc_maksymalna
            self.predkosc_aktualna = 0
            self.pojemnosc_zbiornika_paliwa = pojemnosc_zbiornika_paliwa
            self.stan_paliwa = stan_paliwa
            self.numer_rejestracyjny = numer_rejestracyjny
            self.rocznik = rocznik
            self.przebieg = przebieg

        def wyswietl(self):
            print(self.__dict__)

        def zwroc_predkosc_aktualna(self):
            return self.predkosc_aktualna

        def ile_do_maksymalnej(self):
            return self.predkosc_maksymalna - self.predkosc_aktualna

        def wyswietl_stan_paliwa(self):
            print(f"Stan paliwa to {self.stan_paliwa}")

        def zwroc_wiek_pojazdu(self):
            return 2020 - self.rocznik

        def zmien_nr_pojazdu(self, nr):
            print(f"Nr {self.numer_rejestracyjny} zmieniono na {nr}")
            self.numer_rejestracyjny = nr

        def przyspiesz(self, o_wartosc):
            self.predkosc_aktualna += o_wartosc
            print(f"Aktualna prędkość to {self.predkosc_aktualna}")

        def zwolnij(self, o_wartosc):
            self.predkosc_aktualna -= o_wartosc
            print(f"Aktualna prędkość to {self.predkosc_aktualna}")

        def zatankuj(self, o_wartosc):
            self.stan_paliwa += o_wartosc
            print(f"Stan paliwa to {self.stan_paliwa}")

        def zatankuj_do_pelna(self):
            self.stan_paliwa = self.pojemnosc_zbiornika_paliwa

        def czy_pusty(self):
            if self.stan_paliwa == 0:
                return True
            else:
                return False

        def czy_pelny(self):
            if self.stan_paliwa == self.pojemnosc_zbiornika_paliwa:
                return True
            else:
                return False

        def jedz(self, o_wartosc):
            if self.stan_paliwa - o_wartosc * self.spalanie < 0:
                print(f"Zabrakło paliwa przejechano jedynie {self.stan_paliwa * self.spalanie}")
                self.przebieg += self.stan_paliwa * self.spalanie
                self.stan_paliwa = 0
            else:
                self.przebieg += o_wartosc
                self.stan_paliwa -= o_wartosc * self.spalanie

        def zatrzymaj_sie(self):
            self.predkosc_aktualna = 0

        def czy_zatankowac(self):
            if self.stan_paliwa < self.pojemnosc_zbiornika_paliwa * 0.2:
                return True
            else:
                return False

    samochod = Samochod("BMW", "3", 2, 200, 10, 100, 50, "WS1234", 2018, 2300)

    print(samochod.zwroc_predkosc_aktualna())
    print(samochod.ile_do_maksymalnej())
    print(samochod.czy_pelny())
    print(samochod.czy_pusty())
    print(samochod.czy_zatankowac())
    print(samochod.zwroc_wiek_pojazdu())
    samochod.zmien_nr_pojazdu("WS321")
    samochod.wyswietl_stan_paliwa()
    samochod.przyspiesz(30)
    samochod.zwolnij(20)
    samochod.zatrzymaj_sie()
    samochod.zatankuj(40)
    samochod.zatankuj_do_pelna()
    samochod.jedz(100)
    samochod.wyswietl()
