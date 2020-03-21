import random

import time





def get_tof_statements():

    statements = []

    statements.append(["Penguins can fly", "F"])

    statements.append(["Jupiter is the fifth planet from the sun", "T"])

    statements.append(["Sydney is the capital of Australia", "F"])

    return statements



def play_tof_quiz():

    # generate tof statements

    tof_statements = get_tof_statements()

    # shuffle into the statements and randomises

    random.shuffle(tof_statements)

    score = 0

    for x in tof_statements:

        print("True or False: " + x[0])

        guess = input("Enter T or F: ").upper()

        if guess == x[1]:

            print("Correct :)")

            score = score + 1

            time.sleep(1)

        else:

            print("Incorrect :(")

            time.sleep(1)

    if score == len(tof_statements):

        print("You aced it {}! Well done :)".format(name))

        quit()

    else:

        print("Thank you for playing {}, your final score is: {}/".format(name, score) + str(len(tof_statements)))

        quit()







def get_gk_statements():

    statements = []

    statements.append(["Which country won the 2012 Olympics Gold Medal in football? ", "mexico"])

    statements.append(["What is the second largest country in the world?", "canada"])

    statements.append(["Who sang the song 'Love Yourself'?", "justin bieber"])

    return statements



def play_gk_quiz():

    gk_statements = get_gk_statements()

    random.shuffle(gk_statements)

    score = 0

    for x in gk_statements:

        print("Question: " + x[0])

        guess = input("Answer: ").lower()

        if guess == x[1]:

            print("Correct :)")

            score = score + 1

            time.sleep(1)

        else:

            print("Incorrect :(")

            time.sleep(1)

    if score == len(gk_statements):

        print("You aced it {}! Well done :)".format(name))

        quit()

    else:

        print("Thank you for playing {}, your final score is: {}/".format(name, score) + str(len(gk_statements)))

        quit()







name = input("What is your name?")

print("Welcome to the Quiz Master {}!".format(name))

time.sleep(1)



def main_menu():

    print("Please select an option:")

    time.sleep(1)

    print("1. Play True or False quiz  ")

    print("2. Play General Knowledge quiz ")

    print("0. Quit")

    time.sleep(1)

    choice = input("Enter 1, 2 or 0:")

    if choice == "1":

        play_tof_quiz()

    elif choice == "2":

        play_gk_quiz()

    elif choice == "0":

        print("Thanks for playing {}!".format(name))

        quit()





main_menu()



play_tof_quiz()



play_gk_quiz()