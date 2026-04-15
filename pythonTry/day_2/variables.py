# Day 2: 30 Days of python programming
import math

firstName = "Justine"
lastName = "DC"
fullName = "Justine DC"
country = "Ph"
city = "lp"
age = 26
year = 2026
is_married = False
is_true = True
is_light_on = False
testDate, examNo, score, items = "05/22/2026", 427178, 95, 100

print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(testDate), type(examNo), type(score), type(items))

print(len(firstName))

print("firstName length: ", len(firstName), " vs lastName length: ", len(lastName))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print("Area of circle with radius 30:", area_of_circle)
print("Circumference of circle with radius 30:", circum_of_circle)
user_radius = input('User input Radius: ')
area_of_circle = math.pi * radius ** 2

user_firstName = input('User First Name: ')
user_lastName = input('User Last Name: ')
user_country = input('User Country: ')
user_age = input('User Age: ')

#help('keywords')