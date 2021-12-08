import random
import time

alegereJucator = input('\033[36m' + ">> Alege, par sau impar: \n> ")
alegere = ["par", "impar"]
time.sleep(.75)
alegereOponent1 = random.choice(alegere)
print(f"Oponent 1 a ales: {alegereOponent1}.")
alegereOponent2 = random.choice(alegere)
print(f"Oponent 2 a ales: {alegereOponent2}.")

#for later use
#with another type of print:  // print(f"{warning_yellow}") //
red = '\033[31m'
warning_yellow = '\033[93m'
green = '\033[32m'
cyan = '\033[36m'
endline = '\033[0m'

time.sleep(.75)
if alegereJucator == alegereOponent1 and alegereJucator != alegereOponent2:
    print(f"{green} > Oponent 2 a fost eliminat! \n")
elif alegereJucator == alegereOponent2 and alegereJucator != alegereOponent1:
    print(f"{green} > Oponent 1 a fost eliminat! \n")
elif alegereJucator == alegereOponent2 and alegereJucator == alegereOponent1:
    print(f"{warning_yellow} \n> Egalitate!")
else:
    print(f"{red} > Ai fost eliminat! {endline}")

time.sleep(1.5)
ScenariuUnu = (alegereJucator == alegereOponent1 and alegereJucator != alegereOponent2)
ScenariuDoi = (alegereJucator == alegereOponent2 and alegereJucator != alegereOponent1)
ScenariuTrei = (alegereJucator == alegereOponent2 and alegereJucator == alegereOponent1)
ScenariuPatru = (alegereJucator != alegereOponent1 and alegereOponent1 == alegereOponent2)

if ScenariuUnu:
    MicMare = ["mai mare", "mai mic"]
    NumarRandom1 = random.randint(1, 20)
    print(f"\n\n\n\n\n\n\n\n\n{cyan} >> Numărul inițial este: {NumarRandom1}.")
    print(">> Din intervalul (1, 20):")
    NumarRandom2 = random.randint(1, 20)
    alegereOponent1_1 = random.choice(MicMare)
    alegereJucator2 = input("Al doilea numar va fi mai mare sau mai mic ? \n> ")
    time.sleep(1.5)
    if alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mare" and NumarRandom2 >= NumarRandom1:
        print(f"Oponentul 1 a ales: {alegereOponent1_1}")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n\n{warning_yellow} > Este egalitate...iar...")
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
            print(f"\n\n\n\n\n\n\n\n\n{red} > Ai fost eliminat!")
            time.sleep(1)
            print(f"\n> Ordinea jucatorilor va fi: Oponent 1, Jucator, Oponent 2")
        else:
            print(f"\n\n\n\n\n\n\n\n\n{green} > Oponentul 1 a fost eliminat!")
            time.sleep(1)
            print(f"\n> Ordinea jucatorilor va fi: Jucator, Oponent 1, Oponent 2")
    elif alegereJucator2 == "mai mic" and alegereOponent1_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print(f"{cyan} Oponentul 1 a ales: {alegereOponent1_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n\n{warning_yellow} > Este egalitate...iar...")
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
            print(f"\n\n\n\n\n\n\n\n\n{red} > Ai fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Oponent 1, Jucator, Oponent 2")
        elif jucatorEliminat == "Oponent":
            print(f"\n\n\n\n\n\n\n\n\n{green} > Oponentul 1 a fost eliminat!")
            time.sleep(1)
            print("Ordinea jucatorilor va fi: Jucator, Oponent 1, Oponent 2")
    elif alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print(f"{cyan} Oponentul 1 a ales: {alegereOponent1_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n Nimeni nu a ales corect \n ..Jocul se va reseta!")
    elif alegereJucator2 == "mai mic" and alegereOponent1_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print(f"{cyan} Oponentul 1 a ales: {alegereOponent1_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Nimeni nu a ales corect \n ..Jocul se va reseta!")
    elif alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print(f"Oponentul 1 a ales: {alegereOponent1_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{green} Ai castigat!")
        time.sleep(.45)
        print("Ordinea va fi: Tu, Oponentul 1, Oponentul 2.")
    elif alegereJucator2 == "mai mic" and alegereOponent1_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print(f"{cyan} Oponentul 1 a ales: {alegereOponent1_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{green} Ai castigat! \n")
        time.sleep(0.45)
        print("Ordinea va fi: Tu, Oponentul 1, Oponentul 2.")
    elif alegereJucator2 == "mai mare" and alegereOponent1_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print(f"{cyan} Oponentul 1 a ales: {alegereOponent1_1}")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Ai pierdut!")
        time.sleep(0.45)
        print("Ordinea va fi: Oponentul 1, Tu, Oponentul 2.")
    else:
        print(f"{cyan}Oponentul 1 a ales: {alegereOponent1_1}")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Ai pierdut!")
        time.sleep(.45)
        print("Ordinea va fi: Oponentul 1, Tu, Oponentul 2.")
elif ScenariuDoi:
    time.sleep(1.5)
    MicMare = ["mai mare", "mai mic"]
    NumarRandom1 = random.randint(1, 20)
    print(f"\n\n\n\n\n\n\n\n\n{cyan} >> Numărul inițial este: {NumarRandom1}")
    print(">> Din intervalul (1, 20): ")
    NumarRandom2 = random.randint(1, 20)
    alegereOponent2_1 = random.choice(MicMare)
    alegereJucator2 = input("Al doilea numar va fi mai mare sau mai mic ? \n> ")
    if alegereJucator2 == ">=" and alegereOponent2_1 == ">=" and NumarRandom2 >= NumarRandom1:
        print(f"Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n\n{warning_yellow} Este egalitate...iar...")
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
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n\n{warning_yellow} Este egalitate...iar...")
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
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}.")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Nimeni nu a ales corect \n ..Jocul se va reseta!")
    elif alegereJucator2 == "mai mic" and alegereOponent2_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}.")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Nimeni nu a ales corect \n ..Jocul se va reseta!")
    elif alegereJucator2 == "mai mare" and alegereOponent2_1 == "mai mic" and NumarRandom2 >= NumarRandom1:
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}.")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{green} Ai castigat! \n")
        time.sleep(.5)
        print("> Ordinea va fi: Jucator, Oponentul 2, Oponentul 1.")
    elif alegereJucator2 == "mai mic" and alegereOponent2_1 == "mai mare" and NumarRandom2 <= NumarRandom1:
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}.")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{green} Ai castigat! \n")
        time.sleep(.5)
        print("> Ordinea va fi: Jucator, Oponentul 2, Oponentul 1.")
    elif alegereJucator2 == "mai mare" and alegereOponent2_1 == "mai mic" and NumarRandom2 <= NumarRandom1:
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}.")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Ai pierdut!")
        time.sleep(.5)
        print("> Ordinea va fi: Oponentul 2, Jucator, Oponentul 1.")
    else:
        print(f"{cyan} Oponentul 2 a ales: {alegereOponent2_1}.")
        print(f"Al doilea numar a fost: {NumarRandom2}.")
        time.sleep(1.5)
        print(f"\n\n\n\n\n\n\n\n\n{red} Ai pierdut!")
        time.sleep(.5)
        print("> Ordinea va fi: Oponentul 2, Jucator, Oponentul 1.")
elif ScenariuTrei:
    time.sleep(.45)
    print(f"{warning_yellow} > Jucati din nou")
else:
    print(f"{red} > Deci nu mai are rost...")
    time.sleep(.75)
    print("> Joaca din nou!")
