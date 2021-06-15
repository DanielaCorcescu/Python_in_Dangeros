import os
import winsound
import Player


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


    elif answer == '2':
        player_name = input("""You heve chosen to be a mighty wizard 
What is your name? -> """)
        player = Player.Wizard(player_name)
        print("Intro the world")
        os.system('cls')

    else:
        print("Chose a valid option")
else:
    print("Thanck you, good bye")