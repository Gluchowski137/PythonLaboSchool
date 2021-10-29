import random


def quest1():
    lista_filmow = ["matrix", "titanic", "faces", "naruto", "sao", "desperados"]
    lista_filmow.append("zorro")
    lista_filmow.append("apollo")
    lista_filmow.append("dzien_swira")
    lista_filmow.append("kobiety_mafii")
    print(lista_filmow[0:2])
    print(lista_filmow[-2:])
    lista_filmow[3] = "Psy"
    lista_filmow.insert(0, "pila")
    lista_filmow.insert(0, "kickboxer")
    lista_filmow.insert(0, "lot_nad_kukolczym_gniazdem")
    lista_filmow.pop(7)
    od_uzytkownika = input("Podaj tylul filmu: ")
    help = 0
    for x in range(3):
        if od_uzytkownika == lista_filmow[x]:
            help += 1

    if help == 0:
        print("filmu nie ma na 3 pierwszych pozycjach liscie")
    else:
        print("film jest na pierwszych 3 pozycjach na liscie")

    premiery = ["matrix_nowy", "pokemony", "parapety"]

    film_od_uzytownika = input("podaj tytul filmu: ")

    if film_od_uzytownika in lista_filmow:
        print("Film jest na liscie filmow")
    elif film_od_uzytownika in premiery:
        print("Film jest na liscie premier")
    else:
        print("brak podanego tytulu w bazie")

    kopia_listy_filmow = lista_filmow
    lista_filmow = lista_filmow + premiery
    print(lista_filmow[6:])
    lista_filmow.clear()

    def pobieranie_filmu():
        nowy_film = input("podaj film: ")
        if nowy_film != "":
            lista_filmow.append(nowy_film)
            pobieranie_filmu()
        else:
            pass

    pobieranie_filmu()
    print(lista_filmow)
    lista_filmow[-1] = "ostatni_film"
    nazwa_filmu = input("podaj nazwe filmu: ")
    if nazwa_filmu in lista_filmow:
        print(lista_filmow.index(nazwa_filmu))

    print(lista_filmow)
    lista_filmow.sort()
    print(lista_filmow)
    lista_filmow.reverse()
    print(lista_filmow)


def quest2():
    def show_subjects(subjects):
        for subject in subjects:
            print(subject)

    def remove_duplitcats(subjects):
        good_rok_2_mgr = []
        for subject in subjects:
            if subject not in good_rok_2_mgr:
                good_rok_2_mgr.append(subject)
        return good_rok_2_mgr

    semestr_zimowy = ["Computer architecture", "Computer networks and Internet", "Introduction to computer science",
                      "Introduction to differential and integral calculus", "Linear algebra", "Logic", "Spanish",
                      "Tennis"]
    print("semestr_zimowy")
    show_subjects(semestr_zimowy)
    semestr_letni = ["Algorithms of numerical analysis", "Analytic geometry", "Discrete mathematics",
                     "Fundamentals of algorithms and programming", "Operating systems",
                     "Computer graphics", "Entrepreneurship", "Websites design",
                     "Spanish", "Tennis"]
    print("semestr_letni")
    show_subjects(semestr_letni)
    subject_name = input("Pass subject name: ")
    if subject_name in semestr_zimowy:
        print("Przedmiot z semestru zimowego")
    if subject_name in semestr_letni:
        print("Przedmiot z semestru letniego")
    else:
        print("Nie ma takiego przedmiotu na aktualnym roku studiów")
    rok_2_mgr = semestr_zimowy + semestr_letni
    rok_2_mgr = remove_duplitcats(rok_2_mgr)
    rok_2_mgr.sort()
    print("rok_2_mgr")
    show_subjects(rok_2_mgr)


def quest3():
    ksiazki = []
    ksiazki.append("Futu.re")
    ksiazki.append("Homo deus")
    ksiazki.append("Listy do Astrofizyka")
    ksiazki.append("Czysty kod")
    ksiazki.append("Kwantechizm")
    ksiazki.append("Elon Musk")
    ksiazki.sort()
    print(ksiazki[0], ksiazki[-2:])
    print(len(ksiazki))


