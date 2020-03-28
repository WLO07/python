def getage():
    while True:
        try:
            age=(int(input("Veuillez saisir votre age: ")))
            if (age <0 or age >= 120):
                print("Veuillez saisir un age compris entre 1 et 120 !")
            else:
               break
        except ValueError:
            print("Veuillez saisir un entien SVP !")
    print(age)
    return (age)



getage()