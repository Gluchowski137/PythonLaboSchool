import random
from bs4 import BeautifulSoup
import requests


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


def quest_s_3():
    a = set()
    b = set()
    c = set()
    for value in range(random.randint(7, 10)):
        a.add(random.randint(1, 100))
        b.add(random.randint(1, 100))
        c.add(random.randint(1, 100))

    print(a.difference(b))
    print(b.difference(c))
    print(a.difference(c))
    abc = a.union(b, c)

    for value in range(3):
        a.add(random.randint(1, 100))
        b.add(random.randint(1, 100))
        c.add(random.randint(1, 100))

    a.pop()
    b.pop()
    c.pop()
    abc.pop()

    podana_liczba = int(input("Podaj liczbe by dodać ją do zboru A:"))
    if podana_liczba in a:
        print(f"Liczba {podana_liczba} znajduje się już w zbiorze A")
    else:
        a.add(podana_liczba)
        print(f"Dodano liczbę {podana_liczba} do zbioru A")

    podana_liczba = int(input("Podaj liczbe by odjąć ją do zboru A:"))
    if not podana_liczba in a:
        print(f"Liczba {podana_liczba} nie znajduje się już w zbiorze B")
    else:
        print(f"Usunięto liczbę {podana_liczba} ze zbioru B")
        b.remove(podana_liczba)

    print(a.difference(b))
    print(b.difference(c))
    print(a.difference(c))

    abc = a.union(b, c)
    print(
        f"Zbiór A posiada {len(a)} liczb:{a}\nZbiór B posiada {len(b)} liczb:{b}\nZbiór C posiada {len(c)} liczb:{c}\nZbiór ABC posiada {len(abc)} liczb:{abc}")


def quest_s_4():
    cyfry = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    liczby_pierwsze = {2, 3, 5, 7, 11, 13, 17, 19, 23}

    for cyfra in cyfry:
        if cyfra in liczby_pierwsze:
            print(cyfra)

    print(cyfry.difference(liczby_pierwsze))
    for liczba in liczby_pierwsze:
        if liczba >= 10:
            print(liczba)

    podana_cyfra = int(input("Sprawdz czy liczba jest cyfrą:"))

    if podana_cyfra in cyfry:
        print(f"{podana_cyfra} jest cyfra")
    else:
        print(f"{podana_cyfra} nie jest cyfrą")

    podana_cyfra = int(input("Sprawdz czy liczba jest w zbiorze liczb pierwszych:"))

    if podana_cyfra in liczby_pierwsze:
        print(f"{podana_cyfra} jest w zbiorze liczb pierwszych")
    else:
        print(f"{podana_cyfra} nie jest w zbiorze liczb pierwszych")


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


def quest_v_2():
    def find_key_for_value(vocabulary):
        pobrana_cyfra = int(input("Podaj cyfre by poznać jej słowny zapis: "))
        if pobrana_cyfra in vocabulary:
            print(f"Słowny zapis cyfry {pobrana_cyfra} to {vocabulary.get(pobrana_cyfra)}")
        else:
            print(f"{pobrana_cyfra} nie ma w słowniku podaj inną liczbe 0-9")
            find_key_for_value(vocabulary)

    cyfry_slownie = {1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
                     8: "osiem",
                     9: "dziewięć", 0: "zero"}

    for key, value in cyfry_slownie.items():
        print(f"{key} słownie zapisujemy {value}")

    find_key_for_value(cyfry_slownie)


