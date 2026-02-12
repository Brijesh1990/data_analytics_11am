# if elif  if are executed when condition is true elif is check multiple true condition if elif false else is executed  

# multiline comment
"""
syntax 

if condition:
 statements
elif condition:
 statements
elif condition:
 statement
else:
   statements

"""

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))

# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("a and b both are equal")         


# w.a.p to print among three numbers a max values 

# n1=int(input("Enter N1 values :"))
# n2=int(input("Enter N2 values :"))
# n3=int(input("Enter N3 values :"))

# if n1>n2 and n1>n3:
#     print("N1 is max Numbers ")
# elif n2>n1 and n2>n3:
#     print("N2 is max Numbers")

# elif n3>n2 and n3>n1:
#     print("N3 is max Numbers")

# else: 
#     print('something went wrong try again')
#     exit;    


# w.a.p to print to addition when user input 1, substraction when user input 2, multiplication when user input 3,division when user input 4


a=int(input("Enter a values :"))
b=int(input("Enter b values :"))

res=int(input("Enter numbers 1 for additions , 2 for substraction , 3 for multiplications  :"))


if res==1:
    c=a+b 
    print("Additions of numbers is :",c)

elif res==2:
    c=a-b 
    print("Substractions of numbers is :",c)

elif res==3:
    c=a*b 
    print("Multiplications of numbers is :",c)

else: 
    print("sorry you cant select proper numbers")
