def quest1():
    def kalkulator(x, y=1):
        print(f"{x} + {y} = {x + y}")
        print(f"{x} - {y} = {x - y}")
        print(f"{x} * {y} = {x * y}")
        if x == 0 or y == 0:
            print(print(f"{x} / {y} = 0"))
        else:
            print(f"{x} / {y} = {x / y}")

    kalkulator(2, 5)


def quest2():
    def promocja(*paragony):
        for paragon in paragony:
            print(f"Za kwote {paragon} otrzymujesz {int(paragon / 40)} naklejek")

    promocja(45, 82, 76, 120)


def quest3():
    lista = []

    def lista_przedmiotow(lista):
        przedmiot = input("Podaj przdmiot:")
        if przedmiot != "":
            lista.append(przedmiot)
            lista_przedmiotow(lista)
        else:
            print(lista)

    print("Tworzenie listy przechowującej nazwy przedmiotów")
    lista_przedmiotow(lista)


def quest4():
    def mniej_niz(waga, waga_paczki):
        lzejszepaczki = [paczka for paczka in waga_paczki if paczka < waga]
        print(lzejszepaczki)

    mniej_niz(30, [30, 20, 24, 14, 32, 54, 32, 45, 1, 11])


def quest5():
    def lodowy_pocisk(moc, poziom):
        if poziom == 0:
            return f"Lodowy pocisk zada {20 * moc}"
        elif poziom == 1:
            return f"Lodowy pocisk zada {20 * moc + 10}"
        elif poziom == 2:
            return f"Lodowy pocisk zada {20 * moc + 20}"
        elif poziom == 3:
            return f"Lodowy pocisk zada {20 * moc + 30}"
        else:
            return -1

    print(lodowy_pocisk(120, 5))


def quest6():
    def predkosc_ruchu(szybkosc, teren):
        if szybkosc == 3:
            return f"Prędkosc ruchu wynosi {1500 + teren * - 400}"
        elif szybkosc == 4:
            return f"Prędkosc ruchu wynosi {1560 + teren * - 400}"
        elif szybkosc == 5:
            return f"Prędkosc ruchu wynosi {1630 + teren * - 400}"
        elif szybkosc == 6:
            return f"Prędkosc ruchu wynosi {1700 + teren * - 400}"
        elif szybkosc == 7:
            return f"Prędkosc ruchu wynosi {1760 + teren * - 400}"
        elif szybkosc == 8:
            return f"Prędkosc ruchu wynosi {1830 + teren * - 400}"
        elif szybkosc == 9:
            return f"Prędkosc ruchu wynosi {1900 + teren * - 400}"
        elif szybkosc == 10:
            return f"Prędkosc ruchu wynosi {1960 + teren * - 400}"
        elif szybkosc >= 11:
            return f"Prędkosc ruchu wynosi {2000 + teren * - 400}"
        else:
            return f"Prędkosc ruchu wynosi 0"

    print(predkosc_ruchu(5, 1))


def quest7():
    def wymiana_naklejek(naklejki):
        if naklejki >= 60:
            print("Możesz wymienić naklejki na dowolną maskotkę")
        elif 40 <= naklejki < 60:
            print("Możesz wymienić naklejki na mini maskotkę")
            print(f"Musisz uzbierać jeszcze {60 - naklejki} naklejek do dużej maskotki")
        elif 0 <= naklejki < 40:
            print(f"Musisz uzbierać jeszcze {40 - naklejki} naklejek do mini maskotki")
            print(f"Musisz uzbierać jeszcze {60 - naklejki} naklejek do dużej maskotki")
        else:
            print("Liczba naklejek nie może być ujemna")

    wymiana_naklejek(50)


def quest8():
    def polis(mieszkancy):
        if mieszkancy == 5040:
            return "Idealnie!"
        elif mieszkancy < 5040:
            return "Za mało mieszkańców"
        else:
            return "Za dużo mieszkańców"

    print(polis(5041))