def quest_v_3():
    kontakty = {"joanna": 539359369, "basia": 533596564, "iza": 549587142, "kasia": 987658633, "mateusz": 688587412}
    kontakty.update({"kamil": 312314121, "wojtek": 857960992, "bartek": 123456789})
    kontakty.pop("iza")
    kontakty["joanna"] = 3216549876
    kontakty["kasia"] = 5216112874
    nowe_kontakty = {"maciek": 987123845, "robert": 192837475}
    kontakty.update(nowe_kontakty)
    print(f"Baza zawiera numery {len(kontakty)} osób")
    print(f"Imiona osób w bazie: {kontakty.keys()}")
    for imie, numer in kontakty.items():
        print(f"Numer osoby o imieniu {imie} to: {numer}")
    print(f"Numery w bazie: {kontakty.values()}")

    imie_od_uzytkownika = input("Podaj imie osoby by sprawdzić czy jej numer telefonu jest w bazie:")
    if imie_od_uzytkownika in kontakty.keys():
        print(f"Numer telefonu {imie_od_uzytkownika} to {kontakty[imie_od_uzytkownika]}")
    else:
        print(f"Nie ma numeru telefonu {imie_od_uzytkownika} w bazie!")

    numer_od_uzytkownika = input("Podaj numer telefonu by sprawdzić czy jest w bazie")

    if numer_od_uzytkownika in kontakty.values():
        print(f"Numer {numer_od_uzytkownika} jest w bazie")
    else:
        print(f"Numeru {numer_od_uzytkownika} nie ma w bazie")

    kontakty_copy = kontakty.copy()


def quest_v_4():
    miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień',
                'październik', 'listopad', 'grudzień']

    def make_money():
        for miesiac in miesiace:
            przychody.update({miesiac: random.randint(2000, 3500)})

    def find_key_for_value(vocabulary, given_value):
        keys = []
        for key, value in vocabulary.items():
            if value == given_value:
                keys.append(key)
        return keys

    przychody = {}
    make_money()
    print(przychody.keys())
    for miesiac, dochod in przychody.items():
        print(f"W {miesiac} dochód wynosił {dochod}")

    miesiac_od_uzytkownika = input("Podaj nazwe miesiąca by poznać dochod: ")

    if miesiac_od_uzytkownika in przychody.keys():
        print(f"Dochod w miesiącu {miesiac_od_uzytkownika} wyniósł {przychody[miesiac_od_uzytkownika]}")
    else:
        print("Nie ma takiego miesiąca")

    if not len(find_key_for_value(przychody, 2500)) == 0:
        for times in range(len(find_key_for_value(przychody, 2500))):
            print(f"Dochod 2500 zostal uzyskany w {find_key_for_value(przychody, 2500)[times]}")
    else:
        print("W znadym miesiącu nie uzyskanu dochodu o wysokosci 2500")

    suma_dochodow = 0
    for dochod in przychody.values():
        suma_dochodow += dochod
    przychody.clear()
    make_money()
    suma_dochodow_2 = 0
    for dochod in przychody.values():
        suma_dochodow_2 += dochod

    sredni_dochod = suma_dochodow_2 / len(przychody)

    for miesiac, dochod in przychody.items():
        if dochod > sredni_dochod:
            print(f"Dochod w {miesiac} był wiekszy niż srednia")


