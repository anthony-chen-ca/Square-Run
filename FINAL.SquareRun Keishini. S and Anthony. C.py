# Square Run.py
# Keishini Selvaganesh and Anthony Chen
# June 13 2018
# Final programming project!

#----------------------------------------------------------------------------------------------------
#TABLE OF CONTENTS
#----------------------------------------------------------------------------------------------------
# - INITIALIZATION      - 
# - COLOURS             - 
# - TEXTS               - 
# - MAIN MENU           - 
# - CLASSES             - 
# - PLAYER SELECTION    - 
# - LEVEL SELECTION     - 
# - PAUSE MENU          - 
# - GAME OVER           - 
# - GAMEPLAY            - 
# - MAIN PROGRAM        - 

#----------------------------------------------------------------------------------------------------
#INITIALIZATION
#----------------------------------------------------------------------------------------------------
import pygame, sys
import math
import random
from random import randint
pygame.init()
pygame.font.init()
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CENTREX = WIDTH/2
CENTREY = HEIGHT/2
#font initialization
title = pygame.font.Font('Fonts/Barrio-Regular.ttf', 80)
heading = pygame.font.Font('Fonts/Barrio-Regular.ttf', 40)
headingTwo = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 50)
body = pygame.font.Font('Fonts/OpenSans-Regular.ttf', 25)

#----------------------------------------------------------------------------------------------------
#COLOURS
#----------------------------------------------------------------------------------------------------
#Here are some cool colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 36, 125)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 86)
PURPLE = (114, 16, 223)
DARKPURPLE = (85, 26, 139)
GOLD = (255, 215, 0)
#Level Colours
# - Shelter
OLIVEGREEN = (135, 194, 138)
PASTELBLUE = (60, 126, 186)
# - Fireflies
NAVYBLUE = (5, 0, 54)
# - No Money
FADEDTEAL = (124, 179, 150)
SAND = (199, 128, 76)
ORCHID = (96, 19, 51)
# - Pay No Mind
DEEPPINK = (163, 73, 73)
# - Jackpot
SLATE = (44, 44, 60)
ORANGE = (196, 112, 54)
# - Echolands
OCEANBLUE = (25, 17, 72)
HEAVENWHITE = (234, 247, 254)
# - Me and You
PINK = 	(203, 105, 99)
LIGHTPINK = (241, 178, 165)
# - Elevatia
DEEPPURPLE = (101, 34, 87)
MINTGREEN = (114, 204, 132)
# - Crave you
LIGHTBLUE = (75, 202, 216)
# - The Seven Seas
BROWN = (78, 25, 5)

#----------------------------------------------------------------------------------------------------
#TEXTS
#----------------------------------------------------------------------------------------------------
#"Square Run"
titleText = title.render("Square Run", True, WHITE, PURPLE)
titleWidth = titleText.get_rect().width
titleHeight = titleText.get_rect().height

#"Exit"
exitText = heading.render("Exit", True, WHITE, PURPLE)
exitWidth = exitText.get_rect().width
exitHeight = exitText.get_rect().height

#"Pause"
pauseText = heading.render("Paused", True, WHITE, RED)
pauseWidth = pauseText.get_rect().width
pauseHeight = pauseText.get_rect().height

#"Game Over"
gameText = title.render("Game Over", True, WHITE, PURPLE)
gameWidth = gameText.get_rect().width
gameHeight = gameText.get_rect().height

#"Congratulations!"
winText = title.render("Congratulations!", True, WHITE, GOLD)
winWidth = winText.get_rect().width
winHeight = winText.get_rect().height

#"Credits"
creditsText = heading.render("Credits", True, WHITE, PURPLE)
creditsWidth = creditsText.get_rect().width
creditsHeight = creditsText.get_rect().height

#"Instructions"
instructionsText = heading.render("Instructions", True, WHITE, PURPLE)
instructionsWidth = instructionsText.get_rect().width
instructionsHeight = instructionsText.get_rect().height

#"Achievements"
achievementsText = heading.render("Achievements", True, WHITE, PURPLE)
achievementsWidth = achievementsText.get_rect().width
achievementsHeight = achievementsText.get_rect().height

#"Options"
optionsText = heading.render("Options", True, WHITE, PURPLE)
optionsWidth = optionsText.get_rect().width
optionsHeight = optionsText.get_rect().height

#"Options" Title
optionsTitleText = title.render("Options", True, WHITE, PURPLE)
optionsTitleWidth = optionsTitleText.get_rect().width
optionsTitleHeight = optionsTitleText.get_rect().height

#"How many players?"
howManyPlayersText = title.render("How many players?", True, WHITE, PURPLE)
howManyPlayersWidth = howManyPlayersText.get_rect().width
howManyPlayersHeight = howManyPlayersText.get_rect().height

#"1"
oneText = title.render("1", True, WHITE, DARKPURPLE)
oneWidth = oneText.get_rect().width
oneHeight = oneText.get_rect().height

#"2"
twoText = title.render("2", True, WHITE, DARKPURPLE)
twoWidth = twoText.get_rect().width
twoHeight = twoText.get_rect().height

#"Player One"
playerOneText = headingTwo.render("Player One", True, WHITE, PURPLE)
playerOneWidth = playerOneText.get_rect().width
playerOneHeight = playerOneText.get_rect().height

#"Player One" Gold
playerOneGoldText = headingTwo.render("Player One", True, WHITE, GOLD)
playerOneGoldWidth = playerOneGoldText.get_rect().width
playerOneGoldHeight = playerOneGoldText.get_rect().height

#"Player Two"
playerTwoText = headingTwo.render("Player Two", True, WHITE, PURPLE)
playerTwoWidth = playerTwoText.get_rect().width
playerTwoHeight = playerTwoText.get_rect().height

#"Player Two" Gold
playerTwoGoldText = headingTwo.render("Player Two", True, WHITE, GOLD)
playerTwoGoldWidth = playerTwoGoldText.get_rect().width
playerTwoGoldHeight = playerTwoGoldText.get_rect().height

