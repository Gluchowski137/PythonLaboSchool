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
