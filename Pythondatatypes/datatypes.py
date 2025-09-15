import sys
# varibales 

my_cool_varibale = 42 

print(my_cool_varibale) 

# numbers integers, whole numbers  float decimal numbers  and complex number 

my_fist_int = 10

my_second_int = 20

# small integers -5 to 256 are cached by python and larger integers are not cached 

my_large_int = 10000000*10000000

print(sys.getsizeof(my_large_int))
print(sys.getsizeof(my_fist_int))

#floats
my_first_float = 10.5
my_second_float = 20.5

print( my_first_float + my_second_float)
print(type(my_first_float + my_fist_int))

# string a string is naything inside single or double quotes 
my_first_string = "Hello"

# string are dynamically allocated in memory

print(my_first_string)

print(f"the size of my string is {sys.getsizeof(my_first_string)} bytes")

# triple quotes for multi line strings

print(f'this is my first string : "{my_first_string}"')

# string and integers dont mix 

print(str(my_fist_int) + my_first_string)

# boolean True or False 

very_good_data = True
very_bad_data = False

print(type(very_good_data))
print(type(very_bad_data))
print(very_good_data + very_bad_data)

# = is assignment operator and == is comparison operator

print(very_good_data == very_bad_data)  

print(very_good_data != very_bad_data)  

# None is a special data type in python
my_var = None
my_first_var = 10
my_second_var = 20

#print(my_var + my_first_var + my_second_var) # None is treated as 0 in numeric operations but not in python

#lists
my_first_list = [
    1, 
    2, 
    3, 
    4,
      5,
      'True'
      ]

print(my_first_list)
my_first_list[-1] = "banana"
print(my_first_list)

# tuples are immutable lists

my_first_tuple = (1, 2, 3, 4, 5)
print(my_first_tuple[2])

my_new_string = "Hello World"

print(my_new_string[2:6])
print(my_new_string[2:])
print(my_new_string[:6])

# dictionaries are key value pairs
my_first_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(my_first_dict)
print(my_first_dict["name"], my_first_dict["age"])

my_second_dict = {
    "name": "Jane",
    "age": 25,
    "city": "Los Angeles"
}

print(my_second_dict["name"], my_second_dict["age"]),print(my_first_dict["name"], my_first_dict["age"])


favorite_cars = {
    "John": "BMW",
    "Jane": "Audi",
    "Mike": "Mercedes"
}

if favorite_cars == []:
    print("No favorite cars")
elif "John" in favorite_cars:
    print(f"John's favorite car is {favorite_cars['John']}")
else:
    for name, car in favorite_cars.items():
        print(f"{name}'s favorite car is {car}")

#match statement
code = 200
match code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case 300:
        print("Unknown Error")


for car in favorite_cars:
    if car == "John":
        print(f"John's favorite car is {favorite_cars[car]}") 
        break
    elif car == "Jane":
        print(f"Jane's favorite car is {favorite_cars[car]}")
        continue      
    else:
        print(f"'s favorite car is ")