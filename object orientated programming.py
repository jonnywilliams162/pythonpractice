#####################################
### OBJECT ORIENTATED PROGRAMMING ###
#####################################

##4 PILLARS OF OOP:
# ABSTRACTION
# INHERITENCE
# ENCAPSULATION
# POLYMORPHISM

#abstraction is displaying only essential info to the user and hiding the details from the user
#inheritence is where one class takes the property of another class: is useful to prevent having to repeat yourself
        #class newclass(oldclass):
            #super(). __init__(name,age) #super allows the new class to take all of the methods from the original class
# #so if we make a parent class of people:
class people(object):
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

        #create an object
p1=people("John","Smith")
p1.printname()

#now lets use that parent class to create a child class called students
class students(people):
    pass #use pass to not add any other properties or methods
s1=students("emma","wing")
s1.printname()

class students(people):
    def __init__(self,fname,lname,age): ##add the variable 'age' specifically for the sub-class
        super().__init__(fname, lname)
        self.age=age
        self.fname=fname
    def printage(self):
        print(self.age)
    def func(self):
        print("{} is a student".format(self.fname))
s2=students("James","Hill",12)
s2.printage()
s2.func()
s2.printname()



#####################
### ENCAPSULATION ###

#restricting access to methods and variables
#this can prevent data from being modified by accident
#not allowing the user to access the method
#use '__' before the name of the method to prevent it from being used -  it will be unusable in it's child classes and the class it is in

# class child(students):
#
#     def __init__(self,fname,lname,age):
#         super().__init__(fname,lname,age)
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def __secondary(self):
#         return("I am in secondary school")
#     def primary(self):
#         return("I am in primary school")
#
# child1=child("Luke","Bond",16)
# print(child1.primary()) #currently all the methods from both parent classes and this class are available to use
# print(child1.secondary()) #returns an error saying 'child does not have the attribute secondary'


####################
### POLYMORPHISM ###

#Methods in a child class that have the same name as a method in a parent class
#it is possible to modify the method in  the child class - known as method overriding
class child(students):

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)
        self.fname=fname
        self.lname=lname
        self.age=age
    def __secondary(self):
        return("I am in secondary school")
    def primary(self):
        return("I am in primary school")
    def printage(self): #the little cirlce to the left shows that you are overriding a previous method
        return("{}, thats old af".format(self.age))

child2=child("Harry","Bond",15)
print(child2.printage()) #so the function of the child class takes precedence over the parent class





