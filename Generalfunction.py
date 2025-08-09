def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def subtract(x,y):
    return x-y

def modulus(x,y):
    return x%y

def floor(x,y):
    return x//y

def greetings(exit):
    return"Hello",exit
print("options")
print("1.addition")
print("2.multiplication")
print("3.subtraction")
print("4.modulus")
print("5.floor division")
print("6.Exit")
user_option= int(input())
if user_option==1:
    x=int(input("Enter your number:"))
    y=int(input("Enter your number:"))
    print(add(x,y))
elif user_option==2:
    x=int(input("Enter your number:"))
    y=int(input("Enter your number:"))
    print(multiply(x,y))    
elif user_option==3:
    x=int(input("Enter your number:"))
    y=int(input("Enter your number:"))
    print(subtract(x,y))
elif user_option==4:
     x=int(input("Enter your number:"))
     y=int(input("Enter your number:"))
     print(modulus(x,y))
elif user_option==5:
    x=int(input("Enter your number:"))
    y=int(input("Enter your number:"))
    print(floor(x,y))
elif user_option==6:
    print("exit")
else:
    print("invalid option")     
        