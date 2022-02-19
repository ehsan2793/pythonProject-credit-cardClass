from higher_lower_data import data
import random
logo = """
██╗░░██╗██╗░██████╗░██╗░░██╗███████╗██████╗░  ░█████╗░██████╗░  ██╗░░░░░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░
██║░░██║██║██╔════╝░██║░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗
███████║██║██║░░██╗░███████║█████╗░░██████╔╝  ██║░░██║██████╔╝  ██║░░░░░██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝
██╔══██║██║██║░░╚██╗██╔══██║██╔══╝░░██╔══██╗  ██║░░██║██╔══██╗  ██║░░░░░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗
██║░░██║██║╚██████╔╝██║░░██║███████╗██║░░██║  ╚█████╔╝██║░░██║  ███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝  ╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝

"""
def compare(Choice,B,A):
    if Choice == 'A':
        return A['follower_count'] > B['follower_count']
    else:
        return B['follower_count'] > A['follower_count']
game_ends = False
score = 0
while not game_ends:
    endRange = len(data) -1

    randomNum1 = random.randint(0,endRange)
    randomNum2 = random.randint(0,endRange)

    item1 = data[randomNum1]
    item2 = data[randomNum2]


    item1['name']

    print(f" A: {item1['name']}, {item1['description']}, from {item1['country']}")
    print(f" B: {item2['name']}, {item2['description']}, from {item2['country']}")

    choice = input("who has more followers: ")
    result = compare(choice,item1,item2)

    if result:
        score +=1
    else:
        print(f"You lose and your score is {score}")
        game_ends = True
