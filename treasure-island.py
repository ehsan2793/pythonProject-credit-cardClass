print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print('Welcome to Tresure Island.\nYour mission is to find the the tresure')

choice= input("Youre at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()

if  choice == 'left':
    choice= input('You come to a Lake. There is an island in the middle of the Lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice == 'swim':
        choice = input("you waited for few hours and magical beast apeard in fornt of you. It offered you a ride do you accpet Type 'yes' or 'no' ").lower()
        if choice == 'yes':
            choice = input('beast gave you ride to island and ask you to give him half of the tresure. do you accpet Type "yes" or "no" ').lower()
            if choice == 'yes':
                pass

    else:
        choice= input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?')
        if choice == 'red':
            pass
        elif choice == 'yellow':
            pass
        else:
            print('You enter a room of beasts. Game Over.')

else:
    pass
