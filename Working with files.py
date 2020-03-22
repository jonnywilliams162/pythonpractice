###################################################
#### WORKING WITH, READING IN AND SAVING FILES ####
###################################################

#'open()' takes two parameters: 'filename and mode'
#four different modes:
#'r' - read (default value)
#'a' - append
#'w' - write
#'x' - creates the specified file
#should specify if the file should be handled as binary or text mode 't' or 'b'

#syntax:
# file = open("demofile.txt")
# file = open("demofile.txt","rt") #these are the same as r for read and t for text are the defau;t
# print(file.read()) #will print out the contents of the file
# print(file.read(5))#will display only first 5 characters of the file
# print(file.readline())#will return one line, by calling this twice you can see the first two lines
#
# for x in file
#     print(x) #this loop will print the whole file line by line
#
# #it is good practice to close the file once done with it to save space and memory
# file.close()

###writing to an existing file ###
# f = open("demofile.txt", "a") #the "a" allows you to append to the existing file
# f.write("more content for the file")
# f.close()
#
# f=open("demofile.txt","w") #"w" will overwrite the existing content of the file!
# f.write("woops i have deleted the content")
# f.close

### Create a new file ###
#can use the modes: 'a,x or w'
#'x' is the proper way, the others will just make one if there isnt one with the name you put in already

# f=open("myfile.txt","x")
# f.write("first bit of content for myfile")

### Delete files ###
# must import the 'os' module and run its 'os.remove()' function
import os
#os.remove("demofile.txt")

#check if file exists
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("the file does not exist")

#to delete an entire folder use 'os.rmdir()' remove directory
# os.rmdir("myfolder")
