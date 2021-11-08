def quest1():
    class Konto:
        def __init__(self, imie, nazwisko, nr_konta, saldo, debet=0):
            self.imie = imie
            self.nazwisko = nazwisko
            self.nr_konta = nr_konta
            self.saldo = 0
            self.saldo += saldo
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
    Konto.zwieksz_saldo(konta[1], 250)
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
