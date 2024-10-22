# type casting

name = "amith"
age = 18
is_student = True

type(name) # gives  type of data

print(type(name)) # gives str
print(type(age)) # gives int

age = str(age) # converts type of age to string

print(type(age)) # gives str

name = bool(name)

print(name) # give true