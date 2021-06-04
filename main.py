import os
introMsg = """ 
*****************************************************************************************
* Welcome,stranger.                                                                     *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.  *
* In a country where magic rules, anything is possible if you wish so.                  *
* It all depends on you, brave hero.                                                    *
*****************************************************************************************
"""

print(introMsg)
print("Would you like to start the adventure ?")
print("Yes or No")
user_answer = input("Yes or No -> ")
if user_answer.upper() == "YES":
    print("OK")
    os.system("cls") #windows

else:
    print("Thanck you, good bye")