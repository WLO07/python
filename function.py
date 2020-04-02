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


def PasswordGenerator():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    password=''
    while True:
        try:
            lenth=(int(input("Veuillez saisir la longueur de mot de passe entre 6 et 20: \n")))
            if (lenth <6 or lenth >= 20):
                print("entre 6 et 20 !\n")
            else:
               break
        except ValueError:
            print("Veuillez saisir un entien SVP !\n")
    for c in range(lenth):
        password+=random.choice(chars)
    print(password)
    return(password)

def calculatens(string):
    lettre=0
    nombre=0
    for i in string:
        if (i.isdigit()):
            nombre=nombre+1
        else:
            lettre=lettre+1
    return (lettre, nombre)
  
def checkpassword (password):
    if (not(any(char.isupper() for char in password)) or (not any(char.islower() for char in password)) or (not any(char.isdigit() for char in password))):
        PasswordGenerator() 
    else:
        print(password)

