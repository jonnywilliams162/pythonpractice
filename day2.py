###################
### COLLECTIONS ###
###################
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

# list =[1,2,3,4,5,6,7,8,9,10]
# new_list=[]
# for num in list:
#     if num<5:
#         new_list.append(num)
#     else:
#         print(num)
#
# print(new_list)

#EXAMPLE ARE THE NUMBERS ODD OR EVEN?
# start_list = [10,11,24,56,78,75,65,80]
# even_list = []
# odd_list =[]
# for num in start_list:
#     if num%2 ==0:
#         even_list.append(num)
#         print("added to the even list: ",even_list)
#     else:
#         odd_list.append(num)
#         print("added to the odd list: ", odd_list)
# print('final even list: ',even_list)
# print('final odd list: ', odd_list)


### TUPLES ###
##############
# essentials = ("bread","eggs","milk")
# print(essentials.count("bread"))
# #essentials[0]="beans" # this throws an error as the items in a tuple cannot be changes

### DICTIONARIES ###
####################

# student = {
#     "name" : "Jonny",
#     "stream": "data",
#     "completed_lessons": 4,
#     "completed_lesson_names": ["sql","business","python","excel"] #a list as a value
# }
# print(student["stream"])
#
# #changing a value:
# student["stream"]="tech"
# print(student["completed_lesson_names"][1])
#
# #removing a value
# student["completed_lesson_names"].remove("business")
# print(student)

#looping through a dict:
# for x in student: #just the keys
#     print(x) #prints the names of all the keys
#
# for x, y in student.items(): #runs through all of the keys and values
#   print(x, y)
#
# for x in student.values(): #runs through just the values
#   print(x)


### SETS ###
############

# thisset = {"apple", "banana", "cherry"}
# # #print(thisset)
# # #for x in thisset:
# #   #print(x)
# # #print("banana" in thisset)
# # thisset.add("lollipop")#can add items by 'add' OR 'update
# # thisset.update(['grape','milk','truffle']) # adds a list to the set
# # for x in thisset:
# #   print(x)
# #
# # print(len(thisset))
# # thisset.remove("banana") #remove an item
# #
# # print(thisset)

####################
### CONTROL FLOW ###
####################

#If statements
# age = 19
# if age>19:
#     print("old")
# elif age<19:
#     print("young")
# else:
#     print("you're 19")

# film_rating = input("what is the film rating?")
# if film_rating.lower() == "universal":
#     print("all age groups can watch this film")
# elif film_rating.lower() == "pg":
#     print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating == "15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating == "18":
#     print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#     print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

# number = int(input("put in a number for fizzbuzz game "))
# number_list = list(range(1,number+1))
# for n in number_list:
#     if (n % 3 ==0) and (n %5 ==0):
#         print("Fizzbuzz")
#     elif n %3 ==0:
#         print("Fizz")
#     elif n%5 ==0:
#         print("Buzz")
#     else:
#         print("party pooper")

##embedded list:
# list_data = [1,2,3,4,5,6]
# # embedded_list = [[1,2,3],[4,5,6]]
# # for data in embedded_list:
# #     print(data)
# #     for num in data:
# #         print(num)

# dict_data = {1:{"name":"Bronson","money":"50"},2:{"name":"masha","money":"3.66"},3:{"name":"roscoe","money":"319.80"}}
# #
# # for value in dict_data:
# #     print(value)
# # for item in dict_data.values():
# #     for embed_values in item.values():
# #         print(embed_values)

### WHILE LOOP ###
##################
# x=0
# while x<10:
#     print("its working --> {x}")
#     x=x+1



