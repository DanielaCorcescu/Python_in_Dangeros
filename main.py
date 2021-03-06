import os
import winsound
import Enemy

import Player
import random


introMsg = """ 
*****************************************************************************************
* Welcome,stranger.                                                                     *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.  *
* In a country where magic rules, anything is possible if you wish so.                  *
* It all depends on you, brave hero.                                                    *
*****************************************************************************************
"""

sound = "Main_Menu.wav"
winsound.PlaySound(sound, winsound.SND_ASYNC)
print(introMsg)
print("Would you like to start the adventure ?")
print("Yes or No")
user_answer = input("Yes or No -> ")
if user_answer.upper() == "YES":
    print("OK")
    os.system("cls") #windows
    answer = input("""What type of player are you: 
1 for Warrior 2 for Wizard -> """)
    if answer == '1':
        player_name = input("""You heve chosen to be a mighty warrior 
What is your name? -> """)
        player = Player.Warrior(player_name)
    elif answer == "2":
        player_name = input("""You have chosen to be a mighty Wizard 
                What is your name? -> """)
        player = Player.Wizard(player_name)
    print("Intro the world")
    input("Press a key to continue... ")


    os.system('cls')
    sound = "Exploring.wav"
    winsound.PlaySound(sound, winsound.SND_ASYNC)
    print("""You are in the middle of a crossroads.
You have 3 paths in front of you:
1. Going to a village
2. Going to a forest
3. Going to desert  """)
    path_option = input("What is your destiny? ")

    """Create a metod path(userPath)
    that uses the returned value from crossroads method"""

    if path_option == '1':
        #in_the_village() from utils
        print("You are in the village...")
        print("From a backside ally a enemy appears")
        random_number = random.randint(0, 2)

        sound = "BattleFinal.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        enemy = None
        if random_number == 0:
            enemy = Enemy.Goblin()

        elif random_number == 1:
            enemy = Enemy.Orc()

        elif random_number == 2:
            enemy = Enemy.Rat()

        else:
            print("Invalid enemy...")

        print("You met a...",enemy.name)
        option = input("Attack or Run? (A/R) ")
        if option == "A":
            print("You killed your enemy, You WIN! ")
        elif option == "R":
            print("you didn't run, very fast and you were Killed... ")





    elif path_option == '2':
        #in_the_forest()
        print("You are in the forest")
        random_number = random.randint(0, 2)

        sound = "BattleFinal.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        enemy = None
        if random_number == 0:
            enemy = Enemy.Goblin()

        elif random_number == 1:
            enemy = Enemy.Orc()

        elif random_number == 2:
            enemy = Enemy.Rat()

        else:
            print("Invalid enemy...")

        print("You met a...", enemy.name)
        option = input("Attack or Run? (A/R) ")
        if option == "A":
            print("You killed your enemy, You WIN! ")
        elif option == "R":
            print("you didn't run, very fast and you were Killed... ")

    elif path_option == '3':
        #in_the_desert()
        print("You are in the desert...")
        random_number = random.randint(0, 2)

        sound = "BattleFinal.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        enemy = None
        if random_number == 0:
            enemy = Enemy.Goblin()

        elif random_number == 1:
            enemy = Enemy.Orc()

        elif random_number == 2:
            enemy = Enemy.Rat()

        else:
            print("Invalid enemy...")

        print("You met a...", enemy.name)
        option = input("Attack or Run? (A/R) ")
        if option == "A":
            print("You killed your enemy, You WIN! ")
        elif option == "R":
            print("you didn't run, very fast and you were Killed... ")
    else:
        print("Path not available")


else:
    print("Thanck you, good bye")