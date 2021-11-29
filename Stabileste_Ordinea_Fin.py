import random
import time


alegereJucator = input('\033[36m' + ">> Alege, par sau impar: \n> ")
alegere = ["par", "impar"]
time.sleep(0.75)
alegereOponent1 = random.choice(alegere)
print("Oponent 1 a ales: " + alegereOponent1 + ".")
alegereOponent2 = random.choice(alegere)
print("Oponent 2 a ales: " + alegereOponent2 + "." + '\033[0m')

# for later use
# red = (\033[31m)
# warning_yellow = (\033[93m)
# green = (\033[32m)
# cyan = (\033[36m)


time.sleep(0.75)
if alegereJucator == alegereOponent1 and alegereJucator != alegereOponent2:
    print('\033[32m' + "> Oponent 2 a fost eliminat! \n")
elif alegereJucator == alegereOponent2 and alegereJucator != alegereOponent1:
    print('\033[32m' + "> Oponent 1 a fost eliminat! \n")
elif alegereJucator == alegereOponent2 and alegereJucator == alegereOponent1:
    print('\033[93m' + "\n> Egalitate!")
else:
    print('\033[31m'"> Ai fost eliminat!" + '\033[0m')


time.sleep(1.5)
ScenariuUnu = (alegereJucator == alegereOponent1 and alegereJucator != alegereOponent2)
ScenariuDoi = (alegereJucator == alegereOponent2 and alegereJucator != alegereOponent1)
ScenariuTrei = (alegereJucator == alegereOponent2 and alegereJucator == alegereOponent1)
ScenariuPatru = (alegereJucator != alegereOponent1 and alegereOponent1 == alegereOponent2)


if ScenariuUnu:
    MicMare = ["mai mare", "mai mic"]
    NumarRandom1 = random.randint(1, 20)
    print("\n\n\n\n\n\n\n\n\n" + '\033[36m' + ">> Numărul inițial este: ", NumarRandom1)
    print(">> Din intervalul (1, 20):")
    NumarRandom2 = random.randint(1, 20)
    alegereOponent1_1 = random.choice(MicMare)
    alegereJucator2 = input("Al doilea numar va fi mai mare sau mai mic ? \n> ")
    time.sleep(1.5)

    if alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mare" and NumarRandom2 >= NumarRandom1:
        print("Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93m' + "\n> Este egalitate...iar...")
        time.sleep(1.8)
        print("\n> Eliminaation !")
        time.sleep(1.3)
        print("> Unul din jucatori va fi eliminat aleoatoriu in...")
        time.sleep(1.8)
        print("\n\n\n\n\n\n\n\n\n> 3")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n> 2")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n> 1")
        time.sleep(1)
        listaJucatoriEliminare = ["Jucator", "Oponent"]
        alegereEliminare = random.choice(listaJucatoriEliminare)
        jucatorEliminat = alegereEliminare
        if jucatorEliminat == "Jucator":
            print("\n\n\n\n\n\n\n\n\n> Ai fost eliminat!")
            time.sleep(1)
            print("\n> Ordinea jucatorilor va fi: Oponent 1, Jucator, Oponent 2")
        else:
            print("\n\n\n\n\n\n\n\n\n> Oponentul 1 a fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Jucator, Oponent 1, Oponent 2")

    elif alegereJucator2 == "mai mic" and alegereOponent1_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93m' + "\n Este egalitate...iar...")
        time.sleep(1.8)
        print("\n\n\n\n\n\n\n\n\n> Eliminaation !")
        time.sleep(1.3)
        print("> Unul din jucatori va fi eliminat aleoatoriu in...")
        time.sleep(1.8)
        print("\n\n\n\n\n\n\n\n\n> 3")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n> 2")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n> 1")
        time.sleep(1)
        listaJucatoriEliminare = ["Jucator", "Oponent"]
        alegereEliminare = random.choice(listaJucatoriEliminare)
        jucatorEliminat = alegereEliminare
        if jucatorEliminat == "Jucator":
            print("\n\n\n\n\n\n\n\n\n> Ai fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Oponent 1, Jucator, Oponent 2")
        elif jucatorEliminat == "Oponent":
            print("\n\n\n\n\n\n\n\n\n> Oponentul 1 a fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Jucator, Oponent 1, Oponent 2")

    elif alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Nimeni nu a ales corect \n ..Jocul se va reseta!")

    elif alegereJucator2 == "mai mic" and alegereOponent1_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033]31m' + "Nimeni nu a ales corect \n ..Jocul se va reseta!")

    elif alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print("Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.45)
        print("Ordinea va fi: Tu, Oponentul 1, Oponentul 2.")

    elif alegereJucator2 == "mai mic" and alegereOponent1_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.45)
        print("Ordinea va fi: Tu, Oponentul 1, Oponentul 2.")

    elif alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.45)
        print("Ordinea va fi: Oponentul 1, Tu, Oponentul 2.")

    else:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.45)
        print("Ordinea va fi: Oponentul 1, Tu, Oponentul 2.")

