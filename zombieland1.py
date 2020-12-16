#Creating An Introduction
print("\nWELCOME to the Text Based Adventure Game-->Zombie Land")
print("\nYou are a brave fighter and protector of the magical lands of the Black Village")
print("\nI am Jojo the talking dog and I will guide you through the whole game ")
print("\nThis game will test your imagination. Keep noting down coordinates of traps, zombies, treasure chests or more.")
name=input("\nChoose a name that you want to be known by: ")
print("\nAll hail the brave knight",name)
#Explaining the Rules
movingon1=input("\nPress enter key to go on: ")
print("\nYou are at the centre of the village. The villagers have abandoned this village as it has been taken over by zombies.")
print("\nThe village spans 5 km in all directions. Imagine a 10 by 10 grid.")
print("\nYou are free to move 1 km at a time in one of the four directions: North, South, East, West.")
print("\nYou can move by typing: (w) to go North, (s) to go South, (d) to go East, (a) to go West.")
movingon2=input("\nPress enter key to go on: ")
print("\nYour aim is to light all the 5 torches in the village, as zombies burn when exposed to light.")
print("\nI would suggest you keep a notepad and pen and map out the village as we go...")
movingon3=input("\nPress enter key to go on: ")
print("\n\n\nLets start!!!!")
print("\n\n\nThe village elder has left you the following hints to locate the torches.")
print("\nFind torch1 at a position such that the x coordinate is 999 divided by infinty and the y coordinate is 999 divided by 333.")
print("\nFind torch2 at a position such that the x coordinate is same as the y coordinate of torch1 +1 and the y coordinate is unity.")
print("\nFind torch3 at a position such that x coordinate is 12345**0 and y corrdinate is the negative of the second prime number.")
print("\nFind torch4 at a position such that the x and y coordinate are the same and are the negative of the least odd prime number.")
print("\nFind torch5 at a position such that the x coordinate is the negative of square root of 16 and y coordinate is x coordinate -3 ")
t=0 #Torch counter
x=0 #X-coordinate counter
y=0 #Y-coordinate counter
s1=0 #Torch1 switch checker
s2=0 #Torch2 switch checker
s3=0 #Torch3 switch checker
s4=0 #Torch4 switch checker
s5=0 #Torch5 switch checker
def pos():
    print("You are at","(",x,",",y,")")
