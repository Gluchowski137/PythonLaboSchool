def quest():
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

