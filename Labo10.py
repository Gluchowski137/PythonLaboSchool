def quest1():
    class Pracownik:
        def __init__(self, imie, nazwisko, zawod, rok_zatrudnienia=2020, wynagrodzenie_podstawowe=2500):
            self.imie = imie
            self.nazwisko = nazwisko
            self.zawod = zawod
            self.wynagrodzenie_podstawowe = wynagrodzenie_podstawowe
            self.rok_zatrudnienia = rok_zatrudnienia

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


def quest2():
    class KontoBankowe:
        def __init__(self, imie_wlasciciela, nazwisko_wlasciciela, pesel_wlasciciela, stan_konta, rok_zalozenia=2020):
            self.imie_wlasciciela = imie_wlasciciela
            self.nazwisko_wlasciciela = nazwisko_wlasciciela
            self.pesel_wlasciciela = pesel_wlasciciela
            self.stan_konta = stan_konta
            self.rok_zalozenia = rok_zalozenia
            self.stan_konta = 0

        def zwieksz_stan_konta(self, kwota):
            self.stan_konta += kwota

        def oblicz_lata(self):
            return 2020 - self.rok_zalozenia

        def zwroc_stan_konta(self):
            return self.stan_konta

        def wyswietl(self):
            print(
                f"Wlasciciel:{self.imie_wlasciciela} {self.nazwisko_wlasciciela} {self.pesel_wlasciciela} rok_zalozeni"
                f"a: {self.rok_zalozenia} Lat u nas: {self.oblicz_lata()} Stan konta: {self.stan_konta}")

    class KontoOszczednosciowe(KontoBankowe):
        def __init__(self, imie_wlasciciela, nazwisko_wlasciciela, pesel_wlasciciela, stan_konta, rok_zalozenia=2020,
                     oprocentowanie=0, okres_rozliczeniowy=12):
            super().__init__(imie_wlasciciela, nazwisko_wlasciciela, pesel_wlasciciela, stan_konta, rok_zalozenia)
            self.oprocentowanie = oprocentowanie / 100
            self.okres_rozliczeniowy = okres_rozliczeniowy

        def ustaw_oprocentowanie(self, procent):
            self.oprocentowanie = procent / 100

        def oblicz_odsetki(self):
            stan_konta_help = self.stan_konta
            odsetki = 0
            for x in range(int(round(((self.oblicz_lata() * 12) / self.okres_rozliczeniowy), 0))):
                odsetki += stan_konta_help * self.oprocentowanie
                stan_konta_help += stan_konta_help * self.oprocentowanie

            return int(round(odsetki, 0))

        def nalicz_odsetki(self):
            self.stan_konta += self.oblicz_odsetki()

        def __str__(self):
            return f"Wlasciciel:{self.imie_wlasciciela} {self.nazwisko_wlasciciela} {self.pesel_wlasciciela} rok_zalozenia: {self.rok_zalozenia} Lat u nas: {self.oblicz_lata()} Stan konta: {self.stan_konta}"
