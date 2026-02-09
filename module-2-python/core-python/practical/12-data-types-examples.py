# integer or int
# a=10
# print(type(a))

# a=1554552562121
# print(type(a))

# float or decimal
a=10.56
print(type(a))
# string or str : set of characters enclosed in single or double quotes
b="brijesh"
c='brijesh'
print(type(b))
print(type(c))

# boolean or bool : True or False
d=True
print(type(d))
e=False
print(type(e))

#list : collection of items enclosed in square brackets []
# list can contain items of different data types
# list is mutable : we can change the items of list
# list is ordered : we can access the items of list using index
# list is iterable : we can loop through the items of list
# list is heterogeneous : we can store different data types in a list


# employee=["brijesh", "kumar", "pandey", 10, 20.56, True]
# print(type(employee))

# list=[10,20,30,40,50]
# print(type(list))
# print(list)
# print(list[0]) # access first item of list
# print(list[1]) # access second item of list
# print(list[2]) # access third item of list


#list is mutable : we can change the items of list
list=[10,20,30,40,50]
print(list)
list[0]=100 # change first item of list
print(list)
list[1]=200 # change second item of list    
print(list)
list[2]=300 # change third item of list
print(list)
list[3]=400 # change fourth item of list
print(list)
list[4]=500 # change fifth item of list
print(list)



# tuple : collection of items enclosed in parentheses ()
# tuple can contain items of different data types
# tuple is immutable : we cannot change the items of tuple
# tuple is ordered : we can access the items of tuple using index
# tuple is iterable : we can loop through the items of tuple
# tuple is heterogeneous : we can store different data types in a tuple

tuple_example=(10,20.56,"brijesh",True)
print(type(tuple_example))
print(tuple_example)
# tuple_example[0]=100 # this will throw an error because tuple is immutable
# print(tuple_example)


# set : collection of items enclosed in curly braces {}
# set can contain items of different data types
# set is mutable : we can change the items of set
# set is unordered : we cannot access the items of set using index

set_example={10,20.56,"brijesh",True}
print(type(set_example))
print(set_example)
set_example.add(100) # add an item to set
print(set_example)
set_example.remove(10) # remove an item from set
print(set_example)



# dictionary : collection of key-value pairs enclosed in curly braces {}
# dictionary can contain items of different data types
# dictionary is mutable : we can change the items of dictionary
# dictionary is unordered : we cannot access the items of dictionary using index
# dictionary is iterable : we can loop through the items of dictionary
# dictionary is heterogeneous : we can store different data types in a dictionary

# dictionary_example={"name":"brijesh","age":25,"city":"delhi"}
# print(type(dictionary_example))
# print(dictionary_example)

# mutable : we can change the items of mutable data types
# immutable : we cannot change the items of immutable data types

# examples of mutable data types : list, set, dictionary
# examples of immutable data types : int, float, str, tuple, bool


# create an dictionary with employee details
employee={"name":"brijesh","age":25,"city":"delhi","salary":50000}
print(type(employee))
print(employee)
employee["name"]="kumar" # change the value of name key
employee["age"]=30 # change the value of age key
employee["city"]="mumbai" # change the value of city key
employee["salary"]=60000 # change the value of salary key
print(employee)

# remove an item from dictionary
del employee["salary"] # remove the salary key-value pair from dictionary
print(employee)

# add a new key-value pair to dictionary
employee["department"]="IT" # add a new key-value pair to dictionary
print(employee)

# access the value of a key in dictionary
# print(employee["name"]) # access the value of name key
print(employee["department"]) # access the value of department key

# access the value of a key in dictionary using get() method
print(employee.get("name")) # access the value of name key using get() method
print(employee.get("department")) # access the value of department key using get() method

# access the value of a key that does not exist in dictionary
print(employee.get("salary")) # this will return None because salary key does not exist in dictionary

# a
# print(type(a))

# opearte=10+20
# print(type(opearte))



# none : it is a special data type that represents the absence of value
# none is immutable : we cannot change the value of none

# examples of none data type
none_example=None
print(type(none_example))


# complex : it is a data type that represents complex numbers
complex_example=10+20j
print(type(complex_example))

# examples of complex numbers
complex_example1=10+20j
complex_example2=5-10j
print(complex_example1)
print(complex_example2)