#"Player One Selection"
playerOneSelectText = body.render("Player 1", True, WHITE, DARKPURPLE)
playerOneSelectWidth = playerOneSelectText.get_rect().width
playerOneSelectHeight = playerOneSelectText.get_rect().height

#"Player Two Selection"
playerTwoSelectText = body.render("Player 2", True, WHITE, DARKPURPLE)
playerTwoSelectWidth = playerTwoSelectText.get_rect().width
playerTwoSelectHeight = playerTwoSelectText.get_rect().height

#"SPACE to change icons"
playerOneControlText = body.render("Press SPACE to change icons", True, WHITE, PURPLE)
playerOneControlWidth = playerOneControlText.get_rect().width
playerOneControlHeight = playerOneControlText.get_rect().height

#"UP to change icons"
playerTwoControlText = body.render("Press UP to change icons", True, WHITE, PURPLE)
playerTwoControlWidth = playerTwoControlText.get_rect().width
playerTwoControlHeight = playerTwoControlText.get_rect().height

#"Back"
backWidth = 90
backHeight = 46
def back(colour):
    backText = heading.render("Back", True, WHITE, colour)
    screen.blit(backText, (30, 620))

#----------------------------------------------------------------------------------------------------
#MAIN MENU
#----------------------------------------------------------------------------------------------------
#main menu layout
def layout(circleColour):
    #layout design
    screen.fill(PURPLE)
    screen.blit(titleText, (CENTREX - titleWidth/2, CENTREY - titleHeight/2 - 220))
    screen.blit(exitText, (WIDTH-exitWidth-25, 10))

    #instructions
    screen.blit(instructionsText, (WIDTH-instructionsWidth-25, 480))
    #options
    screen.blit(optionsText, (WIDTH-optionsWidth-25, 550))
    #credits
    screen.blit(creditsText, (WIDTH-creditsWidth-25, 620))

    #play button
    circle = pygame.draw.circle(screen, circleColour, (CENTREX, CENTREY+25), 150)
    triangle = pygame.draw.polygon(screen, PURPLE, ((CENTREX-50, CENTREY-70+25), (CENTREX-50, CENTREY+70+25), (CENTREX+80, CENTREY+25)))
    pygame.display.update()

#end of def of the standard layout design
    
#game instructions
def instructions():
    instructions = True

    #texts
    instructionsText = heading.render("Instructions", True, WHITE, PURPLE)
    spaceText = body.render("1. Space Key: Player 1 uses this key to move up." , True, WHITE, PURPLE)
    arrowText = body.render("2. Up Key: Player 2 uses this key to move up." , True, WHITE, PURPLE)
    escText = body.render("3. Escape Key: Pause the game." , True, WHITE, PURPLE)
    rText = body.render("4. R Key: Restart the game when game is over/paused." , True, WHITE, PURPLE)
    qText = body.render("5. Q Key: Quit the game when game is over/paused." , True, WHITE, PURPLE)

    #images
    spaceKey = pygame.image.load('Images/Instructions/Space.png').convert_alpha()
    spaceKey = pygame.transform.scale(spaceKey, (120, 100))
    arrow = pygame.image.load('Images/Instructions/Arrow-Keys.png').convert_alpha()
    arrow = pygame.transform.scale(arrow, (100, 100))
    escKey = pygame.image.load('Images/Instructions/Escape.png').convert_alpha()
    escKey = pygame.transform.scale(escKey, (100, 100))
    rKey = pygame.image.load('Images/Instructions/R.png').convert_alpha()
    rKey = pygame.transform.scale(rKey, (100, 100))
    qKey = pygame.image.load('Images/Instructions/Q.png').convert_alpha()
    qKey = pygame.transform.scale(qKey, (100, 100))

    while instructions == True:
        #draw
        screen.fill(PURPLE)
        
        #Here are the instructions
        #title
        screen.blit(instructionsText, (CENTREY, 20))
        #space bar key
        screen.blit(spaceKey, (30, 100))
        screen.blit(spaceText, (200, 100))
        #arrows keys
        screen.blit(arrow, (30, 200))
        screen.blit(arrowText, (200, 200))
        #esc key
        screen.blit(escKey, (30, 300))
        screen.blit(escText, (200, 300))
        #r key
        screen.blit(rKey, (30, 400))
        screen.blit(rText, (200, 400))
        #q key
        screen.blit(qKey, (30, 500))
        screen.blit(qText, (200, 500))

        #back button
        back(PURPLE)

        #update
        pygame.display.update()
        
        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        #click buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                instructions = False
                mainmenu(False)
        #end of while loop (displaying the instructions screen)
#end of defining variables that are displayed on the instructions screen.
                
