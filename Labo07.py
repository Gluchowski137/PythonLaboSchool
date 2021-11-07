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
