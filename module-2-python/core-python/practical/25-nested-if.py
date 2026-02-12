# nested if meanse if within another if i.e called nested if 

"""
syntax 
if condition:
 if condition:
   statements
else:
  statements

"""

a=50
b=20
if a>b:
    if a!=0 and b!=0:
        print("a is greater than b and both are positive numbers")
else:
    print("a is less than b")