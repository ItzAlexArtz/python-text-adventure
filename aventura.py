import time
import random

#game function
def game():

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Welcome to the cavern of secrets!")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     
    time.sleep(3)

    print ("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    ch1 = str(input("Do you take it? [y/n]: "))



    #STICK TAKEN
    if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You have taken the stick!")
        time.sleep(2)
        stick = 1

    #STICK NOT TAKEN
    else:
        print("You did not take the stick")
        stick = 0

    print ("As you proceed further into the cave, you see a small glowing object")
    ch2 = str(input("Do you approach the object? [y/n]"))

    #APPROACH SPIDER
    if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print ("You approach the object...")
        time.sleep(2)
        print ("As you draw closer, you begin to make out the object as an eye!")
        time.sleep(1)
        print ("The eye belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it? [Y/N]"))

        #APPROACH SPIDER
    elif ch2 in ['n', 'N', 'No', 'NO', 'no']:
        print ("You don't approach the object...")
        time.sleep(2)
        print ("As you walk away, the object begins to come closer to you!")
        time.sleep(1)
        print ("The object is an eye that belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it? [Y/N]"))

    # FIGHT SPIDER
    if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:

        # WITH STICK
        if stick == 1:
            print("You only have a stick to fight with!")
            print("You quickly jab the spider in it's eye and gain an advantage")
            time.sleep(2)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                  Fighting...                   ")
            print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
            print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(2)
            fdmg1 = int(random.randint(3, 10))
            edmg1 = int(random.randint(1, 5))
            print("you hit a", fdmg1)
            print("the spider hits a", edmg1)
            time.sleep(2)

            if edmg1 > fdmg1:
                print ("The spider has dealt more damage than you!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the spider, but you manage to escape")
                complete = 1
                return complete

            else:
                print ("You killed the spider!")
                print ("As you want to walk away you heard a girl screaming!")
                explore = input ('Do you want to find out who screamed? [y/n] ')
                if explore in ['y', 'Y', 'yes', 'YES', 'Yes', ]:
                    print ("As you where going further into the cave, you see a princess!")
                    fight = input("Do you want to save her?")
                    if fight in ['y', 'Y', 'yes', 'YES', 'Yes', ]:
                        print ("As you walk closer to her a skeleton with a sword and a shield reveals himself from the darkness of the cave!")
                        fight = str(input("Do you try to fight it? [Y/N]"))
                        if fight in ['y', 'Y', 'yes', 'YES', 'Yes', ]:
                            print ("You choose to fight it!")
                            time.sleep(2)
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("                  Fighting...                    ")
                            print("   YOU MUST HIT ABOVE A 20 TO KILL THE Skeleton  ")
                            print("IF THE Skeleton HITS HIGHER THAN YOU, YOU WILL DIE")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            time.sleep(2)
                            fdmg1 = int(random.randint(20, 30))
                            edmg1 = int(random.randint(10, 15))
                            print("you hit a", fdmg1)
                            print("the skeleton hits a", edmg1)
                            time.sleep(2)
                            complete = 1
                            return complete


        # WITHOUT STICK
        else:
            print("You don't have anything to fight with!")
            time.sleep(2)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                  Fighting...                   ")
            print("   YOU MUST HIT ABOVE A 10 TO KILL THE SPIDER    ")
            print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(2)
            fdmg1 = int(random.randint(10, 12))
            edmg1 = int(random.randint(1, 5))
            print("you hit a", fdmg1)
            print("the spider hits a", edmg1)
            time.sleep(2)

            if edmg1 > fdmg1:
                print ("The spider has dealt more damage than you!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the spider, but you manage to escape")
                complete = 1
                return complete

            else:
                print ("You killed the spider!")
                print ("As you want to walk away you heard a girl screaming!")
                explore = input ('Do you want to find out who screamed? [y/n]')
                fight = input("Do you want to save her? [y/n]")
                if explore in ['y', 'Y', 'yes', 'YES', 'Yes']:
                    print ("As you where going further into the cave ,you saw a princess! Do you want to save her?")
                    if fight in ['y', 'Y', 'yes', 'YES', 'Yes', ]:
                        print ("As you walk closer to her a skeleton with a sword and a shield reveals himself from the darkness of the cave!")
                        fight = str(input("Do you try to fight it? [Y/N]"))
                        if fight in ['y', 'Y', 'yes', 'YES', 'Yes', ]:
                            print ("You choose to fight it!")
                            time.sleep(2)
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("                  Fighting...                    ")
                            print("   YOU MUST HIT ABOVE A 20 TO KILL THE Skeleton  ")
                            print("IF THE Skeleton HITS HIGHER THAN YOU, YOU WILL DIE")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            time.sleep(2)
                            fdmg1 = int(random.randint(1, 20))
                            edmg1 = int(random.randint(1, 15))
                            print("you hit a", fdmg1)
                            print("the skeleton hits a", edmg1)
                            time.sleep(2)
                            complete = 1
                            return complete

    #DON'T FIGHT SPIDER
    elif ch3 in ['n', 'N', 'No', 'NO', 'no']:
        print ("You choose not to fight the spider.")
        time.sleep(1)
        print ("As you turn away, it ambushes you and impales you with it's fangs!!!")
        complete = 0
        return complete

    
                
# game loop
alive = True
while alive:

    complete = game()
    if complete == 1:
        alive = input('You managed to escape the cavern alive! Would you like to play again? [y/n]: ')
        if alive in ['y', 'Y', 'YES', 'yes', 'Yes',]:
            alive
        else:
            break
    else:
        alive = input('You have died! Would you like to play again? [y/n]: ')
        if alive in ['y', 'Y', 'YES', 'yes', 'Yes',]:
            alive
        else:
            break
