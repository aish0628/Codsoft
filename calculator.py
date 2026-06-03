def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
   try :
       return a/b
   except ZeroDivisionError:
       return "Sorry, you cannot divide by zero"
print("="*40)
print("          CALCULATOR")
print("="*40)

while True :
    try :
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError :
        print("Enter a valid number")
        continue

    print("Choose Operation :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice(1,2,3,4) : "))
    print("="*40)

    if choice == 1:
        result = add(num1,num2)
        print(num1,"+",num2,"=",result)
    elif choice == 2:
        result = sub(num1,num2)
        print(num1,"-",num2,"=",result)
    elif choice == 3:
        result = mul(num1,num2)
        print(num1,"*",num2,"=",result)
    elif choice==4:
        result = div(num1,num2)
        print(num1,"/",num2,"=",result)
    else :
        print("Invalid choice")
    print("="*40)
    again = input("Do you want to continue? (yes/no) : ").lower()
    if again != "yes":
       break