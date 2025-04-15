# Type casting = The process of converting a variable from one data type to another
#                str(), int(), float(), bool()

name = "Dilakshan"
age = 25
gpa = 3.6
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = str(age)
age += "1"
print(age)

name1 = ""
name1 = bool(name1)
print(name1)