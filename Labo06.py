# Tuple

def quest_t_1():
    oceny = (3, 3, 4, 4.5, 5, 2, 2, 2)
    srednia = 0
    for ocena in oceny:
        srednia += ocena

    print(srednia / len(oceny))
    print(
        f"2: {oceny.count(2)}\n3: {oceny.count(3)}\n3.5: {oceny.count(3.5)}\n4: {oceny.count(4)}\n4.5: {oceny.count(4.5)}\n5: {oceny.count(5)}")

    oceny_dozwolone = (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)
    ocena = float(input("Podaj ocenę: "))
    if ocena in oceny_dozwolone:
        print(f"{ocena} wystąpiła {oceny.count(ocena)} razy")
    else:
        print("Nie mozna miec takiej oceny!")


def quest_t_2():
    przedmioty_semestr_zimowy = (
        "Computer architecture", "Computer networks and Internet", "Introduction to computer science",
        "Introduction to differential and integral calculus", "Linear algebra", "Logic", "Spanish",
        "Tennis")
    przedmioty_semestr_letni = ("Algorithms of numerical analysis", "Analytic geometry", "Discrete mathematics",
                                "Fundamentals of algorithms and programming", "Operating systems",
                                "Computer graphics", "Entrepreneurship", "Websites design",
                                "Spanish", "Tennis")

    print(f"przedmioty_semestr_letni: {len(przedmioty_semestr_letni)}")
    print(f"przedmioty_semestr_zimowy: {len(przedmioty_semestr_zimowy)}")
    if len(przedmioty_semestr_zimowy) < len(przedmioty_semestr_letni):
        print("Więcej przedmiotów w semestrze letnim")
    elif len(przedmioty_semestr_zimowy) > len(przedmioty_semestr_letni):
        print("Więcej przedmiotów w semestrze zimowym")
    else:
        print("Taka sama liczba przedmiotów w obu semestrach")

    print(przedmioty_semestr_zimowy, przedmioty_semestr_letni)
    przedmiot_do_sprawdzenia = input("Podaj przedmiot do sprawdzenia: ")
    if przedmiot_do_sprawdzenia in przedmioty_semestr_letni:
        print(
            f"Przedmiot znajduje się w semestrze letnim oraz ma indeks o nr: {przedmioty_semestr_letni.index(przedmiot_do_sprawdzenia)}")
    if przedmiot_do_sprawdzenia in przedmioty_semestr_zimowy:
        print(
            f"Przedmiot znajduje się w semestrze zimowym oraz ma indeks o nr: {przedmioty_semestr_zimowy.index(przedmiot_do_sprawdzenia)}")
    else:
        print("Przedmiotu nie ma na aktulanym roku studiow!")

    przedmioty_sem_zim_let = przedmioty_semestr_letni + przedmioty_semestr_zimowy
    przedmiot_do_sprawdzenia = input("Podaj przedmiot do sprawdzenia: ")
    if przedmioty_sem_zim_let.count(przedmiot_do_sprawdzenia) >= 2:
        print(f"Przedmiot {przedmiot_do_sprawdzenia} występuje przynajmniej 2 razy!")
    else:
        print(f"Przedmiot {przedmiot_do_sprawdzenia} nie występuje przynajmniej 2 razy!")


def quest_t_3():
    studenci = ("Gluchowski", "Arseniuk", "Kowalski", "Nowak", "Krab", "Nowak")
    print(studenci)
    print(f"Liczba studentów na roku wynosi {len(studenci)} osób")

    podane_nazwisko = input("Podaj nazwisko do sprawdzenia:")
    print(f"Studentów o nazwisku {podane_nazwisko} na roku jest: {studenci.count(podane_nazwisko)}")
    del studenci


# Set

def quest_s_1():
    biblioteka_gier = {"miencraft", "cs", "lol", "nostale", "metin2"}
    gry_w_koszyku = {"Simsy", "Terraria", "The forest", "Wiedzmin"}
    gry_w_koszyku.update(["New world", "black desert", "Sacred", "Diablo"])
    gry_w_koszyku.pop()
    gry_w_koszyku.pop()
    gry_w_koszyku.pop()
    print(gry_w_koszyku, biblioteka_gier)
    biblioteka_gier.update(gry_w_koszyku)
    gry_w_koszyku.clear()
    gry_w_koszyku.add("Far Cry")
    gry_w_koszyku.add("rainbow six siege")
    gry_w_koszyku.add("Pay day")
    if "Heroes 3" in biblioteka_gier:
        print("Heroes 3 jest w bibliotece gier")
    else:
        print("Heroes 3 nie jest w bibliotece gier")

    print(f"Liczba gier w bibliotece wynosi: {len(biblioteka_gier)}")
    podana_gra = input("Podaj gre: ")
    if podana_gra in biblioteka_gier:
        print(f"{podana_gra} znajduje się w bibliotece")
        if podana_gra in gry_w_koszyku:
            gry_w_koszyku.remove(podana_gra)
    else:
        print(f"{podana_gra} nie najduje się w bibliotece")

    gry_w_koszyku.difference_update(biblioteka_gier)

    gry_w_promocji = {"Far Cry", "cs", "lol", "Naruto", "Pay day"}

    for gra in gry_w_promocji:
        if gra not in biblioteka_gier:
            print(gra)

    for game in gry_w_koszyku.difference(gry_w_promocji):
        gry_w_koszyku.remove(game)


