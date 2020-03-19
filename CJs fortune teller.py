'''

A game inspired by 'cootie catchers', where colours and numbers are used to tell your future!

Theme of fortune given depends on the colour the user chooses.

Use of time module to mimic the programme thinking.

Use of dictionary to store all fortunes linked to colour (keys)

Has a 'go again' feature to automatically restart the programme if the user wants to know another fortune.

'''



import time



fortune = {

    "red": {

        "fortune one": "Be careful or you could fall for some tricks today!",

        "fortune two": "You have a secret admirer!"

    },

    "green": {

        "fortune three": "Now is a good time to buy stock!",

        "fortune four": "Be careful how you spend this week - you are set to lose a lot!"

    },

    "blue": {

        "fortune five": "Failure is the chance to do better next time!",

        "fortune six": "The harder you work, the luckier you get!"

    },

    "yellow": {

        "fortune seven": "Don’t just spend time - invest it!",

        "fortune eight": "Remember to share good fortune as well as bad with your friends!"

    }

}



TRY = 1



print("Hello, friend! I am the GREAT ZORBINI")

time.sleep(1)



print("Let me tell you your fortune for this week..")

time.sleep(1)



name = input("First, tell me your name: ")

print("Hi {}, what do you want to know about?".format(name.capitalize()))

time.sleep(1)



while TRY != 0:

    print("Choose a colour:\nRed for Love\nGreen for Money\nBlue for Work \nYellow for Friendship")

    chosen_colour = input()

    try:

        chosen_number = int(input("Now choose either 1 or 2: "))

    except ValueError:

        print("{}, please insert a numeric character!".format(name.capitalize()))

        time.sleep(1)

    else:

        if chosen_number < 1 or chosen_number > 2:

            print("You can only choose 1 or 2 {}! Try again.".format(name.capitalize()))

            time.sleep(1)

        else:

            print("Hmm. the universe is speaking to me...")

            time.sleep(2)



            for colour in fortune:

                if chosen_colour.lower() == "red":

                    if chosen_number == 1:

                        print(fortune["red"].get("fortune one"))

                    else:

                        print(fortune["red"].get("fortune two"))

                    break

                elif chosen_colour.lower() == "green":

                    if chosen_number == 1:

                        print(fortune["green"].get("fortune three"))

                    else:

                        print(fortune["green"].get("fortune four"))

                    break

                elif chosen_colour.lower() == "blue":

                    if chosen_number == 1:

                        print(fortune["blue"].get("fortune five"))

                    else:

                        print(fortune["blue"].get("fortune six"))

                    break

                elif chosen_colour == "yellow":

                    if chosen_number == 1:

                        print(fortune["yellow"].get("fortune seven"))

                    else:

                        print(fortune["yellow"].get("fortune eight"))

                    break

            time.sleep(2)

            go_again = input("So {}, do you want another try? Y/N: ".format(name.capitalize()))

            if go_again.upper() == "Y":

                TRY += 0

            else:

                TRY -= 1