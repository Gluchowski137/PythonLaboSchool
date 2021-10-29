def quest1():
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


def quest2():
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


def quest3():
    studenci = ("Gluchowski", "Arseniuk", "Kowalski", "Nowak", "Krab", "Nowak")
    print(studenci)
    print(f"Liczba studentów na roku wynosi {len(studenci)} osób")

    podane_nazwisko = input("Podaj nazwisko do sprawdzenia:")
    print(f"Studentów o nazwisku {podane_nazwisko} na roku jest: {studenci.count(podane_nazwisko)}")
    del studenci


def quest4():
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