def quest_s_2():
    owoce = {"jabłko", "pomarańcza", "banan"}
    warzywa = {"ogórek", "sałata", "marchewka"}
    print(f"Owoce:{owoce}\nWarzywa:{warzywa}")
    warzywniak = owoce.union(warzywa)
    lista_zakupow = {"banan", "rzodkiew", "granat"}
    for produkt in lista_zakupow:
        if produkt not in warzywniak:
            print(f"Brak {produkt} w warzywniaku")

    lista_zakupow.remove("rzodkiew")
    lista_zakupow.remove("granat")
    lista_zakupow.add("ogórek")
    lista_zakupow.add("banan")
    for produkt in warzywniak:
        if produkt in lista_zakupow:
            lista_zakupow.remove(produkt)
    lista_zakupow.clear()
    lista_zakupow.update({"Arbuz", "kokos", "wiśnie"})
    print(f"Produkty na liscie zakupów:{lista_zakupow}")
    nowe_owoce = {"cytryna", "limonka"}
    nowe_warzywa = {"batat", "ziemniak"}
    warzywniak.update(nowe_warzywa, nowe_owoce)
    for produkt in lista_zakupow:
        if produkt not in warzywniak:
            print(f"Brak {produkt} w warzywniaku")
    for produkt in warzywniak:
        if produkt in lista_zakupow:
            lista_zakupow.remove(produkt)
    zapotrzebowanie = lista_zakupow
    warzywniak.update(zapotrzebowanie)
    warzywniak.pop()

    lista_zakupow.update({"Arbuz", "ogórek", "czereśnie"})

    lista_zakupow.difference_update(warzywniak)

    wybrany_owoc_warzywo = input("Podaj nazwe owocu lub warzywa,aby sprawdzić czy jest w warzywniaku:")
    if wybrany_owoc_warzywo in warzywniak:
        print(f"{wybrany_owoc_warzywo} jest w warzywniaku")
    else:
        print(f"{wybrany_owoc_warzywo} nie jest w warzywniaku")


# Vocabulary

def quest_v_1():
    def find_key_for_value(vocabulary, given_value):
        for key, value in vocabulary.items():
            if value == given_value:
                return key

    skojarzenia = {"wina": "kłopoty", "świnia_1": "zwierze", "brak reakcji": "brak słów",
                   "świnia_2": "Osoba niskiej kultury", "Placz": "smark"}

    rymy = {"wina": "świnia", "pochmurnie": "w urnie", "męka": "wstęga", "oddech": "ech"}

    skojarzenia.update({"kolor": "uczcucie", "ex_1": "wróg", "ex_2": "była"})
    rymy.update({"przesmutek": "upadek", "łamać": "wstawać", "krzyk": "ryk"})

    for skojarzenie_1, skojarzenie_2 in skojarzenia.items():
        print(f"Słowo | {skojarzenie_1} | ma powiązanie ze słowem | {skojarzenie_2} |")

    for rym_1, rym_2 in rymy.items():
        print(f"Słowo | {rym_1} | rymuje się ze słowem | {rym_2} |")

    skojarzenie_uzytkownika = input("Podaj słowo by podać jego skojarzenie, które znajduje się bazie: ")
    if skojarzenie_uzytkownika in skojarzenia:
        print(f"Skojarzeniem do słowa {skojarzenie_uzytkownika} jest {skojarzenia.get(skojarzenie_uzytkownika)}")
    elif skojarzenie_uzytkownika in skojarzenia.values():
        print(
            f"Skojarzeniem do słowa {skojarzenie_uzytkownika} jest {find_key_for_value(skojarzenia, skojarzenie_uzytkownika)} ")
    else:
        print(f"Nie ma skojarzenia do słowa {skojarzenie_uzytkownika} w bazie")

    rym_uzytkownika = input("Podaj słowo by podać rym, który znajduje się w bazie: ")
    if rym_uzytkownika in rymy:
        print(f"Rymem do słowa {rym_uzytkownika} jest {rymy.get(rym_uzytkownika)}")
    elif rym_uzytkownika in rymy.values():
        print(f"Rymem do słowa {rym_uzytkownika} jest {find_key_for_value(rymy, rym_uzytkownika)}")
    else:
        print(f"Nie ma rymu do słowa {rym_uzytkownika} w bazie")


