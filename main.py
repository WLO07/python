from function import getname, getage, gettime, PasswordGenerator

name=getname()
age=getage()
password=PasswordGenerator()
print(str(gettime()) + "  Votre usermane est " + name + str(age)+ "  et votre password est " + password)