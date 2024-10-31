### print welcome message
print("Welcome adveturer to Journey to the Python Kingdom ")
print("The Python kingdom is a land of riches and dangers but thoes who succed will find sectrets beyond thier imagination")


### prompt user for choice
print("What is your name" )
advname = input("> ")
print(f'I greet you {advname}')
start = input('shall we begin?')
if start == 'yes':
    print('very well let us begin')
    scene1= input('where do which to begin a camp in the forest or and Inn in a town?  ')
else:
    print('very well your adventure Ends bitterly')
    quit()
if scene1 == 'forest':
    print ('You start your adventure in a camp in the forest')
    response = input('you look into your bag and see a apple and bannana, which do you eat first?' )
    if response == 'apple':
        print('you eat the apple and you feel alot healther, but you realise it was a poisoned apple you fall dead.')
        quit()
    elif response == 'bannana':
        print('despite eating a fruit you dont feel to different.')
        
    else:
        print(' you ate nothing you starve to death, please eat somthing.')
        quit()

scene2 = input('head out of the forest to the north lies the village of Talonberg and south lines an extended road that could lead to anywhere which way do you go.  ')  
if scene2 == 'south':
    print('you head south only to encounter a merchant with a broken carraige.') 
elif scene2 == 'north':
    print('you head to Talonberg a nice river village, but you are suddenly attacked and cut down by bandits looks can be deciving maybe try another way.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene3 = input('The merchant:"good sire can you help me a group of goblins attacked me and took my satchals" will you help him or be on your way ')
if scene3 == 'help':
    print(f'you introduce yourself and offer to help the strained,the merchant elated says"thank you {advname} if you do this I am forver in you debt. remember these goblins are crafty and will try to trick you they left eastward I belive they have a cave there be careful and good luck.') 
elif scene3 == 'leave':
    print('you decide not to help the merchant and go on your way, I guess you have more important things to do.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene3a = input('you enter the eastward forest and notice a forked path you, the left path seems dark and downhill with a "danger" sign dangling on the tree, the right side seems equally trecherous and uphill with a sign saying "beware" which way do you go?')  
if scene3a == 'right':
    print('you cautously make your way up th hill, after what seems like an hour worth of walking you see the cave and with a deep breath you enter.') 
elif scene3a == 'left':
    print('you walk downhill cautoulsy for about a minute until you feel a sharp pain in your neck and your legs begin to falter, you keep yourself upright as long as you can but you eventually come tumbling down the hill off a cliff to your death, but just before you fell you swear you heard a mistifous laugh.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene4 = input('you make your way through goblin cave using a conviniant torch to light your way, yet agian you see another fork path; on the left you see a decayed sign saying treasure ahead and although you see no sign on the right path you see footprints leading deeper in which way do you go? ')  
if scene4 == 'right':
    print('beliving it is a trap you continue right untill you enter a cave opening revealing a large room full of goblins.') 
elif scene4 == 'left':
    print('beliving that you can steal the treasure under the goblins you take the left path only to finnd a single treasure chest in a room, you about to open until but suddenly without warning the chest opens its mouth and with one chop eats you whole dead, you encounter a mimic.')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene5 = input('the goblins mummur to one an othe deciding what to do with you, then an old goblin leader rose up and adress "greetings intruder you have succesfully passed our traps, for your reward will give you two options either you can fight us or you solve the riddle and we will give you what yous seek".  ')  
if scene5 == 'Riddle':
    print('you nod your head agree to the terms, the goblin leader smiling says "alright then lets begin".') 
elif scene5 == 'Fight':
    print('beliving that you can take them all on you pull your sword out dissapointed the goblin leader signals his horde upon you, you fight valiantly but rhe horde is too much and you fall dead. ')
    quit()
else:
 print('invalid please choose!.')
 quit()

scene5a = input('the goblin leader clears his throat "what has a neck but no head?".  ')  
if scene5a == 'bottle':
    print('"well done next".') 
else:
 print('"you choose poorly" the golbin leader say sending his green horde at you killing you in proccess.')
 quit()

scene5b = input('the goblin leader continues"what has a head but no brain?".  ')  
if scene5b == 'lettuce':
    print('"well done now for the final riddle".') 
else:
 print('"you choose poorly" the golbin leader say sending his green horde at you killing you in proccess.')
 quit()

scene5c = input('the goblin leader continues"What thrives when you feed it but dies when you water it?".  ')  
if scene5c == 'fire':
    print('"well done, you have solved all riddle here take our treasure from our last raid reward and dont comeback unless you want to solve more riddles" the goblin smiles.') 
else:
 print('"you choose poorly" the golbin leader say sending his green horde at you killing you in proccess.')
 quit()

scene6 = input(f'retracing you steps you make you way to the merchant who is hold up in an inn awaiting your return,"ah {advname} were you able to get my items?"')
if scene6 == 'no':
    print('"nooo (sight) now ill never return to my bussiness again." you leave the merchant to mourn his loss knowing full well you have his riches and you intend to enrich yourself with it. you have achived the GREED ENDING GAME OVER')
    quit()
elif scene6 == 'yes':
    print(f'"oh thank you {advname} you saved my bussiness as a reward how about i give 1000 gold for you deeds and if you need anything else look me up ill give you a discount" you leave the merchant in good terms and a warm feeling in heart knowing you did some good adventuring, you have achived the HEROIC ENDING GAME OVER')
    quit()
else:
 print('invalid please choose!.')
 quit()

 

