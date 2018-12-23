def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Sélectionner une opération.")
print("1.Addition")
print("2.Soustraction")
print("3.Multiplication")
print("4.Division")

choice = input("Entrez votre choix(1/2/3/4):")

num1 = int(input("Entrez le premier nombre: "))
num2 = int(input("Entrez le second nombre: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Saisie invalide")
