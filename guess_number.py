import random
logo ="""

░██████╗░███╗░░██╗░██████╗░
██╔════╝░████╗░██║██╔════╝░
██║░░██╗░██╔██╗██║██║░░██╗░
██║░░╚██╗██║╚████║██║░░╚██╗
╚██████╔╝██║░╚███║╚██████╔╝
░╚═════╝░╚═╝░░╚══╝░╚═════╝░

"welcome to the Guess Number Game(GNG).

"""

print(logo)

def gng():
    print("Im think of a number between 1 and 100.")
    difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")

    random_number = random.randint(1,100)

    if difficulty == "easy":
        numer_of_choices = 10

    elif difficulty == "hard":
        numer_of_choices = 5

    while numer_of_choices > 0 :
        print(f"you have {numer_of_choices} remaining to guess the number.")
        guess = int(input('make a guess: '))

        if guess == random_number:
            print("You won")
            numer_of_choices= 0

        elif guess > random_number:
            print("Too High")
            print("Guess again")

        else:
            print("Too Low")
            print("Guess again")

        numer_of_choices-= 1

while input("Do you want to play GNG: 'yes' or 'no': ") == "yes":
    gng()
