import sys,time,os
from random import randint
from datetime import datetime


def sprint(str): # print slowly function
    for c in str + '\n': 
        sys.stdout.write(c) # print 1 letter at a time
        sys.stdout.flush() # clear the print buffer
        time.sleep(0.01) # time delay

### print welcome message
sprint("Welcome adveturer to Journey to the Python Kingdom ")
sprint("The Python kingdom is a land of riches and dangers but thoes who succed will find sectrets beyond thier imagination")


### prompt user for choice
advname = input("What is your name adventurer? ")
print('I greet you, ' + advname +'.')
start = input('shall we begin(yes/no)?  ')
if start == 'yes':
    sprint('very well let us begin (NOTE PLEASE TYPE ANSWERS IN CAPS)')
    scene1= input('so ' + advname + ' where do you wish to begin a camp, in the FOREST or an Inn in a TOWN  ')
else:
    sprint('very well your adventure Ends bitterly GAME OVER!!!')
    quit()


if scene1 == 'FOREST':
    sprint ('You start your adventure in a camp in the forest')
    response = input('you look into your bag and see a APPLE(1) and BANNANA), which do you eat first?' )
    if response == 'APPLE':
        print('you eat the apple and you feel alot healther, but you realise it was a poisoned apple you fall dead.')
        quit()
    elif response == 'BANNANA':
        print('Your hunger has been sated and so you make ready to leave out of the forest.')
        
    else:
        print(' you ate nothing you starve to death, please eat somthing.')
        quit()

elif scene1 == 'TOWN':
    sprint ('You start your adventure in aN INN in on the main road') ###town
    response = input('the maid of the offers you two option wine or drink of WATER, Which do you pick?' )
    if response == 'WINE':
        print('you drink the wine but find that it was a bit too strong for you soo you get knock out drunk, when you come to you find that all your goods have been stolen YOUVE BEEN ROBBED GAME OVER.' )
        quit()
    elif response == 'WATER':
        print('The water quenches your thirst and you make ready to open the door to leave the inn.')
        
    else:
        print(' You get kicked out of the inn for you indecisiveness, Hurry up next time.')
        quit()

scene2 = input('open to you are two paths, to the NORTH lies the village of Talonberg and SOUTH(2) lines an extended road that could lead to anywhere which way do you go?.  ')  
if scene2 == 'SOUTH':
    print('you head south only to encounter a merchant with a broken carraige.') 
elif scene2 == 'NORTH':
    print('you head to Talonberg a nice river village, but you are suddenly attacked and cut down by bandits looks can be deciving maybe try another way.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene3 = input('The merchant:"good sire can you help me a group of goblins attacked me and took my satchals" will you HELP him or LEAVE him ')
if scene3 == 'HELP':
    print('you introduce yourself and offer to help the strained,the merchant elated says"thank you ' + advname + ' if you do this I am forver in you debt. remember these goblins are crafty and will try to trick you they left eastward I belive they have a cave there be careful and good luck.') 
elif scene3 == 'LEAVE':
    print('you decide not to help the merchant and go on your way, I guess you have more important things to do.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene3a = input('you enter the eastward forest and notice a forked path you, the LEFT path seems dark and downhill with a "danger" sign dangling on the tree, the RIGHT side seems equally trecherous and uphill with a sign saying "beware" which way do you go?')  
if scene3a == 'RIGHT':
    print('you cautously make your way up th hill, after what seems like an hour worth of walking you see the cave and with a deep breath you enter.') 
elif scene3a == 'LEFT':
    print('you walk downhill cautoulsy for about a minute until you feel a sharp pain in your neck and your legs begin to falter, you keep yourself upright as long as you can but you eventually come tumbling down the hill off a cliff to your death, but just before you fell you swear you heard a mischievous laugh.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene4 = input('you make your way through goblin cave using a conviniant torch to light your way, yet agian you see another fork path; on the LEFT you see a decayed sign saying treasure ahead and although you see no sign on the RIGHT path you see footprints leading deeper in which way do you go? ')  
if scene4 == 'RIGHT':
    print('beliving it is a trap you continue right untill you enter a cave opening revealing a large room full of goblins.') 
elif scene4 == 'LEFT':
    print('beliving that you can steal the treasure under the goblins you take the left path only to finnd a single treasure chest in a room, you about to open until but suddenly without warning the chest opens its mouth and with one chop eats you whole dead, you encounter a mimic.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene5 = input('the goblins mummur to one an othe deciding what to do with you, then an old goblin leader rose up and adress "greetings intruder you have succesfully passed our traps, for your reward will give you two options either you can FIGHT us or you solve the RIDDLE and we will give you what yous seek".  ')  
if scene5 == 'RIDDLE':
    print('you nod your head agree to the terms, the goblin leader smiling says "alright then lets begin".') 
elif scene5 == 'FIGHT':
    print('beliving that you can take them all on you pull your sword out dissapointed the goblin leader signals his horde upon you, you fight valiantly but rhe horde is too much and you fall dead. ')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene5a = input('the goblin leader clears his throat "what has a neck but no head?".  ')  
if scene5a == 'BOTTLE':
    print('"well done next".') 
else:
 print('"you choose poorly" the golbin leader say sending his green horde at you killing you in proccess.')
 quit()

scene5b = input('the goblin leader continues"what has a head but no brain?".  ')  
if scene5b == 'LETTUCE':
    print('"well done now for the final riddle".') 
else:
 print('"you choose poorly" the golbin leader say sending his green horde at you killing you in proccess.')
 quit()

scene5c = input('the goblin leader continues"What thrives when you feed it but dies when you water it?".  ')  
if scene5c == 'FIRE':
    print('"well done, you have solved all riddle here take our treasure from our last raid reward and dont comeback unless you want to solve more riddles" the goblin smiles.') 
else:
 print('"you choose poorly" the golbin leader say sending his green horde at you killing you in proccess.')
 quit()

scene6 = input('retracing you steps you make you way to the merchant who is hold up in an inn awaiting your return,"ah ' + advname + ' were you able to get my items?" YES OR NO')
if scene6 == 'NO':
    print('"nooo (sigh) now ill never return to my bussiness again." you leave the merchant to mourn his loss knowing full well you have his riches and you intend to enrich yourself with it. you have achived the GREED ENDING GAME OVER')
    quit()
elif scene6 == 'YES':
    print('"oh thank you ' + advname + ' you saved my bussiness as a reward how about i give 1000 gold for you deeds and if you need anything else look me up ill give you a discount" you leave the merchant in good terms and a warm feeling in heart knowing you did some good adventuring, you have achived the HEROIC ENDING GAME OVER')
    quit()
else:
 print('invalid please choose!.')
 quit()

 
### TOWN
scene2T = input('head out of the forest to the NORTH lies the village of Talonberg and SOUTH(2) lines an extended road that could lead to anywhere which way do you go?.  ')  
if scene2 == 'SOUTH':
    print('you head south only to encounter a merchant with a broken carraige.') 
elif scene2 == 'NORTH':
    print('you head to Talonberg a nice river village, but you are suddenly attacked and cut down by bandits looks can be deciving maybe try another way.')
    quit()
else:
 print('invalid please choose!.')
 quit()