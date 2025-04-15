# input() = A function that prompts the user to enter data returns
#           the entered data as a string

name = input("What is your name: ")
age = int(input("How old are you?: "))
age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} old!")

# Example1: Find the area of rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"Area of {length} length and {width} width rectangle is {area}")


# Example2: Shooping cart program
item = input("What item would you like to buys?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} {item}/s")
print(f"Your total is: {total}")