#options menu
def options():
    #variables
    global deathNumber
    global autoRetry
    options = True
    resetCounter = 0

    #"Change Death Effect"
    optionsOneText = body.render("Change Death Effect:", True, WHITE, PURPLE)
    optionsOneWidth = optionsOneText.get_rect().width
    optionsOneHeight = optionsOneText.get_rect().height

    #"Auto-Retry"
    autoText = body.render("Auto-Retry:", True, WHITE, PURPLE)
    autoWidth = autoText.get_rect().width
    autoHeight = autoText.get_rect().height

    #"Reset Data"
    resetText = body.render("Reset Data", True, WHITE, RED)
    resetWidth = resetText.get_rect().width
    resetHeight = resetText.get_rect().height

    #"Data Deleted!"
    deleteText = body.render("Data Deleted!", True, WHITE, RED)
    deleteWidth = deleteText.get_rect().width
    deleteHeight = deleteText.get_rect().height

    global checkmark

    deathList = ["Explosion", "Pelo Scream", "Wilhelm Scream", "Oof"]

    while options == True:
        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        #draw
        screen.fill(PURPLE)
        screen.blit(optionsTitleText, (CENTREX-optionsTitleWidth/2, CENTREY-optionsTitleHeight/2-200))

        #change death effect
        screen.blit(optionsOneText, (CENTREX-optionsOneWidth/2-100, CENTREY-optionsOneHeight/2))
        deathText = body.render(deathList[deathNumber], True, WHITE, DARKPURPLE)
        deathWidth = deathText.get_rect().width
        deathHeight = deathText.get_rect().height
        deathX = CENTREX-deathWidth/2+150
        deathY = CENTREY-deathHeight/2
        pygame.draw.rect(screen, DARKPURPLE, (deathX-10, deathY-10, deathWidth+20, deathHeight+20))
        screen.blit(deathText, (deathX, deathY))

        #auto-retry
        screen.blit(autoText, (CENTREX-optionsOneWidth/2-100, CENTREY-optionsOneHeight/2+80))
        autoX = CENTREX-autoWidth/2+175
        autoY = CENTREY-optionsOneHeight/2+80-10
        pygame.draw.rect(screen, DARKPURPLE, (autoX, autoY, 60, 60))
        if autoRetry == True:
            screen.blit(checkmark, (autoX, autoY))

        #reset data
        if resetCounter == 0:
            resetX = CENTREX-resetWidth/2
            resetY = CENTREY-resetHeight/2+220
            pygame.draw.rect(screen, RED, (resetX-10, resetY-10, resetWidth+20, resetHeight+20))
            screen.blit(resetText, (resetX, resetY))
        else:
            deleteX = CENTREX-deleteWidth/2
            deleteY = CENTREY-deleteHeight/2+220
            pygame.draw.rect(screen, RED, (deleteX-10, deleteY-10, deleteWidth+20, deleteHeight+20))
            screen.blit(deleteText, (deleteX, deleteY))
            resetCounter -= 1
            
        #end of while loop (draw, changing the death effect, auto-retry, and reseting data)   
        #end of if statement (reseting data)