def quest4():
    lista_zakupow = ["chleb", "ser", "wedlina", "ketchup"]
    lista_zakupow[2] = "mleko"
    for x in range(3):
        lista_zakupow.insert(x, input("Podaj produkt: "))
    print(lista_zakupow[-2:])
    lista_zakupow.pop(1)
    lista_zakupow.pop(1)
    if "chleb" in lista_zakupow:
        print("Chleb jest na liscie zakupow")
    else:
        print("Chleb nie jest na liscie zakupow")
    lista_zakupow.remove(input("Produkt do usuniecia: "))
    print(lista_zakupow)


def quest5():
    def from_chess_to_eq():
        print("You found: ", skrzynia)
        ekwipunek.extend(skrzynia)
        skrzynia.clear()

    def change_ball_for_potion(eq):
        if "magiczna kula" in eq:
            eq.remove("magiczna kula")
            eq.append("napój uzdrawiający")
            print("Wymieniasz magiczną kulę na utracony napój")

    ekwipunek = ["napój uzdrawiający", "miecz", "zbroja", "tarcza"]
    print(len(ekwipunek), ekwipunek)
    skrzynia = ["złoto", "magiczna kula"]
    from_chess_to_eq()
    print(len(ekwipunek), ekwipunek)
    print("Używasz napój uzdrawiający")
    ekwipunek.remove("napój uzdrawiający")
    change_ball_for_potion(ekwipunek)
    skrzynia.append("prowiant")
    from_chess_to_eq()
    print(len(ekwipunek), ekwipunek)
    statystyki = [100, 50, 20]  # hp,ATACK,armor
    print(f"Twoje statystyiki HP|ATACK|ARMOR wynoszą: {statystyki}")
    print("Zakładasz zbroje i tarczę")
    ekwipunek.remove("zbroja")
    ekwipunek.remove("tarcza")
    statystyki[2] = 65
    print(len(ekwipunek), ekwipunek)
    print(f"HP|ATACK|ARMOR: {statystyki}")
    print(
        f"Spotykasz kupca! Kup jeden z jego przedmiotów za swoje złoto!\nPrzedmioty Kupca:\nMagiczny Grzyb\nPuszka\nStara waza")
    kupiony_przedmiot = input("Wybieram przedmiot o nazwie: ")
    if kupiony_przedmiot == "Magiczny Grzyb":
        ekwipunek.append("Magiczny Grzyb")
        ekwipunek.remove("złoto")
    elif kupiony_przedmiot == "Puszka":
        ekwipunek.append("Puszka")
        ekwipunek.remove("złoto")
    elif kupiony_przedmiot == "Stara waza":
        ekwipunek.append("Stara waza")
        ekwipunek.remove("złoto")

    else:
        print("Kupca nie ma takiego przedmiotu.Speszony uciekł !")
        kupiony_przedmiot = "złoto"
    print(len(ekwipunek), ekwipunek)
    print("Zakładasz miecz")
    ekwipunek.remove("miecz")
    statystyki[1] += 50
    print(f"HP|ATACK|ARMOR: {statystyki}")
    print("Bierzesz do reki", kupiony_przedmiot)

    if "Puszka" in ekwipunek:
        print("W puszce były złe moce! Umierasz.")
    if "Magiczny Grzyb" in ekwipunek:
        print("Zjadasz go! Twoje HP wzrasta!")
        statystyki[0] += 25
        print(f"HP|ATACK|ARMOR: {statystyki}")
    if "Stara waza" in ekwipunek:
        print("Ta waza to najprawdziwszy Antyk!! Możesz uważać się za bogacza!")
    if "złoto" in ekwipunek:
        print("Wpada na Ciebie ładna pani po podniesieniu się zauważasz,że straciłeś złoto!")
        ekwipunek.remove("złoto")
        print(len(ekwipunek), ekwipunek)


def quest6():
    def srednia(oceny):
        srednia_ocen = 0
        for i in oceny:
            srednia_ocen += i
        return srednia_ocen / len(oceny)

    oceny = [4, 4, 3, 5, 1, 4, 5, 3, 2]
    oceny_semestr_2 = [3, 3, 5, 5, 1, 2, 4, 2]
    oceny.extend(oceny_semestr_2)
    print(oceny)
    print(srednia(oceny))
    ocena = int(input("Podaj ocene: "))
    if oceny.count(ocena) != 0:
        print(oceny.index(ocena))
    else:
        print("Nie ma tej oceny")


