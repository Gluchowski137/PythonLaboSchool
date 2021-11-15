import random


def quest1():
    def randomnumbers():
        random_numbers = open("ThingsForProjects/numbers.txt", "w")
        for x in range(100):
            random_numbers.write(f"{random.randint(-10, 10)}\n")
        random_numbers.close()

    filepath = "ThingsForProjects/numbers.txt"
    numbers = open(filepath, "r")
    numbers_with_name = open("ThingsForProjects/numbers_with_name.txt", "w")
    for line in numbers.readlines():
        line = line[:line.find(" ")]
        if line[0] == "-":
            numbers_with_name.write(line + " Ujemna\n")
        elif line[0] == "0":
            numbers_with_name.write(line + " Zero\n")
        else:
            numbers_with_name.write(line + " Dodatnia\n")

    numbers.close()
    numbers_with_name.close()


def quest2():
    def randomresults():
        test = open("ThingsForProjects/test_results.txt", "w")
        numer = ["A", "B", "C"]
        for x in range(100):
            test.write(f"{random.randint(0, 100)}{random.choice(numer)}\n")
        test.close()

    test = open("ThingsForProjects/test_results.txt", "r")
    group_test = open("ThingsForProjects/group_test_results.txt", "w")
    a_results = [0, 0]
    b_results = [0, 0]
    c_results = [0, 0]
    for line in test.readlines():
        line = line[:line.find(" ")]
        if "A" in line:
            a_results[0] += int(line[:line.find("A")])
            a_results[1] += 1
        elif "B" in line:
            b_results[0] += int(line[:line.find("B")])
            b_results[1] += 1
        elif "C" in line:
            c_results[0] += int(line[:line.find("C")])
            c_results[1] += 1

    group_test.writelines(f"GroupA:MEAN {round(a_results[0] / a_results[1], 2)} Students: {a_results[1]}\n")
    group_test.write(f"GroupB:MEAN {round(b_results[0] / b_results[1], 2)} Students: {b_results[1]}\n")
    group_test.write(f"GroupC:MEAN {round(c_results[0] / c_results[1], 2)} Students: {c_results[1]}")

    test.close()
    group_test.close()


def quest3():
    pass
