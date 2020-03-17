#################
####VARIABLES####
#################

###create a variable
#x = 1
#print(x)
'''
name = "john"
print(name)

a=1 #int
b=2 #int
c=3.5 #float
hi = "Hello World" #string
print(hi)
'''

'''
print('what is your name?')
name = input()
print('Hi')
print(name)
'''
'''
first_name = input("what is your first name?")
last_name = input("what is your last name?")
address_line1 = input("what is the first line of your address?")
post_code = str(input("what is your post code?"))
birthdate = input("what is your birthdate")
age = int(input("how old are you?"))
print("Hi {} {}, you live at {} {} and your birthdate is {}, making you {} years old.".format(first_name, last_name,address_line1,post_code, birthdate, age))
'''

###ARITHMETIC OPERATORS###
# a=24
# # b=16
# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(4*'me')
# # print(8%3) #remainder

###STRING OPERATORS###
# example = "hello there!"
# print(example.upper())
# # .lower
# # .capitalize
# print(example.replace("!","?"))

# a='here ' #concatenation
# b='more'
# c=10
# print(a+b,c)

###boolean methods###
# hi ="hello world"
# print(hi.isalpha()) #uses the alphabet
# print(hi.islower()) #is lower case?
# print(hi.isupper()) #is upper case?
# print(hi.endswith("d"))
# print(hi.startswith("h"))

###reversing a string###
# s = input("input a word")
# print(bool(s[::-1]==s))

###########
###LISTS###
###########
#
# shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1])
# shopping_list[1] = "crackers"
# print(shopping_list)
# shopping_list.pop() # removes last item
# shopping_list.append("aubergine") #add an item
# print(len(shopping_list)) #show size of the list
#
# #mixed data types:
# mixed =[1,2,3,"one","two","three"]
# print(mixed)
#
# #list slicing:
# print(mixed[1:3])
# print(mixed[1::3])
# print(mixed[-2::-1])

########
###IF###
########
# a=int(input("giz us a number  "))
# b=int(input("giz us anuther 1  "))
# c=int(input("uno mass  "))
# if a>b and a>c:
#     print("{} is the largest number".format(a))
# elif b>a and b>c:
#     print("{} is the largest number".format(b))
# elif c>b and c>a:
#     print("{} is the largest number".format(b))
# else:
#     print("two or more of the numbers are the same")

# z=int(input("number plz  "))
# if (z%2==0):
#     print("{} is an even number!".format(z))
# else:
#     print("{} is an odd number!".format(z))

###############
###FOR LOOPS###
###############
#iterate your way through elements of a list of collection of items
# shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
# for item in shopping_list:
#     print(item)

list =[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for num in list:
    if num<5:
        new_list.append(num)
    else:
        print(num)

print(new_list)