def quest7():
    def fill_money(przychody):
        for x in range(12):
            przychody.append(random.randint(3000, 5000))

    def how_much_more(przychody, kwota):
        this_much = 0
        for x in przychody:
            if x > kwota:
                this_much += 1
        return this_much

    przychodyRok2018 = []
    przychodyRok2019 = []
    przychodyRok2020 = []
    fill_money(przychodyRok2018)
    fill_money(przychodyRok2019)
    fill_money(przychodyRok2020)
    print("PrzychodyRok2018: ", przychodyRok2018)
    print("PrzychodyRok2019: ", przychodyRok2019)
    print("PrzychodyRok2020: ", przychodyRok2020)
    print("suma przychodów:")
    print("2018: ", sum(przychodyRok2018))
    print("2019: ", sum(przychodyRok2019))
    print("2020: ", sum(przychodyRok2020))
    print("2018-2020: ", sum(przychodyRok2018) + sum(przychodyRok2019) + sum(przychodyRok2020))
    print("srednia przychodów:")
    print("2018: ", int(sum(przychodyRok2018) / 12))
    print("2019: ", int(sum(przychodyRok2019) / 12))
    print("2020: ", int(sum(przychodyRok2020) / 12))
    maximum = max(sum(przychodyRok2018), sum(przychodyRok2019), sum(przychodyRok2020))
    print("suma przychodów była największa:")
    if maximum == sum(przychodyRok2018):
        print("2018")
    elif maximum == sum(przychodyRok2019):
        print("2019")
    elif maximum == sum(przychodyRok2020):
        print("2020")

    maximum_srednia = max(int(sum(przychodyRok2018) / 12), int(sum(przychodyRok2019) / 12),
                          int(sum(przychodyRok2020) / 12))
    print("średnia przychodów była największa:")
    if maximum_srednia == int(sum(przychodyRok2018) / 12):
        print("2018")
    elif maximum_srednia == int(sum(przychodyRok2019) / 12):
        print("2019")
    elif maximum_srednia == int(sum(przychodyRok2020) / 12):
        print("2020")

    kwota = int(input("podaj kwote: "))
    print("2018:", how_much_more(przychodyRok2018, kwota))
    print("2019:", how_much_more(przychodyRok2019, kwota))
    print("2020:", how_much_more(przychodyRok2020, kwota))

    copied_przychody_2018 = przychodyRok2018.copy()
    copied_przychody_2019 = przychodyRok2019.copy()
    copied_przychody_2020 = przychodyRok2020.copy()

    copied_przychody_2018.sort()
    copied_przychody_2019.sort()
    copied_przychody_2020.sort()
    print("najmniejszy | najwiekszy dochod w roku:")
    print("2018:", copied_przychody_2018[0], copied_przychody_2018[-1])
    print("2019:", copied_przychody_2019[0], copied_przychody_2019[-1])
    print("2020:", copied_przychody_2020[0], copied_przychody_2020[-1])

    print("najmniejszy | najwiekszy dochod byl w miesiacu w roku:")
    print("2018:", przychodyRok2018.index(copied_przychody_2018[0]), przychodyRok2018.index(copied_przychody_2018[-1]))
    print("2019:", przychodyRok2019.index(copied_przychody_2019[0]), przychodyRok2019.index(copied_przychody_2019[-1]))
    print("2020:", przychodyRok2020.index(copied_przychody_2020[0]), przychodyRok2020.index(copied_przychody_2020[-1]))
    print("największy i najmniejszy przychod uzyskany od początku 2018 roku")
    print(min(copied_przychody_2018 + copied_przychody_2019 + copied_przychody_2020),
          max(copied_przychody_2018 + copied_przychody_2019 + copied_przychody_2020))

    print("2018: ", copied_przychody_2018)
    print("2019: ", copied_przychody_2019)
    print("2020: ", copied_przychody_2020)