elif ScenariuDoi:
    time.sleep(1.5)
    MicMare = ["mai mare", "mai mic"]
    NumarRandom1 = random.randint(1, 20)
    print("\n\n\n\n\n\n\n\n\n" + '\033[36m' + ">> Numărul inițial este: ", NumarRandom1)
    print(">> Din intervalul (1, 20): ")
    NumarRandom2 = random.randint(1, 20)
    alegereOponent2_1 = random.choice(MicMare)
    alegereJucator2 = input("Al doilea numar va fi mai mare sau mai mic ? \n> ")

    if alegereJucator2 == ">=" and alegereOponent2_1 == ">=" and NumarRandom2 >= NumarRandom1:
        print("Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93m' + "\nEste egalitate...iar...")
        time.sleep(1.3)
        print("> Eliminaation !")
        time.sleep(1.8)
        print("> Unul din jucatori va fi eliminat aleoatoriu in...")
        time.sleep(1.8)
        print("\n\n\n\n\n\n\n\n\n> 3")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n> 2")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n> 1")
        listaJucatoriEliminare = ["Jucator", "Oponent"]
        alegereEliminare = random.choice(listaJucatoriEliminare)
        jucatorEliminat = alegereEliminare
        if jucatorEliminat == "Jucator":
            print("> Ai fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Oponent 2, Jucator, Oponent 1")
        elif jucatorEliminat == "Oponent":
            print("> Oponentul 2 a fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Jucator, Oponent 2, Oponent 1")

    elif alegereJucator2 == "mai mic" and alegereOponent2_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93m' + "\nEste egalitate...iar...")
        time.sleep(1.3)
        print("> Eliminaation !")
        time.sleep(1.8)
        print("Unul din jucatori va fi eliminat aleoatoriu in...")
        time.sleep(1.8)
        print("\n\n\n\n\n\n\n\n\n3")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n2")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n1")
        listaJucatoriEliminare = ["Jucator", "Oponent"]
        alegereEliminare = random.choice(listaJucatoriEliminare)
        jucatorEliminat = alegereEliminare
        if jucatorEliminat == "Jucator":
            print("> Ai fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Oponent 2, Jucator, Oponent 1")
        else:
            print("> Oponentul 1 a fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Jucator, Oponent 2, Oponent 1")

    elif alegereJucator2 == "mai mare" and alegereOponent2_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Nimeni nu a ales corect \n ..Jocul se va reseta!")

    elif alegereJucator2 == "mai mic" and alegereOponent2_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Nimeni nu a ales corect \n ..Jocul se va reseta!")

    elif alegereJucator2 == "mai mare" and alegereOponent2_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.5)
        print("> Ordinea va fi: Jucator, Oponentul 2, Oponentul 1.")

    elif alegereJucator2 == "mai mic" and alegereOponent2_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.5)
        print("> Ordinea va fi: Jucator, Oponentul 2, Oponentul 1.")

    elif alegereJucator2 == "mai mare" and alegereOponent2_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.5)
        print("> Ordinea va fi: Oponentul 2, Jucator, Oponentul 1.")

    else:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1 + ".")
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.5)
        print("> Ordinea va fi: Oponentul 2, Jucator, Oponentul 1.")

elif ScenariuTrei:
    time.sleep(0.45)
    print('\033[93m' + "> Jucati din nou")

else:
    print('\033[31m' + "> Deci nu mai are rost...")
    time.sleep(0.75)
    print("> Joaca din nou!")