#end defining variables (changing the death effect, auto-retry, deleting data, and reseting data
            
        #back button
        back(PURPLE)
        
        #update
        pygame.display.update()

        #click buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #back
                if (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                    options = False
                    mainmenu(False)

                #change death effect
                elif (deathX-10 < x < deathX+deathWidth+20) and (deathY-10 < y < deathY+deathHeight+20):
                    deathNumber = (deathNumber + 1)%4
                    if deathNumber == 0:
                        deathSample = pygame.mixer.Sound('Music/Death.wav')
                    elif deathNumber == 1:
                        deathSample = pygame.mixer.Sound('Music/Pelo.wav')
                    elif deathNumber == 2:
                        deathSample = pygame.mixer.Sound('Music/Wilhelm.wav')
                    elif deathNumber == 3:
                        deathSample = pygame.mixer.Sound('Music/Oof.wav')
                    deathSample.play()
                #end of if statements for each death effect
                    
                #auto-retry
                elif (autoX < x < autoX+60) and (autoY < y < autoY+60):
                    if autoRetry == True:
                        autoRetry = False
                    else:
                        autoRetry = True
                #if statement for making the auto-retry function
                #data deleted
                elif (resetX-10 < x < resetX+20+resetWidth) and (resetY-10 < y < resetY+20+resetHeight):
                    scoreFile = open(scoreFileName, 'w+')
                    scoreFile.write('0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0')
                    scoreFile.close()
                    global highScoreList
                    highScoreList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                    resetCounter = 1000
                #end of if statement for deleting data

#cool credits
def credits():
    credits = True
    #music
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Music/Credits.mp3')
    pygame.mixer.music.play()

    #image
    creditsImage = pygame.image.load("Images/Credits.png").convert_alpha()
    creditsImage = pygame.transform.scale(creditsImage, (4000, 600))

    #variables
    creditsClock = pygame.time.Clock()
    creditsFPS = 120
    creditsImageX = 0

    while credits == True:
        #draw
        screen.fill(BLACK)

        #credits image
        scroll = creditsImageX % creditsImage.get_rect().width
        screen.blit(creditsImage, (scroll - creditsImage.get_rect().width, 0))
        if scroll < WIDTH:
            screen.blit(creditsImage, (scroll, 0))
        creditsImageX -= 1
        pygame.draw.line(screen, (255, 255, 255), (scroll, 0), (scroll, HEIGHT), 3)

        #back
        back(BLACK)

        #update
        pygame.display.update()
        creditsClock.tick(creditsFPS)

        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        #click buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                credits = False
                mainmenu(True)
        #end of while liip for credits
#end of defining the credits screen
                
#random menu music
def menuMusic():
    randomMenuMusic = randint(1,2)
    if randomMenuMusic == 1:
        pygame.mixer.music.load('Music/Beautiful-Lie.mp3')
    else:
        pygame.mixer.music.load('Music/Mii.mp3')
    pygame.mixer.music.play(-1)
#defining the menu's music
    
#main menu
def mainmenu(new):
    layout(WHITE)

    #variables
    menu = True
    instructionsX = WIDTH-instructionsWidth-25
    instructionsY = 480
    optionsX = WIDTH-optionsWidth-25
    optionsY = 550
    creditsX = WIDTH-creditsWidth-25
    creditsY = 620

    #music
    if new == True:
        menuMusic()

    #main while loop
    while True:
        #main menu
        while menu == True:
            #get mouse position
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            sqx = (x - CENTREX)**2
            sqy = (y - CENTREY-25)**2

            #highlight buttons
            if math.sqrt(sqx + sqy) < 150:
                layout(GREY)
            else:
                layout(WHITE)

            #click buttons
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #exit
                    if (WIDTH-exitWidth-25 < x < WIDTH-exitWidth-25+exitWidth) and (10 < y < 10+exitHeight):
                        pygame.quit();
                        sys.exit();

                    #instructions
                    if (instructionsX < x < instructionsX+instructionsWidth) and (instructionsY < y < instructionsY+instructionsHeight):
                        menu = False
                        instructions()

                    #options
                    if (optionsX < x < optionsX+optionsWidth) and (optionsY < y < optionsY+optionsHeight):
                        menu = False
                        options()

                    #credits
                    if (creditsX < x < creditsX+creditsWidth) and (creditsY < y < creditsY+creditsHeight):
                        menu = False
                        credits()

                    #play
                    elif math.sqrt(sqx + sqy) < 150:
                        menu = False
                        numPlayerMenu()
#defining mainmenu functions
#end of while loop (clicking and hovering buttons)
                        
#----------------------------------------------------------------------------------------------------
#CLASSES
#----------------------------------------------------------------------------------------------------
#icons
class Icon():
    def __init__(self):
        self.image = pygame.image.load("Images/Red.png").convert_alpha()
        self.x = 150
        self.y = 530
        self.w = 70
        self.h = 70
#defining the player's icon (in the clas "Icon")
        
    #update the icon on-screen
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    #Defining (drawing the icon on the screen)
        
    #move up
    def shipUp(self, shipSpeed):
        if self.y > 0:
            self.y -= shipSpeed
        if self.y <= 0:
            self.y = 0
    #defining function for the icon to go up
            
    #fall down
    def gravity(self, gravitySpeed):
        if self.y < 530:
            self.y += gravitySpeed
    #defining function for the icon to go down

#hazards
class Hazard():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 50
        self.h = 50
#defining the hazards
        
    #update the hazard on-screen
    def draw(self, colour):
        pygame.draw.rect(screen, colour, (self.x, self.y, self.w, self.h))
    #defining (drawing the hazards on the screen)
        
    #check for collisions
    def checkCollision(self, iconX, iconY, iconW, iconH):
        if (iconX + iconW > self.x) and (iconX < self.x + self.w) and (iconY + iconH > self.y) and (iconY < self.y + self.h):
            return True
        else:
            return False
    #defining (if the icon crashes with the hazards)
        
#----------------------------------------------------------------------------------------------------
#PLAYER SELECTION
#----------------------------------------------------------------------------------------------------
def numPlayerMenu():
    global numPlayers
    numPlayerMenu = True
#defining the number of players
    
    while numPlayerMenu == True:
        #draw
        screen.fill(PURPLE)
        screen.blit(howManyPlayersText, (CENTREX-howManyPlayersWidth/2, CENTREY-howManyPlayersHeight/2-150))
        pygame.draw.rect(screen, DARKPURPLE, (CENTREX-50-100, CENTREY-50, 100, 100))
        pygame.draw.rect(screen, DARKPURPLE, (CENTREX-50+100, CENTREY-50, 100, 100))
        screen.blit(oneText, (CENTREX-oneWidth/2-100, CENTREY-oneHeight/2))
        screen.blit(twoText, (CENTREX-twoWidth/2+100, CENTREY-twoHeight/2))
        back(PURPLE)
    #end of while loop for the number of players
        
        pygame.display.update()

        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #one player
                if (CENTREX-50-100 < x < CENTREX-50) and (CENTREY-50 < y < CENTREY+50):
                    numPlayerMenu = False
                    numPlayers = 1
                    playerSelection()
                #two players
                elif (CENTREX-50+100 < x < CENTREX-50+200) and (CENTREY-50 < y < CENTREY+50):
                    numPlayerMenu = False
                    numPlayers = 2
                    playerSelection()
                #back
                elif event.type == pygame.MOUSEBUTTONDOWN and (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                    numPlayerMenu = False
                    mainmenu(False)
        #clicking the options for number of players
                    
def playerSelection():
    #variables
    characterOne = 1
    characterTwo = 2
    playerMenu = True
    avatarList = ["Red", "Blue", "Yellow", "Green", "Purple", "Baymax"]
    
    #defining the characters and the avatar list
    
    while playerMenu == True:
        #draw
        screen.fill(PURPLE)  
        #rect
        pygame.draw.rect(screen, DARKPURPLE, (CENTREX-150/2-200, CENTREY-50/2-150, 150, 50))
        #"Player 1"
        screen.blit(playerOneSelectText, (CENTREX-playerOneSelectWidth/2-200, CENTREY-playerOneSelectHeight/2-150))
        #avatar
        iconOne = pygame.image.load("Images/"+avatarList[characterOne]+".png").convert_alpha()
        iconOneLarge = pygame.transform.scale(iconOne, (150, 150))
        screen.blit(iconOneLarge, (CENTREX-150/2-200, CENTREY-150/2+150-150))
        #name
        iconText = body.render(avatarList[characterOne], True, WHITE, DARKPURPLE)
        iconWidth = iconText.get_rect().width
        iconHeight = iconText.get_rect().height
        pygame.draw.rect(screen, DARKPURPLE, (CENTREX-iconWidth-200, CENTREY-iconHeight+150, iconWidth*2, iconHeight*2))
        screen.blit(iconText, (CENTREX-iconWidth/2-200, CENTREY-iconHeight/2+150))
        #control
        screen.blit(playerOneControlText, (CENTREX-playerOneControlWidth/2-200, CENTREY-playerOneControlHeight/2-220))
        
        #back
        back(PURPLE)
    #while loop for the screen for player menu
        
        if numPlayers == 2:
            #rect
            pygame.draw.rect(screen, DARKPURPLE, (CENTREX-150/2+200, CENTREY-50/2-150, 150, 50), 0)
            #"Player 2"
            screen.blit(playerTwoSelectText, (CENTREX-playerTwoSelectWidth/2+200, CENTREY-playerTwoSelectHeight/2-150))
            #avatar
            iconTwo = pygame.image.load("Images/"+avatarList[characterTwo]+".png").convert_alpha()
            iconTwoLarge = pygame.transform.scale(iconTwo, (150, 150))
            screen.blit(iconTwoLarge, (CENTREX-150/2+200, CENTREY-150/2+150-150))
            #name
            iconTwoText = body.render(avatarList[characterTwo], True, WHITE, DARKPURPLE)
            iconTwoWidth = iconTwoText.get_rect().width
            iconTwoHeight = iconTwoText.get_rect().height
            pygame.draw.rect(screen, DARKPURPLE, (CENTREX-iconTwoWidth+200, CENTREY-iconTwoHeight+150, iconTwoWidth*2, iconTwoHeight*2))
            screen.blit(iconTwoText, (CENTREX-iconTwoWidth/2+200, CENTREY-iconTwoHeight/2+150))
            #control
            screen.blit(playerTwoControlText, (CENTREX-playerTwoControlWidth/2+200, CENTREY-playerTwoControlHeight/2-220))
    #if 2 players are chosen, a different screen will display
            
        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        sqx = (x - CENTREX)**2
        sqy = (y - CENTREY-50 + 100)**2

        #highlight buttons
        if math.sqrt(sqx + sqy) < 50:
            #circle
            circle = pygame.draw.circle(screen, GREY, (CENTREX, CENTREY-50), 50)
            #triangle
            pygame.draw.polygon(screen, PURPLE, ((475 + 350 - 347, 325 - 30 + 5), (480 + 300 - 347, 300 - 30 + 5), (480 + 300 - 347, 350 - 30 + 5)), 0)
        else:
            #circle
            circle = pygame.draw.circle(screen, WHITE, (CENTREX, CENTREY-50), 50)
            #triangle
            pygame.draw.polygon(screen, PURPLE, ((475 + 350 - 347, 325 - 30 + 5), (480 + 300 - 347, 300 - 30 + 5), (480 + 300 - 347, 350 - 30 + 5)), 0)
        #Highlighting buttons when hovering over
            
        pygame.display.update()
        
        #click buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #level selection
                if math.sqrt(sqx + sqy) < 50:
                    global icon
                    icon = Icon()
                    icon.image = iconOne

                    if numPlayers == 2:
                        global icon2
                        icon2 = Icon()
                        icon2.image = iconTwo
                        
                    playerMenu = False
                    levelSelection()

                #back
                elif (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                    playerMenu = False
                    numPlayerMenu()

            #switch character
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                characterOne = (characterOne+1)%6
                if characterOne == characterTwo and numPlayers == 2:
                    characterOne = (characterOne+1)%6

            #switch character
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                characterTwo = (characterTwo+1)%6
                if characterTwo == characterOne:
                    characterTwo = (characterTwo+1)%6
        #if statements for clicking buttons, back button, and switching characters.
                    
#----------------------------------------------------------------------------------------------------
#LEVEL SELECTION
#----------------------------------------------------------------------------------------------------
def loadLevel(levelNumber):
    #level(music, number of hazards, size of hazards, length of level, hazard speed, icon speed,
        #screen colour, ground colour, hazard colour, finish line colour
    if levelNumber == 0:
        level('Candyland', 20, 50, 5000, 1, 5,
              PURPLE, PURPLE, PURPLE, PURPLE)
    elif levelNumber == 1:
        level('Shelter', 25, 60, 7000, 1, 5,
              PASTELBLUE, OLIVEGREEN, PASTELBLUE, PASTELBLUE)
    elif levelNumber == 2:
        level('Fireflies', 50, 20, 8000, 2, 5,
              NAVYBLUE, NAVYBLUE, WHITE, NAVYBLUE)
    elif levelNumber == 3:
        level('No-Money', 50, 50, 8000, 3, 7,
              FADEDTEAL, SAND, ORCHID, ORCHID)
    elif levelNumber == 4:
        level('Pay-No-Mind', 60, 50, 8000, 3, 7,
              DEEPPINK, DEEPPINK, PINK, DEEPPINK)
    elif levelNumber == 5:
        level('Jackpot', 50, 80, 8000, 3, 7,
              SLATE, SLATE, ORANGE, SLATE)
    elif levelNumber == 6:
        level('Echolands', 70, 60, 8000, 4, 8,
              OCEANBLUE, OCEANBLUE, HEAVENWHITE, PURPLE)
    elif levelNumber == 7:
        level('me-and-you', 90, 60, 8000, 4, 8,
              WHITE, PINK, LIGHTPINK, PINK)
    elif levelNumber == 8:
        level('Idols', 110, 40, 8000, 5, 9,
              BLACK, BLACK, GREEN, GREEN)
    elif levelNumber == 9:
        level('Elevatia', 120, 45, 8000, 5, 9,
              DEEPPURPLE, MINTGREEN, MINTGREEN, MINTGREEN)
    elif levelNumber == 10:
        level('One-Off-Mind', 100, 60, 8000, 5, 9,
              BLACK, BLACK, WHITE, WHITE)
    elif levelNumber == 11:
        level('Crave-You', 140, 40, 8000, 6, 11,
              BLACK, LIGHTBLUE, LIGHTBLUE, LIGHTBLUE)
    elif levelNumber == 12:
        level('Challenger', 70, 25, 8000, 8, 14,
              BLACK, RED, RED, RED)
    elif levelNumber == 13:
        level('The-Seven-Seas', 190, 55, 8000, 6, 11,
              BROWN, BROWN, YELLOW, BROWN)
    elif levelNumber == 14:
        level('Screamroom', 200, 50, 8000, 6, 12,
              BLACK, BLACK, GREY, GREY)
#defininf the levels and the differences with their difficulty.
        
#achievements menu
def achievements():
    #variables
    achievementMenu = True
    page = 0

    #"Achievements" Title
    achievementsTitleText = title.render("Achievements", True, WHITE, PURPLE)
    achievementsTitleWidth = achievementsTitleText.get_rect().width
    achievementsTitleHeight = achievementsTitleText.get_rect().height

    #"Page" Texts
    pageOne = heading.render("Page 1", True, WHITE, PURPLE)
    pageTwo = heading.render("Page 2", True, WHITE, PURPLE)

    #achievement list
    achievementList = ["Sugar Sweet", "Even When I'm Gone", "A Thousand Hugs",
                       "Not This Time", "She Was Dancing", "Millionaire",
                       "Otherworldly", "Me and You Together", "2012 Nostalgia",
                       "Elevated", "One-Sided Game", "Dripping in Gold",
                       "Flying into Space", "You are a Pirate", "Don't Breathe"]

#defining schievement menu
    
    def achievementBox(achievementX, achievementY, numAchievement):
        global checkmark
        #rect
        pygame.draw.rect(screen, DARKPURPLE, (achievementX, achievementY, 350, 80))
        #white box
        pygame.draw.rect(screen, WHITE, (achievementX+10, achievementY+10, 60, 60))
        #text
        achievementBoxText = body.render(achievementList[numAchievement], True, WHITE, DARKPURPLE)
        achievementBoxWidth = achievementBoxText.get_rect().width
        achievementBoxHeight = achievementBoxText.get_rect().height
        screen.blit(achievementBoxText, (achievementX+20+60, achievementY-achievementBoxHeight/2+40))
        #checkmark
        if highScoreList[numAchievement] == 100:
            screen.blit(checkmark, (achievementX+10, achievementY+10))

    while achievementMenu == True:
        #draw
        screen.fill(PURPLE)
        
        #achievements
        screen.blit(achievementsTitleText, (CENTREX-achievementsTitleWidth/2, CENTREY-achievementsTitleHeight/2-275))
        if page == 0:
            achievementBox(CENTREX-50-350, CENTREY-200, 0)
            achievementBox(CENTREX-50-350, CENTREY-100, 1)
            achievementBox(CENTREX-50-350, CENTREY, 2)
            achievementBox(CENTREX-50-350, CENTREY+100, 3)
            achievementBox(WIDTH-50-350, CENTREY-200, 4)
            achievementBox(WIDTH-50-350, CENTREY-100, 5)
            achievementBox(WIDTH-50-350, CENTREY, 6)
            achievementBox(WIDTH-50-350, CENTREY+100, 7)
        elif page == 1:
            achievementBox(CENTREX-50-350, CENTREY-200, 8)
            achievementBox(CENTREX-50-350, CENTREY-100, 9)
            achievementBox(CENTREX-50-350, CENTREY, 10)
            achievementBox(CENTREX-50-350, CENTREY+100, 11)
            achievementBox(WIDTH-50-350, CENTREY-200, 12)
            achievementBox(WIDTH-50-350, CENTREY-100, 13)
            achievementBox(WIDTH-50-350, CENTREY, 14)
    #defining achievement boxes (if the player achieves a certain level, a check mark will appear in the checkbox)

        #back button
        back(PURPLE)

        #next page
        if page == 0:
            pageText = pageOne
        else:
            pageText = pageTwo
        pageWidth = pageText.get_rect().width
        pageHeight = pageText.get_rect().height
        screen.blit(pageText, (740, 620))

        #update
        pygame.display.update()
        
        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        #click buttons
        for event in pygame.event.get():
            #back
            if event.type == pygame.MOUSEBUTTONDOWN and (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                achievementMenu = False
                levelSelection()

            #next page
            if event.type == pygame.MOUSEBUTTONDOWN and (740 < x < 740+pageWidth) and (620 < y < 620+pageHeight):
                if page == 0:
                    page = 1
                else:
                    page = 0
        #if statements for back button, next page, mouse position, and clicking buttons.

def levelSelection():
    #variables
    global levelNumber
    global highScoreList
    levelNumber = 0
    levelMenu = True

    #level list
    levelList = ["Candyland", "Shelter", "Fireflies",
                 "No Money", "Pay No Mind", "Jackpot",
                 "Echolands", "Me and You", "Idols",
                 "Elevatia", "One Off Mind", "Crave You",
                 "Challenger", "The Seven Seas", "Screamroom"]

    #artist list
    artistList = ["Tobu", "Porter Robinson & Madeon", "Owl City - Said the Sky Remix",
                  "Galantis", "Madeon", "TheFatRat",
                  "Zyzyx", "succducc", "Virtual Riot",
                  "Bossfight", "Hatsune Miku and Gumi", "Flight Facilities - Adventure Club Remix",
                  "Creo", "F-777", "Xtrullor"]
    
    #fire image (used to show the level of difficulty)
    fire = pygame.image.load("Images/Fire.png").convert_alpha()
    fireWidth = fire.get_rect().width
    fireHeight = fire.get_rect().height

    #"Press Space to scroll through levels"
    spaceText = body.render("Press SPACE to scroll through levels", True, WHITE, PURPLE)
    spaceWidth = spaceText.get_rect().width
    spaceHeight = spaceText.get_rect().height
    
    #while loop
    while levelMenu == True:
        #level text
        levelText = title.render(levelList[levelNumber], True, WHITE, DARKPURPLE)
        levelWidth = levelText.get_rect().width
        levelHeight = levelText.get_rect().height

        #artist text
        artistText = body.render(artistList[levelNumber], True, WHITE, DARKPURPLE)
        artistWidth = artistText.get_rect().width
        artistHeight = artistText.get_rect().height

        #high score text
        highScoreText = headingTwo.render(str(highScoreList[levelNumber])+"%", True, WHITE, PURPLE)
        highScoreWidth = highScoreText.get_rect().width
        highScoreHeight = highScoreText.get_rect().height

        #draw
        screen.fill(PURPLE)
        #rect
        pygame.draw.rect(screen, DARKPURPLE, (CENTREX-650/2, CENTREY-300/2, 650, 300), 0)
        #texts
        screen.blit(levelText, (CENTREX-levelWidth/2, CENTREY-levelHeight/2-50))
        screen.blit(artistText, (CENTREX-artistWidth/2, CENTREY-artistHeight/2+25))
        screen.blit(spaceText, (CENTREX-spaceWidth/2, CENTREY-spaceHeight/2-250))
        #high score
        screen.blit(highScoreText, (CENTREX-highScoreWidth/2, CENTREY-highScoreHeight/2+200))
        #back
        back(PURPLE)
        #achievements
        screen.blit(achievementsText, (WIDTH-achievementsWidth-25, 620))
        
        #difficulty
        screen.blit(fire, (CENTREX-fireWidth/2-75*2, CENTREY-fireHeight/2+100))
        if levelNumber > 2:
            screen.blit(fire, (CENTREX-fireWidth/2-75, CENTREY-fireHeight/2+100))
        if levelNumber > 5:
            screen.blit(fire, (CENTREX-fireWidth/2, CENTREY-fireHeight/2+100))
        if levelNumber > 8:
            screen.blit(fire, (CENTREX-fireWidth/2+75, CENTREY-fireHeight/2+100))
        if levelNumber > 11:
            screen.blit(fire, (CENTREX-fireWidth/2+75*2, CENTREY-fireHeight/2+100))
            

        #get mouse position
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        pygame.display.update()
        
        #click buttons
        for event in pygame.event.get():
            #switch level
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                levelNumber = (levelNumber+1)%15
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #load level
                if (CENTREX-600/2 < x < CENTREX-600/2+600) and (CENTREY-300/2 < y < CENTREY-300/2+300):
                    levelMenu = False
                    loadLevel(levelNumber)

                #back
                elif (30 < x < 30+backWidth) and (620 < y < 620+backHeight):
                    levelMenu = False
                    playerSelection()

                #achievements
                elif (WIDTH-achievementsWidth-25 < x < WIDTH-25) and (620 < y < 620+achievementsHeight):
                    achievements()
#defining the level selection
#end of while lop if the level selection == True
                    
#------------------------------------------------------------------------------------------
#PAUSE MENU
#------------------------------------------------------------------------------------------
def pausemenu():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            condition = True
            #pause music
            pygame.mixer.music.pause()
            #display pause
            pygame.draw.rect(screen, RED, (690, 5, pauseWidth+20, pauseHeight+10))
            screen.blit(pauseText, (700, 10))
            pygame.display.update()
            while condition == True:
                event = pygame.event.wait()
                #unpause
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and condition == True:
                    condition = False
                    pygame.mixer.music.unpause()
                #restart
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and condition == True:
                    condition = False
                    loadLevel(levelNumber)
                #quit
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and condition == True:
                    condition = False
                    menuMusic()
                    levelSelection()
#defining the pause menu (if the player wants to pause in the middle of a game).
#------------------------------------------------------------------------------------------
#GAME OVER
#------------------------------------------------------------------------------------------
def death():
    #death sound effects
    if deathNumber == 0:
        death = pygame.mixer.Sound('Music/Death.wav')
    elif deathNumber == 1:
        death = pygame.mixer.Sound('Music/Pelo.wav')
    elif deathNumber == 2:
        death = pygame.mixer.Sound('Music/Wilhelm.wav')
    elif deathNumber == 3:
        death = pygame.mixer.Sound('Music/Oof.wav')
    death.play()

#defining the death sound effects
    
def gameOver(win, progressOne, progressTwo, totalLength):
    condition2 = True
    #win
    if win == True:
        #high score
        highScoreList[levelNumber] = 100.0

        #store scores into a file
        scoreFile = open(scoreFileName,'w')
        for i in range(0, len(highScoreList)):
            scoreFile.write(str(highScoreList[i])+" ")
        scoreFile.close()
        
        #trophy
        trophy = pygame.image.load('Images/Trophy.png').convert_alpha()
        trophyWidth = trophy.get_rect().width
        trophyHeight = trophy.get_rect().height
    #if the player winds, a screen will display
        
        while condition2 == True:
            #draw
            screen.fill(GOLD)
            screen.blit(winText, (CENTREX-winWidth/2, CENTREY-winHeight/2-250))
            screen.blit(trophy, (CENTREX-trophyWidth/2, CENTREY-trophyHeight/2+50))
            if numPlayers == 1:
                screen.blit(icon.image, (CENTREX-70/2, CENTREY-70/2-100))
            elif numPlayers == 2:
                screen.blit(icon.image, (CENTREX-70/2-50, CENTREY-70/2-100))
                screen.blit(icon2.image, (CENTREX-70/2+50, CENTREY-70/2-100))
                #texts
                screen.blit(playerOneGoldText, (CENTREX-playerOneGoldWidth/2-150, 650-playerOneGoldHeight/2-75))
                screen.blit(playerTwoGoldText, (CENTREX-playerTwoGoldWidth/2+150, 650-playerTwoGoldHeight/2-75))

            #progress bar
            if numPlayers == 1:
                progress(progressOne, 0, GOLD, 0, 0)
            elif numPlayers == 2:
                progress(progressOne, totalLength, GOLD, -100, 0)
                progress(progressTwo, totalLength, GOLD, 100, 0)
                
            #showing the percent of the game that has been completed

            pygame.display.update()

            for event in pygame.event.get():
                #restart
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r and condition2 == True:
                    condition2 = False
                    loadLevel(levelNumber)
                #quit
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and condition2 == True:
                    condition2 = False
                    menuMusic()
                    levelSelection()
            #Pressing "r" to restart the game and "q" to quit the game
    #lose
    else:
        #high score
        if (round((float(progressOne)/(WIDTH+totalLength+350) * 100), 1) >= highScoreList[levelNumber]):
            highScoreList[levelNumber] = round((float(progressOne)/(WIDTH+totalLength+350) * 100), 1)

            #store scores into a file
            scoreFile = open(scoreFileName,'w')
            for i in range(0, len(highScoreList)):
                scoreFile.write(str(highScoreList[i])+" ")
            scoreFile.close()
            
        #storing high scores
            
        #if two players
        if (numPlayers == 2) and (round((float(progressTwo)/(WIDTH+totalLength+350) * 100), 1) >= highScoreList[levelNumber]):
            highScoreList[levelNumber] = round((float(progressTwo)/(WIDTH+totalLength+350) * 100), 1)

            #store scores into a file
            scoreFile = open(scoreFileName,'w')
            for i in range(0, len(highScoreList)):
                scoreFile.write(str(highScoreList[i])+" ")
            scoreFile.close()
            
        #storing high scores for two players

        #music
        if autoRetry == False:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Music/Heartless-Journey.mp3')
            pygame.mixer.music.play()
        #playing music
            
        while condition2 == True:
            #draw
            screen.fill(PURPLE)
            screen.blit(gameText, (CENTREX - gameWidth/2, CENTREY - gameHeight/2 - 200))
            if numPlayers == 2:
                #texts
                screen.blit(playerOneText, (CENTREX-playerOneWidth/2-150, 650-playerOneHeight/2-75))
                screen.blit(playerTwoText, (CENTREX-playerTwoWidth/2+150, 650-playerTwoHeight/2-75))

            #progress bar
            if numPlayers == 1:
                progress(progressOne, totalLength, PURPLE, 0, 0)
            elif numPlayers == 2:
                progress(progressOne, totalLength, PURPLE, -100, 0)
                progress(progressTwo, totalLength, PURPLE, 100, 0)
            
            pygame.display.update()

            #auto-retry
            if autoRetry == True:
                condition2 = False
                pygame.time.delay(200)
                loadLevel(levelNumber)

            for event in pygame.event.get():
                #restart
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r and condition2 == True:
                    condition2 = False
                    loadLevel(levelNumber)
                #quit
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and condition2 == True:
                    condition2 = False
                    menuMusic()
                    levelSelection()
            #if auto Retry is True or conditions are False
                    
#------------------------------------------------------------------------------------------
#GAMEPLAY
#------------------------------------------------------------------------------------------
#progress
def progress(stepX, totalLength, groundColour, progressX, progressY):
    progress = str(round((float(stepX)/(WIDTH+totalLength+350) * 100), 1))+'%'
    progressText = headingTwo.render(progress, True, WHITE, groundColour)
    progressWidth = progressText.get_rect().width
    progressHeight = progressText.get_rect().height
    screen.blit(progressText, (CENTREX-progressWidth/2+progressX, 650-progressHeight/2+progressY))
#defining progress
    
#gameplay
def level(level, numHazards, hazardSize, length, hazardSpeed, iconSpeed, screenColour, groundColour, hazardColour, finishColour):
    #music
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Music/"+level+".mp3")
    pygame.mixer.music.play()

    #variables
    global icon
    icon.y = 530
    iconDead = False
    if numPlayers == 2:
        global icon2
        icon2.y = 530
        iconDeadTwo = False
    totalLength = length * hazardSpeed
    stepX = 0
    clock = pygame.time.Clock()

    #list of hazards
    hazardList = []
    for i in range(numHazards):
        randX = randint(WIDTH+150, WIDTH+totalLength)
        randY = randint(10, 530)
        hazardList.append([randX, randY])

    #initialize background
    backgroundImg = pygame.image.load("Images/"+level+".png").convert_alpha()
    backgroundWidth = backgroundImg.get_rect().width
    backgroundHeight = backgroundImg.get_rect().height

    #while loop
    while True:
        #draw
        screen.fill(screenColour)

        #background
        screen.blit(backgroundImg, (CENTREX - backgroundWidth/2, CENTREY - backgroundHeight/2))

        #ground
        pygame.draw.rect(screen, groundColour, (0, 600, WIDTH, 200))

        #icons
        if iconDead == False:
            icon.draw()
        if numPlayers == 2:
            if iconDeadTwo == False:
                icon2.draw()

        #finish line
        finishX = WIDTH+totalLength+500-stepX
        pygame.draw.rect(screen, finishColour, (finishX, 0, 50, 600))
        
        #one player
        if numPlayers == 1 and finishX <= 150:
            progressOne = WIDTH+350
            gameOver(True, progressOne, 0, totalLength)
            
        #two players
        if numPlayers == 2 and finishX <= 150:
            #player one is alive
            if iconDead == False:
                progressOne = WIDTH+350+totalLength
            #player two is alive
            if iconDeadTwo == False:
                progressTwo = WIDTH+350+totalLength
            gameOver(True, progressOne, progressTwo, totalLength)
        
        #progress bar
        progress(stepX, totalLength, groundColour, 0, 0)
        
        #hazards
        for i in range(len(hazardList)):
            hazard = Hazard()
            hazard.x = hazardList[i][0]
            hazard.y = hazardList[i][1]
            hazard.w = hazardSize
            hazard.h = hazardSize
            hazard.draw(hazardColour)
            
            #move hazards
            hazardList[i][0] -= hazardSpeed

            #check collision
            if numPlayers == 1:
                if hazard.checkCollision(icon.x, icon.y, icon.w, icon.h):
                    iconDead = True
                    progressOne = stepX
                    death()
                    gameOver(False, progressOne, 0, totalLength)
            elif numPlayers == 2:
                if hazard.checkCollision(icon.x, icon.y, icon.w, icon.h) and iconDead == False:
                    iconDead = True
                    progressOne = stepX
                    death()
                if hazard.checkCollision(icon2.x, icon2.y, icon2.w, icon2.h) and iconDeadTwo == False:
                    iconDeadTwo = True
                    progressTwo = stepX
                    death()
                if iconDead == True and iconDeadTwo == True:
                    gameOver(False, progressOne, progressTwo, totalLength)

        #pause menu
        pausemenu()
        
        #controls
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and iconDead == False:
            icon.shipUp(iconSpeed)
        if numPlayers == 2:
            if keys[pygame.K_UP] and iconDeadTwo == False:
                icon2.shipUp(iconSpeed)

        #gravity
        icon.gravity(iconSpeed/2)
        if numPlayers == 2:
            icon2.gravity(iconSpeed/2)

        #update
        stepX += hazardSpeed
        pygame.display.update()
        clock.tick(200)
    #end of while loop (True)
#defining level
        
#------------------------------------------------------------------------------------------
#MAIN PROGRAM
#------------------------------------------------------------------------------------------
#variable initialization
deathNumber = 0
autoRetry = False
checkmark = pygame.image.load('images/Checkmark.png').convert_alpha()
scoreFileName = 'Files/Save.txt'

#save file
with open(scoreFileName, 'r') as scoreFile:
    highScoreList = []
    for i in scoreFile.read().split():
        highScoreList.append(float(i))

#main menu (display)
mainmenu(True)
