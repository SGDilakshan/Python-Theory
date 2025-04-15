import math

friends = 10
friends += 1     #friends = friends + 1
friends -= 2     #friends = friends - 2
friends *= 3    #friends = friends * 3
friends /= 5     #friends = friends / 5
friends **= 2     #friends = friends ** 2
remainder = friends % 3
# print(remainder)

x = 9.9
y = -4
z = 5
# result = round(x)
# result = abs(y)
# result = pow(4,3)
# result = max(x,y,z)
# result = min(x,y,z)
# print(result)

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

#Example 1: Calculate the circumference of the circle

# radius = float(input("Enter the radius: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference of {radius} cm radius circle is {round(circumference, 2)}cm")

#Example 2: Calculate the area of the circle

# area = math.pi * radius * radius
# area = math.pi * pow(radius,2)
# print(f"The area is: {round(area,2)}")

# Example 3: Calculate the length of hypothesis of right angle triangle
a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(c)