#################
### FUNCTIONS ###
#################

#IS A SPECIAL RELATIONSHIP WHERE EACH INPUT HAS A SINGLE OUTPUT

#FUNCTION WITHOUT ARGUMENTS:
# def hello():
#     print("hello")
# hello()

#function with arguments:
# def func(a,b):
#     return a+b
# print("the sum is",func(10,20))

# #function with default arguments:
# def func(a=10,b=20):
#     return a+b
# print(func())

# #FUNCTIONS WITH DEFAULT AND PASSING THE VALUES:
# def func(a=10,b=20):
#     return a+b
# print(func(20,40)) #takes the inputted values over the default ones

# def multiplication(a,b):
#     return a*b
# print(multiplication(45,37))


#############
### CLASS ###
#############
# A WAY OF BRINGING BOTH DATA AND FUNCTIONALITY TOGETHER
#A class is a way to create objects

# class Dog:
#     animal_kind = "canine" # class variable
#     def __init__(self,name):
#         self.name = name
#     def bark(): #referencing the class you are currently in
#         return "woof"
# print(Dog.animal_kind)
# print(Dog.bark())
#
# #creating a student class:
# class Student:
#     student_type = "trainee"
#
#     def enrol():
#         return "All Good"
# print(Student.student_type)
# print(type(Student))

# #so define the class:
# class myclass:
#     x=5
#
# #now can use this class to creat objects
# obj1 = myclass()
# print(obj1.x)

#ALL CLASSES HAVE A FUCNTION CALLED __INIT__(), WHICH IS ALWAYS EXECUTED WHEN THE CLASS IS BEING INITIATED
#USE THE INIT FUNCTION TO ASSIGN VALUES TO OBJECT PROPERTIES OR OTHER OPERATIONS THAT ARE DONE WHEN THE OBJECT IS BEING CREATED

#create a class named person, use the init function to assign values for name and age:
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
# p1=person("John",36)
# print(p1.name)
# print(p1.age)

#objects can also contain methods
#functions that belong to the object/class
#the 'self' parameter is a reference to the current instance of the class
#is used to access variables that belong to the class
#it does not have to be names 'self' but it has to be the first parameter of any function in the class

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
#
#     def myfunc(self):
#         print("Hello my name is " + self.name)
# p1=person("John",36)
# p1.myfunc()
#
# #modify properties of an object:
# p1.age=40
# print(p1.age)
# #delete the age property from p1
# del p1.age
# #delete objects
# del p1

# class Fizzbuzz:
#     def caluction(num):
#             if int(num) % 3 == 0 and int(num) % 5 == 0:
#                 print("Fizzbuzz")
#             elif int(num) % 3 == 0:
#                 print("Fizz")
#             elif int(num) % 5 == 0:
#                 print("Buzz")
#             else:
#                 print('incorrect value')
#
#
# print(Fizzbuzz.caluction(15))

# class students:
#
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#     def year(self):
#         if self.age =='14':
#             return '{} is in year 7'.format(self.name)
#         elif self.age =='12':
#             return '{} is in year 5'.format(self.name)
#     def what_gender(self):
#         if self.gender == 'Male':
#             return '{} is male'.format(self.name)
#
# x=students('Jack','12','Male')
# y=students('Jill','14','Female')
#
# print(x.what_gender())
# print(y.year())





############################
### LIBRARIES AND MODULES###
############################
# import random
# import math
#
# print(random.random())
# num_float = 23.66
# print(math.ceil(num_float)) #gives highest value
# print(math.floor(num_float)) #gives lowest value