def quest8():
    punkty = [10, 12, 1, 12, 2, 4, 6, 4, 9, 10, 11, 3, 7, 5, 19]

    def add_players(how_many):
        for x in range(how_many):
            punkty.append(random.randint(0, 20))

    add_players(5)
    print("Najwieksza i najmniejsa ilosc punktow: ", max(punkty), min(punkty))
    punkty.sort()
    print(punkty)
    podane_punkty = int(input("Podaj punkty: "))
    if podane_punkty in punkty:
        print("Ktoś zdobył")
    else:
        print("nikt tyle nie zdobyl")

    srednia_punktow = sum(punkty) / len(punkty)
    ile_ponizej = 0
    print("ponizej:")
    for punkt in punkty:
        if punkt < srednia_punktow:
            ile_ponizej += 1
            print(punkt)

    ile_powyzej = 0
    print("powyzej:")
    for punkt in punkty:
        if punkt > srednia_punktow:
            ile_powyzej += 1
            print(punkt)

    punkty.clear()
    add_players(10)
    for x in range(5):
        punkty.append(int(input(f"Podaj {x + 1} punkt: ")))

    punkty.sort()
    print(punkty)


def quest9():
    przelewy_wychodzadze = []
    for x in range(random.randint(4, 6)):
        przelewy_wychodzadze.append(random.randint(3000, 5000))
    print("Ilość wykonanych przelewow: ", len(przelewy_wychodzadze))

    for x in range(1):
        przelewy_wychodzadze.append(int(input(f"Podaj sume {x + 1} przelewu: ")))

    print("Ilość wykonanych przelewow: ", len(przelewy_wychodzadze))
    print(
        f"Suma przelewów: {sum(przelewy_wychodzadze)}\nSrednia przelewow: {round(sum(przelewy_wychodzadze) / len(przelewy_wychodzadze))}")

    powyzej_sredniej = []
    ponizej_sredniej = []
    for przelew in przelewy_wychodzadze:
        if przelew > round(sum(przelewy_wychodzadze) / len(przelewy_wychodzadze)):
            powyzej_sredniej.append(przelew)
        else:
            ponizej_sredniej.append(przelew)
    ponizej_sredniej.sort()
    powyzej_sredniej.sort()
    print(f"Powyzej sredniej: {powyzej_sredniej}\nPoniżej sriedniej: {ponizej_sredniej}")

    podany_przelew = int(input("Podaj wielkosc przelewu do sprawdzenia: "))

    if podany_przelew in przelewy_wychodzadze:
        print("Jest przelew o podanej wartosci")
    else:
        print("Nie ma przelewu o podnej wartosci")

    podany_przelew = int(input("Podaj wielkosc przelewu do sprawdzenia ile jest wiecej: "))
    ile_wiecej = 0
    for przele in przelewy_wychodzadze:
        if przele > podany_przelew:
            ile_wiecej += 1

    print(ile_wiecej)
    podany_przelew = int(input("Podaj warttosc do sprzwadzenia jej indeksu: "))

    if podany_przelew in przelewy_wychodzadze:
        print(przelewy_wychodzadze.index(podany_przelew))
    else:
        print("W bazie nie ma przlewu o podanej wartosci!")


def quest10():
    imiona_zenskie = ["Gabi", "Maria", "Gosia", "Ewa", "Kasia", "Magda"]
    imiona_meskie = ["Max", "Kuba", "Krzysztof", "Robert", "Adam", "Wojtek"]
    imiona_zenskie.append("Dorota")
    imiona_zenskie.append("Ania")
    imiona_zenskie.append("Teresa")
    imiona_meskie.insert(1, "Michal")
    imiona_meskie.insert(2, "Lukasz")
    imiona_zenskie.sort()
    imiona_meskie.sort()
    print(f"{imiona_zenskie}\n{imiona_meskie}")

    podane_imie = input("Podaj imie: ")
    if podane_imie in imiona_meskie:
        imiona_meskie.remove(podane_imie)
        print(f"Usunięto imię {podane_imie}")
    else:
        if podane_imie in imiona_zenskie:
            imiona_zenskie.remove(podane_imie)
            print(f"Usunięto imię {podane_imie}")
        else:
            print("Nie ma tego imienia w bazie!")
    imiona = imiona_meskie + imiona_zenskie
    imiona.sort()
    imiona.pop(2)
    print(imiona)
