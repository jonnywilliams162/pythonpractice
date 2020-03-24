########################
### WORKING WITH CSV ###
########################

import csv

# with open("user_details.csv",newline='') as csvfile:
#     csvreader = csv.reader(csvfile,delimiter=",")
#
#     print(csvreader)
#
#     for row in csvreader:
#         print(row)
#
#     for row in csvreader:
#         print(row[-1])


#utilising some of the built in mehods
#iter(), and next()
# with open("user_details.csv",newline='') as csvfile:
#     csvreader = csv.reader(csvfile,delimiter=",")
#
#     iterable = iter(csvreader)
#     next(iterable) #to skip the next line, so it skips the first line: or can skip certain details
#     for row in iterable:
#         next(iterable)  # to skip the next line, so in the loop it skips every other line: or can skip certain details
#         print(row[-1])

### CHANGING DATA ###
#APPEND to end of the data:

def transform_user_details(csv_file_name):
    new_user_data= []

    with open(csv_file_name,newline='') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")

        for user in csvreader:
             transformation=[]
             transformation.append(user[0])
             transformation.append(user[1])
             transformation.append(user[-1])
             new_user_data.append(transformation)
    return new_user_data

print(transform_user_details("user_details.csv"))

# Create a csv file and copy information for user_details.csv to new_user_details.csv
def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name='new_user_data.csv'):
    new_user_data = transform_user_details(old_user_data_file)
    new_file = open(new_file_name, 'w')
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)
create_new_user_data_csv()





