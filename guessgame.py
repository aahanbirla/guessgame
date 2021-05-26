import random
user_name = "name"
turns_list = []
def score():
    if len(turns_list) <= 0:
        print("There isn't any score.")
    else:
        print("Your score is {}, WELL DONE!".format(turns_list))
def start_random():
    global user_name
    randomno = int(random.randint(1,10))
    user_name = input("Welcome to the game\nWhat is your name?\n")
    print("Welcome {}".format(user_name))
    choice = input("Would you like to play this game?(yes/no)\n")
    turns = 0
    score()
    while choice.lower()!= "no":
                nom = int(input("Enter a number between 1 and 10\n"))
                if type(nom) == int:
                    if nom < 1 or nom > 10:
                        print("Enter number within range")
                    if nom == randomno:
                        print("Congratulations, you guessed it right")
                        turns += 1
                        score()
                        print(user_name,"you guessed it in {} turns".format(turns))
                        turns_list.append(turns)
                        choice = input("Would you like to continue?!\n(Yes/No)\n")
                    elif randomno % 2 == 0:
                        print("You guessed it wrong\n(hint: It's an even number)")
                        turns += 1
                    elif nom > randomno:
                        print("Number guessed is higher\n(hint: Guess lower)")
                        turns += 1
                    elif nom < randomno:
                        print("Number guessed is lower\n(hint: Guess higher)")
                        turns +=1
                else:
                    print("You haven't entered a number, please try again.")
start_random()
print("Hope to see you again!, Come back soon")