def quest9():
    def slowo(*slowa):
        najdluzsze = ["", 0]
        najkrotsze = ["", 999999]
        for slowo in slowa:
            if len(slowo) > najdluzsze[1]:
                najdluzsze = [slowo, len(slowo)]
            if len(slowo) < najkrotsze[1]:
                najkrotsze = [slowo, len(slowo)]
        return [najkrotsze[0], najdluzsze[0]]

    print(slowo("elo", "ola", "hahahahahah", "Kamil"))


def quest10():
    def wymien_walute(PLN=1):
        return [f"EUR: {PLN * 4.6}", f"GBP:{PLN * 5.3}", f"USD: {PLN * 3.9}", f"CHF: {PLN * 4.3}", f"AUD: {PLN * 2.9}",
                f"JPY: {PLN * 3.5}"]

    print(wymien_walute(30))


def quest11():
    def zwroc_pierwsza_ujemna(liczby):
        for liczba in liczby:
            if liczba < 0:
                return liczba
        return 0

    print(zwroc_pierwsza_ujemna([3, 0, 4, 3]))


def quest12():
    global poprawne_haslo
    poprawne_haslo = "admin"

    def sprawdz_hasslo(haslo):
        if haslo == poprawne_haslo:
            return "Zalgowano"
        else:
            return "Błędne hasło"

    print(sprawdz_hasslo("admin"))


def quest13():
    def suma_liczb(liczby):
        suma = 0
        for liczba in liczby:
            suma += liczba
        return suma

    print(suma_liczb([2, 3, 1]))


def quest14():
    def suma_liczb(liczby):
        suma = 0
        for liczba in liczby:
            suma += liczba
        return suma, len(liczby)

    def srednia(suma, ilosc_liczb):
        return suma / ilosc_liczb

    print(srednia(suma_liczb([2, 3, 1])[0], suma_liczb([2, 3, 1])[1]))


def quest15():
    def suma_liczb(*liczby):
        suma = 0
        for liczba in liczby:
            suma += liczba
        return suma

    print(suma_liczb(2, 3, 1))


def quest16():
    def stypendium(lista, liczba):
        return [powyzej for powyzej in lista if powyzej >= liczba]

    print(f"{len(stypendium([3.5, 4.2, 4.1, 5.3, 5, 1, 3], 4))} studentów kwalifikuje się do stypendium naukowego")


def quest17():
    def czy_jest(zbior1, zbior2):
        for x in zbior1:
            if x in zbior2:
                print(f"{x} jest w 2 zbiorze")

    czy_jest(("jeden", "jabłko", "kisiel", "15"), ("jabłko", "kisiel", "ziemniak"))


def quest18():
    def przywitanie(godnosci):
        for godnosc in godnosci:
            print(f"Hej {godnosc}")

    przywitanie(["Maciek", "Sławek", "Nowak", "Kowalski"])


def quest19():
    def kwoty_faktury(lista, liczba=100):
        return [kwota for kwota in lista if kwota > liczba]

    faktura = [101, 200, 300, 87, 13, 41, 300, 14, 124]

    print(kwoty_faktury(faktura))


def quest20():
    def dodatnie(liczby):
        for liczba in liczby:
            if liczba < 0:
                return False
        return True

    lista_liczb = [1, 2, 3, 4, 5, 4, 2]

    print(dodatnie(lista_liczb))


def quest21():
    def do_10_znakow(*slowa):
        return [slowo for slowo in slowa if len(slowo) <= 10]

    print(do_10_znakow("siema", "hahahahahaha", "trzy", "1234567891011"))


def quest22():
    def bilet_pkp(kilometry=0):
        if kilometry <= 10:
            return f"Bilet kosztuje 20 zł"
        if 11 <= kilometry <= 30:
            return f"Bilet kosztuje {10 + 0.10 * kilometry} zł"
        if kilometry > 30:
            return f"Bilet kosztuje {1 + 0.8 * kilometry} zł"

    print(bilet_pkp(25))


def quest23():
    def zwroc_nieparzyste(liczby):
        return [liczba for liczba in liczby if liczba < 0]

    print(zwroc_nieparzyste([-1, 4, 3, -2, 3, 1, -23, 41]))
