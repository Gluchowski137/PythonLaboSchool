def quest1():
    name = "Krzysztof Gluchowski"
    print(name[0:name.find(" ")])
    print(name[name.find(" ") + 1:])
    print(name[0])
    print(name[name.find(" ") + 1])
    print(len(name))
    print(name.count("a"))
    print(name.upper())


def quest2():
    def check_name():
        name = input("Name: ")
        if name.isalpha():
            if not name[0].isupper():
                name[0].upper()
            if name[-1] == "a":
                gender = "Female"
            else:
                gender = "Male"
            return (name, gender)
        else:
            print("Only letters in name!")
            check_name()

    def check_surname():
        surname = input("Surname: ")
        if surname.isalpha():
            if not surname[0].isupper():
                surname[0].upper()
            return surname
        else:
            print("Only letters in name!")
            check_surname()

    def check_email():
        email = input("Email: ")
        if email.count("@") == 1:
            return email
        else:
            print("Wrong email")
            check_email()

    def check_phone_number():
        phone_number = input("Phone Number: ")
        if phone_number.isdigit() and len(phone_number) == 9:
            return phone_number

        else:
            print("please past correct phone number")
            check_phone_number()

    name = check_name()
    surname = check_surname()
    email = check_email()
    phone_number = check_phone_number()
    dane_osobowe = f"{str(name[0])} {surname} {email} {phone_number} {str(name[1])}"
    print(dane_osobowe)
    print(len(dane_osobowe))


def quest3():
    dna = """CCTACGggGGGcaGCAGTAgggAAtctTCCGC-ATGGACGAAA
GTCTGACGGAGCNACGCCGCGTGAacgAAGAAGGCCTTCGGGT
CGtaaAGTTCTGT-GTTAGGGAAGAACAAGTACCAGAGTAACT
GCTGGTACcTTGAcGGTACctaaCCAGA--GCCACGGCTAA-T
ACGTGCCAGCAgcCGCGGTAATACGTAGGTGGCAAGCGTTGTC
CGGAATTATTG-GCGTAAAGCGCNCGCAGGTGGTTGCANTANG"""
    for x in range(dna.count("-")):
        dna = dna[0:dna.find("-")] + dna[dna.find("-") + 1:]
    for x in range(dna.count("N")):
        dna = dna[0:dna.find("N")] + dna[dna.find("N") + 1:]
    dna = dna.upper()
    print(dna)
    print(
        f"A:{dna.count('A')} \nC:{dna.count('C')}\nG:{dna.count('G')}\nT:{dna.count('T')}\nGTAA:{dna.count('GTAA')}\nGGG:{dna.find('GGG')}")

    dna = dna.replace("A","U")
    dna = dna.replace("C", "g")
    dna = dna.replace("T", "A")
    dna = dna.replace("G", "C")
    print(dna.upper())