pos()
while t!=6:
    if t==5: #Condition for victory
        print("YOU HAVE WON, BRAVE KNIGHT",name,"!!!!!!")
        print("THE VILLAGERS THANK YOU ")
        exit()
    else:
        direction=str(input("Give direction: ")) #Giving direction inputs
        if(direction=="w"):
            y=y+1
        elif(direction=="s"):
            y=y-1
        elif(direction=="d"):
            x=x+1
        elif(direction=="a"):
            x=x-1
        else:
            print("INVALID DIRECTION INPUT")
            print("GAME OVER")
            exit()
        pos()
        if(x<-5 or x>5 or y<-5 or y>5):   #Creating Boundry of map
            print("You Abandoned The Village ")
            print("GAME OVER")
            exit()
        elif(x==0 and y==1): #Quicksand
            print("You fell into quicksand and died")
            print("GAME OVER")
            exit()
        elif x==-1 and y>-1: #Farm side one
            print("There is a farm ahead. You canot cross it because the cattle is running haywire")
            print("This is beacuse they are afraid of the zombie located at (-2,3)")
            print("Use your bow and arrow to kill the zombies.")
            arrowx=int(input("Which x coordinate do you want to shoot the arrow?: "))
            arrowy=int(input("Which y coordinate do you want to shoot the arrow?: "))
            if(arrowx==-2 and arrowy==3):
                print("You have crossed the farm and are at a gate located at (-4,0)")
                x=-4
                y=0
                pos()
            else:
                print("Your aim was bad and you were run over by the cattle.")
                print("GAME OVER")
                exit()
        elif(x==-3 and y>-1): #Farm side two
            print("There is a farm ahead. You canot cross it because the cattle is running haywire")
            print("This is beacuse they are afraid of the zombie located at (-2,1)")
            print("Use your bow and arrow to kill the zombies.")
            arrowx=int(input("Which x coordinate do you want to shoot the arrow?: "))
            arrowy=int(input("Which y coordinate do you want to shoot the arrow?: "))
            if(arrowx==-2 and arrowy==1):
                print("You have crossed the farm and are at a gate located at (0,4)")
                x=0
                y=4
                pos()
            else:
                print("Your aim was bad and you were run over by the cattle.")
                print("GAME OVER")
                exit()
        elif((x<=2 and y==-1) or (x<=2 and y==-2) or (x==2 and y>=-2) or (x==3 and y>=-2)): #Magical lake
            print("You have reched the bank of the magical lake ")
            print("Jump in to teleport to any location other than to the torches. ")
            lakex=int(input("x coordinate: "))
            lakey=int(input("y coordinate: "))
            if lakex==0 and lakey==3:
                print("You broke the rules!!!!!")
                print("GAME OVER")
                exit()
            elif lakex==4 and lakey==1:
                print("You broke the rules!!!!!")
                print("GAME OVER")
                exit()
            elif lakex==1 and lakey==-3:
                print("You broke the rules!!!!!")
                print("GAME OVER")
                exit()
            elif lakex==-3 and lakey==-3:
                print("You broke the rules!!!!!")
                print("GAME OVER")
                exit()
            elif lakex==-4 and lakey==1:
                print("You broke the rules!!!!!")
                print("GAME OVER")
                exit()
            else:
                x=lakex
                y=lakey
                pos()
        elif(x==1 and y==0): #Zombie
            print("There is a zombie in your way. Use your sword to kill it.")
            print("You can do so by typing the sum of the coordinates you are at.")
            sumofcoord=int(input("What is the sum: "))
            if sumofcoord==1:
                print("You have killed the zombie.")
            else:
                print("You have failed to kill the zombie. The zombie killed you")
                print("GAME OVER")
                exit()
        elif(x==0 and y==-3): #Spider
            print("You are stuck in a spider web")
            print("Answer the giant spider's question correctly to be free.")
            answerspider=int(input("Spider: What is the binary representation of 100?: "))
            if answerspider==1100100:
                print("Spider: Yes that is correct. You are free to go.")
            else:
                print("Spider: That is incorrect. I will now eat you.")
                print("GAME OVER")
                exit()
        elif(y==-4): #Valley
            print("You have fallen into a valley.")
            print("GAME OVER")
            exit()
        elif(x==0 and y==-5): #Goldenchest
            print("You have come across a golden chest.")
            print("If you wish to open it type open.")
            print("Otherwise type ignore.")
            goldchest=str(input("What would you like to do?: "))
            if goldchest=="open":
                print("Well done. You have found one switch to light all torches.")
                print("I have switched it on.")
                t=5
            else:
                print("You may go on.")
        elif(x==1 and y==4): #Blackbox1
            print("You see a black box.If you wish to open it type open.")
            print("Otherwise type ignore.")
            blackbox=str(input("What would you like to do?: "))
            if blackbox=="open":
                print("You have released all the demons of hell into the village.")
                print("GAME OVER")
                exit()
            else:
                print("You may go on.")
        elif(x==1 and y==2): #Blackbox2
            print("You see a black box.If you wish to open it type open.")
            print("Otherwise type ignore.")
            blackbox=str(input("What would you like to do?: "))
            if blackbox=="open":
                print("You have released all the demons of hell into the village.")
                print("GAME OVER")
                exit()
            else:
                print("You may go on.")
        elif(x==4 and y==3): #Zombie
            print("There is a zombie in your way. Use your sword to kill it.")
            print("You can do so by typing the sum of the coordinates you are at.")
            sumofcoord=int(input("What is the sum: "))
            if sumofcoord==7:
                print("You have killed the zombie.")
            else:
                print("You have failed to kill the zombie. The zombie killed you")
                print("GAME OVER")
                exit()
        elif(x==-4 and y==2): #Zombie
            print("There is a zombie in your way. Use your sword to kill it.")
            print("You can do so by typing the sum of the coordinates you are at.")
            sumofcoord=int(input("What is the sum: "))
            if sumofcoord==6:
                print("You have killed the zombie.")
            else:
                print("You have failed to kill the zombie. The zombie killed you")
                print("GAME OVER")
                exit()
        elif(x==4 and y==-2): #Spider
            print("You are stuck in a spider web")
            print("Answer the giant spider's question correctly to be free.")
            answerspider=int(input("Spider: how many legs do I have?: "))
            if answerspider==8:
                print("Spider: Yes that is correct. You are free to go.")
            else:
                print("Spider: That is incorrect. I will now eat you.")
                print("GAME OVER")
                exit()
        elif(x==0 and y==3): #Torches
            if s1==0:
                print("You have found torch1")
                t=t+1
                s1=1
            elif s1==1:
                print("You have already lighted torch1")
        elif(x==4 and y==1):
            if s2==0:
                print("You have found torch2")
                t=t+1
                s2=1
            elif s2==1:
                print("You have already lighted torch2")
        elif(x==1 and y==-3):
            if s3==0:
                print("You have found torch3")
                t=t+1
                s3=1
            elif s3==1:
                print("You have already lighted torch3")
        elif(x==-3 and y==-3):
            if s4==0:
                print("You have found torch4")
                t=t+1
                s4=1
            elif s4==1:
                print("You have already lighted torch4")
        elif(x==-4 and y==1):
            if s5==0:
                print("You have found torch5")
                t=t+1
                s5=1
            elif s5==1:
                print("You have already lighted torch5")
