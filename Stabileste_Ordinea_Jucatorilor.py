import random
import time


alegereJucator = input('\033[36m' + ">> Alege, par sau impar: \n")
alegere = ["par", "impar"]
time.sleep(0.75)
alegereOponent1 = random.choice(alegere)
print("Oponent 1 a ales: " + alegereOponent1)
alegereOponent2 = random.choice(alegere)
print("Oponent 2 a ales: " + alegereOponent2 + '\033[0m')


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
    MicMare = [">=", "<="]
    NumarRandom1 = random.randint(1, 20)
    print("\n\n\n\n\n\n\n\n\n" + '\033[36m' + ">> Numărul inițial este: ", NumarRandom1)
    NumarRandom2 = random.randint(1, 20)
    alegereOponent1_1 = random.choice(MicMare)
    alegereJucator2 = input("Al doilea numar va fi >= sau =< ? \n ")
    time.sleep(1.5)

    if alegereJucator2 == ">=" and alegereOponent1_1 == ">=" and NumarRandom2 >= NumarRandom1:
        print("Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93m' + "\nEste egalitate...")
        time.sleep(0.5)
        print("  iar...")
        time.sleep(0.35)
        print("> Joaca din nou.")

    elif alegereJucator2 == "<=" and alegereOponent1_1 == "<=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93' + "\nEste egalitate...")
        time.sleep(0.5)
        print("  iar...")
        time.sleep(0.35)
        print("> Joaca din nou.")

    elif alegereJucator2 == ">=" and alegereOponent1_1 == ">=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Nimeni nu a ales corect \n ..Mai joaca o data!")

    elif alegereJucator2 == "<=" and alegereOponent1_1 == "<=" and NumarRandom2 >= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033]31m' + "Nimeni nu a ales corect \n ..Mai joaca o data!")

    elif alegereJucator2 == ">=" and alegereOponent1_1 == "<=" and NumarRandom2 >= NumarRandom1:
        print("Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.45)
        print("Ordinea va fi: Tu, Oponentul 1, Oponentul 2.")

    elif alegereJucator2 == "<=" and alegereOponent1_1 == ">=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.45)
        print("Ordinea va fi: Tu, Oponentul 1, Oponentul 2.")

    elif alegereJucator2 == ">=" and alegereOponent1_1 == "<=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.45)
        print("Ordinea va fi: Oponentul 1, Tu, Oponentul 2.")

    else:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent1_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.45)
        print("Ordinea va fi: Oponentul 1, Tu, Oponentul 2.")

elif ScenariuDoi:
    time.sleep(1.5)
    MicMare = [">=", "<="]
    NumarRandom1 = random.randint(1, 20)
    print("\n\n\n\n\n\n\n\n\n" + '\033[36m' + ">> Numărul inițial este: ", NumarRandom1)
    NumarRandom2 = random.randint(1, 20)
    alegereOponent2_1 = random.choice(MicMare)
    alegereJucator2 = input("Al doilea numar va fi >= sau =< ? \n ")

    if alegereJucator2 == ">=" and alegereOponent2_1 == ">=" and NumarRandom2 >= NumarRandom1:
        print("Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93' + "\nEste egalitate...")
        time.sleep(0.5)
        print("  iar...")
        time.sleep(0.35)
        print("> Joaca din nou.")

    elif alegereJucator2 == "<=" and alegereOponent2_1 == "<=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[93m' + "\nEste egalitate...")
        time.sleep(0.5)
        print("  iar...")
        time.sleep(0.35)
        print("> Joaca din nou.")

    elif alegereJucator2 == ">=" and alegereOponent2_1 == ">=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Nimeni nu a ales corect \n ..Mai joaca o data!")

    elif alegereJucator2 == "<=" and alegereOponent2_1 == "<=" and NumarRandom2 >= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Nimeni nu a ales corect \n ..Mai joaca o data!")

    elif alegereJucator2 == ">=" and alegereOponent2_1 == "<=" and NumarRandom2 >= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.5)
        print("> Ordinea va fi: Tu, Oponentul 2, Oponentul 2.")

    elif alegereJucator2 == "<=" and alegereOponent2_1 == ">=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[32m' + "Ai castigat! \n")
        time.sleep(0.5)
        print("> Ordinea va fi: Tu, Oponentul 2, Oponentul 1.")

    elif alegereJucator2 == ">=" and alegereOponent2_1 == "<=" and NumarRandom2 <= NumarRandom1:
        print('\033[36m' + "Oponentul 2 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.5)
        print("> Ordinea va fi: Oponentul 2, Tu, Oponentul 1.")

    else:
        print('\033[36m' + "Oponentul 1 a ales: ", alegereOponent2_1)
        print("Al doilea numar a fost: ", NumarRandom2)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n" + '\033[31m' + "Ai pierdut!")
        time.sleep(0.5)
        print("> Ordinea va fi: Oponentul 2, Tu, Oponentul 1.")

elif ScenariuTrei:
    time.sleep(0.45)
    print('\033[93m' + "> Jucati din nou")

else:
    print('\033[31m' + "> Deci nu mai are rost...")
    time.sleep(0.75)
    print("> Joaca din nou!")
