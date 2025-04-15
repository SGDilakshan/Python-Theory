# Variable: A Container for a value(String, integer, float, boolean)
# A variable behaves as if it was the value it contains

#String
first_name = "Dilakshan"
food = "Pizza"
email = "dilakshan@gmail.com"

#Integers
age = 25
quantity = 3
num_of_students = 30

#Float
price = 10.99
gpa = 3.99
distance = 5.5

#Boolean
is_student = True
print(f"Are you a Student?: {is_student}")

print(first_name)
print("first_name")

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

print(f"Your are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

print(f"The price us ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

if is_student:
    print("You are a Student")
else:
    print("You are not a student")

for_sale = False
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

is_online = True
if is_online:
    print("You are online")
else:
    print("You are offline")