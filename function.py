import random
import datetime

def getname():
    while True:
        name=(str(input("Veuillez enter votre nom \n")))
        if (len(name) < 3):
            print("Minimaum 3 caractere \n")
        else:
            break
    return(name)


def getage():
    while True:
        try:
            age=(int(input("Veuillez saisir votre age: \n")))
            if (age <0 or age >= 120):
                print("Veuillez saisir un age compris entre 1 et 120 !\n")
            else:
               break
        except ValueError:
            print("Veuillez saisir un entien SVP !\n")
    return (age)


def gettime():
    currentDT = datetime.datetime.now()
    return (currentDT.strftime("%Y-%m-%d %H:%M:%S"))