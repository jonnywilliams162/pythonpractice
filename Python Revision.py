#######################################################
### HERE IS A MESS OF PRACTICE OF ALL THINGS PYTHON ###
#######################################################

###############
## FUNCTIONS ##

# def myfunc(x,y):
#     print(x*y)
# myfunc(5,7)
#
# def name(fname,lname):
#     print(fname+ " " + lname)
# name("Jonny", "Williams")
#
# def arbarg(*food): #Arbitrary arguments, if you don't know how many arguments you need to pass you can put a * in front
#     print(food[2])    #the function will receive a tuple of arguments and can access them accordingly
# arbarg("bread","cheese","grapes")
#
# #using keyword arguments
# def key(child3,child2):
#     print(child3)
# key(child2="james",child3="sarah") #using the keywords allows you to not bother about the order of input
#
# #kwargs
# #if you dont know how many keyword arguments are needed us **
# def kwarg(**child):
#     print(child["lname"]) #this 'lname' has to be in speech marks
# kwarg(fname="james",lname="chong")
#
# #default parameter function
# #if we call the function with no arguments it will use the default
# def countries(country="England"):
#     print("I am from "+country)
# countries()
# countries("Sweden")
#
# #Passing a list as an argument::
# #You can send any data types of argument to a function and it will be treated as such
#
# def listfunc(food):
#     for x in food:
#         print(x)
# fruits =["apple","banana","Strawb"]
# listfunc(fruits) ###So here we could set up a complex loop as a function and pass ready made lists or columns through it
#
# #Returning a value (does not print)
# def ret(x):
#     return 5*x
# print(ret(2))

#### RECURSION ###
# a function can call itself
# can loop through data to reach a result

# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k-2)
#         print(result)
#     else:
#         result=0 # this is the base case that allows the function to end
#     return result
# tri_recursion(6)

#####Recursive factorial function::
# def get_recursive_factorial(n):
#     if n<0:
#         return -1 #error check
#     elif n<2:
#         return 1 #base case
#     else:
#         return n * get_recursive_factorial(n-1) #return n times the factorial of the number below
#
# #iterative factorial function: (using loop)
# def get_iterative_factorial(n):
#     if n<0:
#         return -1
#     else:
#         fact=1
#         for i in range(1,n+1): #n+1 =n as the range is non-inclusive
#             fact *= i
#         return fact
# print(get_recursive_factorial(6))
# print(get_iterative_factorial(6))

### LAMBDA FUNCTIONS ###
#is a small anonymous function
#can take any number of arguments but only one expression
#lambda arguments : expression

#a simple lambda function that adds 10 to the number passed in as an argument and print the result:
# x = lambda a: a+10
# print(x(5))
#
# x = lambda a,b: a*b
# print(x(5,10))
#
# #THE power of lambda functions are better appreciated when used as an anonymous function inside another function
# #say you have a function than takes 1 argument and multiplies it with an unknown number
# def lamb(n):
#     return lambda a: a*n
# todouble = lamb(2) #defining n as 2
# print(todouble(11))#passing 11 through lamb where n=2 and a=11
# totriple=lamb(3)
# print(totriple(11)) #making another function out of that function

###############
### CLASSES ###

#A way to create own types of data entries
# has data ATTRIBUTES and METHODS
#use these classes to create objects
# class circle(object):
#     def __init__(self,radius,colour):
#         self.radius=radius;
#         self.colour=colour;
# #so now we have the class, lets make an object that follows the type of the class
# red_circle = circle(10,"red") #radius of 10 and red in colour
# print(red_circle.radius)
# print(red_circle.colour)
# red_circle.colour = "blue" #change the attributes of the object

#
# class circle(object):
#     def __init__(self,radius,colour):
#         self.radius=radius;
#         self.colour=colour;
#     def add_radius(self,r):
#         self.radius=self.radius + r #so we are adding a function to the class that allows us to alter the radius
# red_circle=circle(10,"red")
# red_circle.add_radius(8)
# #so the radius should now be 18
# print(red_circle.radius) #hooray!

#### INHERITENCE::
#allows us to define a class that inherits the properties from a parent class
# so if we make a parent class of people:
# class people(object):
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
#
#         #create an object
# p1=people("John","Smith")
# p1.printname()
#
# #now lets use that parent class to create a child class called students
# class students(people):
#     pass #use pass to not add any other properties or methods
# s1=students("emma","wing")
# s1.printname()

#################
### ITERATORS ###

#An object that contains a countable number of values
#can be iterated upon i.e. you can traverse through all the values
#lists,tuples,dictionaries and sets are all iterable objects
#all these objects have an ' iter() ' method which is used to get an interator

# mytuple= ("apple","banana","cherry")
# # myit=iter(mytuple)
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# #
# # #even strings are iterable
# # mystr="Jonny"
# # myit2=iter(mystr)
# # print(next(myit2))
# # print(next(myit2))
# # print(next(myit2))
# # print(next(myit2))
# # print(next(myit2))

#for loops will go through an iterable object
# mytuple= ("apple","banana","cherry")
# for x in mytuple:
#     print(x)

#CREATING AN ITERABLE CLASS:
#Have to use ' __iter__ ' instead of ' __init__ '
#The ' __next__ ' METHOD allows you to do operations on the next item in the sequence

#e.g. create an iterator that returns numbers starting with 1

# class mynumbers():
#     def __iter__(self,):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a +=1
#         return x
# myclass=mynumbers()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#this would go on forever in a for loop
#so use the StopIteration statement
#
# class mynumbers():
#     def __iter__(self,):
#         self.a=1
#         return self
#     def __next__(self):
#        if self.a <20:
#             x=self.a
#             self.a +=1
#             return x
#        else:
#            raise StopIteration
# myclass=mynumbers()
# myiter=iter(myclass)
# for x in myiter:
#     print(x)

################
### DATETIME ###

#python does not have a default data type for dates but we can import a module calles 'datetime'

import datetime
# x=datetime.datetime.now()
# print(x) #date contains year, month,day,hour,minute,second and microsecond
# print(x.year)
# print(x.strftime("%A")) #prints day of the week
# print(x.month)

#to create a date we can use the datetime() class constructor
#requires 3 parameters: year,month,day

# x = datetime.datetime(2020, 2, 18)
# print(x)

#strftime formats the date and time into readbale string objects:
# x = datetime.datetime(2020, 2, 18)
# print(x.strftime("%B"))
# print(x.strftime("%A"))
# print(x.strftime("%Y")) #there are loads of syntax to show different values of the date: w3 schools has a great table explaining each of them


############
### JSON ###
############
#JSON is a syntax for storing and exchanging data
#JSON is text written with JavaScript notation


