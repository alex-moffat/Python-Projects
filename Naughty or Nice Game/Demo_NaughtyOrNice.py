# Python: 3.8.2
# Author: Alex Moffat
# Purpose: A game that shows off basic programming skills

#===== IMPORTED MODULES
import random

#===== GLOBAL VARIABLES 
scenes, name, yes, nope = [], "", 0, 0
print(name)

#===== SET SCENES : creates a list of 5 scenarios (tuples) of stranger interactions  - Sets messages for scenario, question, nope response, yes response
def setScenes():
    global scenes
    scenes = [ 
    ('A smelly stranger approaches you and says hello.', 'Do you say hello?', 'The stranger glares at you and storms off...', 'The stranger smiles and says you made his day...'), 
    ('You are in a hurry and an old man approaches and asks for directions.', 'Do you stop to give him directions?', 'The old man seems confused as you walk away...', 'The old man thanks you for your time...'),
    ('An old woman with a walker is crossing very slowly across a busy street.', 'Do you help her across the street?', 'The old women falls down at the curb on the other side...', 'The old women says you are very kind...'),
    ('A stranger wants to have a conversation about the weather.', 'Do you have a conversation about the weather?', 'The stranger mutters something about having no friends and walks away...', 'You find out the stranger lives in your home town and knows your mother...'),
    ('You are in a rush to get to work and a stranger asks for the time.', 'Do you stop to give the time?', 'The stranger yells that you are mean as you are running away...', 'The stranger says have a great day and enjoy the sunshine...')]

#===== START GAME : Check if played before --> start game
def startGame():
    print("\nThank you for playing again {}!".format(name)) if name != "" else getName()
    setScenes()
    naughtyNice()

#===== GET NAME : Get players name for global variable 'name', reset yes and nope scores to zero
def getName():
    global name, yes, nope
    go = True
    while go:
        name = input('What is your name? \n>>> ').capitalize()
        if name == "":
            print('You need to provide a name!')
        else:
            print("\nWelcome {}".format(name))
            print('\nIn this game you will be greeted by several different people.')
            print('You can choose to be naughty or nice, but at the end of the game your fate will be sealed by your actions.')
            yes, nope, go = 0, 0, False

#===== NAUGHTYNICE - Check if valid answer then score 1 yes/nope
def naughtyNice():
    global scenes, yes, nope
    go = True
    rStranger = random.sample(scenes,1)[0] #pull a random scene tuple from strangers list
    scenes.remove(rStranger) # remove current scene so we don't repeat
    while go:
        pick = input('\n{scene} \n{question} (Y/N): \n>>> '.format(scene = rStranger[0], question = rStranger[1])).upper()
        if pick == "": # check if left blank
            print('You need to provide an answer\n>>> ')
        elif pick != "Y" and pick != "N": # check if valid answer
            print('You need to answer with \"Y\" (be nice) or \"N\" (be naughty)')            
        else: # valid answer - give message and score
            go = False
            if pick == 'N':
                print("\n{N}".format(N = rStranger[2]))
                nope += 1
            else:
                print("\n{Y}".format(Y = rStranger[3]))
                yes += 1
    print("\n{player}, your current total: \n({naughty} Naughty) and ({nice} Nice)".format(player = name, naughty = nope, nice = yes))
    checkScore()

#===== SCORE - when player has answered YES or nope 3 times - win/lose condition is met - otherwise continue game
def checkScore(): 
    if yes > 2: # WIN - Nice condition
        print("\nNice job {}, you win! \nYou are nice and Santa will bring you lots of presents this year. \nEveryone loves you and you've made lots of friends along the way!".format(name))
    elif nope > 2: # LOSE - Naughty condition
        print("\nToo bad {}, game over! \nYou are naughty and Santa is not bringing you any presents this year. \nKeep it up and you will live alone with no friends to call your own!".format(name))
    else:
        naughtyNice()
    again()

#===== AGAIN - ask if play again - terminate game or reset variables and start again 
def again():
     go = True
     while go:
         choice = input('\nDo you want to play again? (Y/N): \n>>> ').upper()
         if choice == 'Y':
             go = False
             startGame()
         elif choice == 'N':
             go = False            
             print("\nOh, so sad, sorry to see you go!")
             quit()
         else:
             print("\nEnter (Y) for 'Yes' or (N) for 'No':\n>>> ")


if __name__ == '__main__':
    startGame()