# w czasie rzeczywistym
def quest_v_5():
    def find_key_for_value(vocabulary, given_value):
        for key, value in vocabulary.items():
            if value == given_value:
                return key

    money_name = ["złoty"]
    money_value = [1.0000]
    page_url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tab = soup.find("table", {"class": "nbptable"})
    for name in tab.find_all("td", {"class": "left"}):
        money_name.append(name.get_text())
    for value in tab.find_all("td", {"class": "right"}):
        if value.get_text()[-1].isdigit():
            value = str(value.get_text()[:value.get_text().find(",")]) + "." + str(
                value.get_text()[value.get_text().find(",") + 1:])
            money_value.append(float(value))
    kursy_walut = {}
    for nr in range(len(money_name)):
        kursy_walut.update({money_name[nr]: money_value[nr]})

    for nazwa, kurs in kursy_walut.items():
        print(f"Kurs {nazwa} w stosunku do złotego wynosi: {kurs}")

    kwota_od_uzytkownika = int(input("Podaj kwote do przeliczenia:"))
    for nazwa, kurs in kursy_walut.items():
        print(
            f"Kurs {nazwa} w stosunku do kwoty o wyskosci {kwota_od_uzytkownika} wynosi: {kurs * kwota_od_uzytkownika}")

    print(f"Baza posiada informacje o {len(kursy_walut)} walut")
    kwota_od_uzytkownika = int(input("Podaj kwote do przeliczenia:"))
    waluta_od_uzytkownika = input("Podan na jaką walute przeliczyc kwote:")
    if waluta_od_uzytkownika in kursy_walut.keys():
        print(
            f"Kwota {kwota_od_uzytkownika} w {waluta_od_uzytkownika} wynosi {kursy_walut.get(waluta_od_uzytkownika) * kwota_od_uzytkownika} ")

    print(
        f"Najwiekszy kurs posiada {find_key_for_value(kursy_walut, max(kursy_walut.values()))}:{max(kursy_walut.values())}\nNajmniejszy kurs posiada {find_key_for_value(kursy_walut, min(kursy_walut.values()))}:{min(kursy_walut.values())}")


def quest_v_6():
    dane_logowania = {"admin": "admin", "login": "1234"}
    for ile in range(int(input("ile nowych użykowników chcesz dodać:"))):
        dane_logowania.update({input(f"Podaj {ile + 1} login:"): input(f"Podaj {ile + 1} hasło:")})

    login_od_uzytkownika = input("Podaj Login:")
    haslo_od_uzytkownika = input("Podaj haslo:")
    if login_od_uzytkownika in dane_logowania.keys():
        if haslo_od_uzytkownika in dane_logowania.values():
            print("Zalogowano!")
        else:
            print("Błędne hasło")
    else:
        print("Brak użytkownika o podanym loginie")


# Do 7
def quest_v_7():
    motocykle = {"SuzukiHayabusa": {"marka": "Suzuki", "model": "Hayabusa", "pojemnosc silnika": 1000},
                 "SuzukiGSXR": {"marka": "Suzuki", "model": "GSXR", "pojemnosc silnika": 600},
                 "HondaCBR": {"marka": "Honda", "model": "CBR", "pojemnosc silnika": 600}}

    print(
        f" Honda Model:{motocykle.get('HondaCBR').get('model')} Pojemność:{motocykle.get('HondaCBR').get('pojemnosc silnika')}")


def quest_v_8():
    stolice = {"Polska": "Warszawa", "Andora": "Andora", "Albania": "Tirana", "Chorwacja": "Zagrzeb",
               "Dania": "Kopenhaga"}
    panstwa = ["Polska", "Chorwacja", "Estonia", "Bułgaria", "Grecja", "Albania"]
    for panstwo in panstwa:
        if panstwo in stolice:
            print(f"Stolica {panstwo} to {stolice.get(panstwo)} ")
        else:
            print(f"Brak danych o stolicy państwa {panstwo}")


def quest_v_9():
    menu = {"Jedzenie": {"Stek": 65, "Makaron": 25, "Hamburger": 30}, "Napoje": {"Cola": 5, "Sok": 3, "Sprite": 4}}
    menu.get("Jedzenie").update({"Danie sezonowe": 69})
    menu.get("Jedzenie")["Stek"] = 60
    print(menu)
    menu.get("Jedzenie").pop("Danie sezonowe")
    menu.get("Napoje").pop("Cola")
    print(menu)


def quest_v_10():
    przedmioty_oceny = {"Matematyka": 3, "Hiszpański": 4, "Angielski": 5, "Informatyka": 6}
    przedmioty_oceny_semestr2 = {"Logika": 5, "Polski": 2, "Historia": 3}
    przedmioty_oceny.update(przedmioty_oceny_semestr2)
    for przedmiot, ocena in przedmioty_oceny.items():
        if ocena == 5:
            print(przedmiot)

    print(przedmioty_oceny.values())


def quest_v_11():
     pass