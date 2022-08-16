#Name: Dinith Nawaratne
#Purpose: Creating a Target Shooting game
#Date Started: 10/12/2018
#Date Finished: 17/01/2019

import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()
pygame.mixer.init()

#Set the frame rate
FPS = 30

#Create clock object
fpsClock = pygame.time.Clock()

#Setting the mouse to be unvisible
pygame.mouse.set_visible(False)

#Set the size of the display window in pixels
Display_Surface = pygame.display.set_mode((1200, 800))

#Change the caption of the display window
pygame.display.set_caption("Target Shooting")

#Set the tuples for the colours
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Dark_Green = ( 0, 128, 0)
Blue = (0, 0, 255)
Purple = (128, 0, 128)
Aqua = (0, 255, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Navy_Blue = (0, 0, 128)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
Yellow = (255, 255, 0)
Olive = (128, 128, 0)
Maroon = (128, 0, 0)
Beige = (193, 154, 107)
Brown = (150, 75, 0)

#Loading the gun images
gunImage = pygame.image.load("gun.png")
gunImage = pygame.transform.scale(gunImage, (410, 300))
gun1Image = pygame.image.load("gun1.png")
gun1Image = pygame.transform.scale(gun1Image, (410, 300))
gun2Image = pygame.image.load("gun2.png")
gun2Image = pygame.transform.scale(gun2Image, (410, 300))
gun3Image = pygame.image.load("gun3.png")
gun3Image = pygame.transform.scale(gun3Image, (410, 300))
gun4Image = pygame.image.load("gun4.png")
gun4Image = pygame.transform.scale(gun4Image, (410, 300))
gun5Image = pygame.image.load("gun5.png")
gun5Image = pygame.transform.scale(gun5Image, (410, 300))
gun6Image = pygame.image.load("gun6.png")
gun6Image = pygame.transform.scale(gun6Image, (410, 300))
gun7Image = pygame.image.load("gun7.png")
gun7Image = pygame.transform.scale(gun7Image, (410, 300))
gun8Image = pygame.image.load("gun8.png")
gun8Image = pygame.transform.scale(gun8Image, (410, 300))
gun9Image = pygame.image.load("gun.png")
gun9Image = pygame.transform.scale(gun9Image, (410, 300))
gun10Image = pygame.image.load("gun.png")
gun10Image = pygame.transform.scale(gun10Image, (410, 300))
gun11Image = pygame.image.load("gun11.png")
gun11Image = pygame.transform.scale(gun11Image, (410, 300))
gun12Image = pygame.image.load("gun12.png")
gun12Image = pygame.transform.scale(gun12Image, (410, 300))

#Set the initial x and y coordinates for the gun images
gunx = 395
guny = 640
gun1x = 395
gun1y = 600
gun2x = 395
gun2y = 600
gun3x = 395
gun3y = 600
gun4x = 395
gun4y = 600
gun5x = 395
gun5y = 600
gun6x = 395
gun6y = 600
gun7x = 395
gun7y = 600
gun8x = 395
gun8y = 600
gun9x = 395
gun9y = 657.5
gun10x = 395
gun10y = 675
gun11x = 395
gun11y = 600
gun12x = 395
gun12y = 600

#Setting the position of the targets
targetImage = pygame.image.load("target.png")
targetImage = pygame.transform.scale(targetImage, (100, 100))
targety = random.randint(250, 500)
targetx = random.randint(100, 1000)

#Initially setting the background to the thumbnail size on the location screen
grasslandsImage = pygame.image.load("grasslands.jpg")
grasslandsThumbnail = pygame.transform.scale(grasslandsImage, (300, 200))
ruinsImage = pygame.image.load("ruins.jpg")
ruinsThumbnail = pygame.transform.scale(ruinsImage, (300, 200))
desertImage = pygame.image.load("desert.jpg")
desertThumbnail = pygame.transform.scale(desertImage, (300, 200))
spaceImage = pygame.image.load("space.jpg")
spaceThumbnail = pygame.transform.scale(spaceImage, (300, 200))

#Resizing the image to take up the whole screen
grasslandsImage = pygame.transform.scale(grasslandsImage, (1200, 800))
ruinsImage = pygame.transform.scale(ruinsImage, (1200, 800))
desertImage = pygame.transform.scale(desertImage, (1200, 800))
spaceImage = pygame.transform.scale(spaceImage, (1200, 800))

#Initializing variables
hit = 0
mag = 30
ammo = 210
reload_bar = 0
score = 0
timer = 0
seconds = 30
game_run = False
Colour = Black
target_time = 0
start_game = False
reload_time = False
pausecolour = Black
game_pause = False
run_time = False
restart_game = False

#Reading and writing the hiscore to a text file
f = open("hi-score.txt", "r")
hiscore = f.readline()
hiscore = int(hiscore)
f.close()

#Creating the crosshair for the mouse
reticle = pygame.image.load("crosshair.png")
reticle = pygame.transform.scale(reticle, (25, 25))

#Creating the fonts
start_font = pygame.font.SysFont("comicsans", 50)
game_font = pygame.font.SysFont("comicsans", 42)
game_start = pygame.font.SysFont("comicsans", 150)
end_font = pygame.font.SysFont("comicsans", 75)
pause_font = pygame.font.SysFont("comicsans", 55)
instructions_font = pygame.font.SysFont("comicsans", 33)

#Loading in the sound effects & music
reload_sound = pygame.mixer.Sound("reload.wav")
gunshot_sound = pygame.mixer.Sound("gun shot.wav")
emptymag_sound = pygame.mixer.Sound("empty mag.wav")

while True: #Main loop
  
    while game_run == False:
        
        #Setting the mouse visible
        pygame.mouse.set_visible(True)

        #Playing the music
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("ending.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.15)
        
        Display_Surface.fill(Black)
        pygame.draw.rect(Display_Surface, Gray, (40, 40, 320, 270), 0)
        Display_Surface.blit(grasslandsThumbnail, (50, 50))
        pygame.draw.rect(Display_Surface, Gray, (840, 40, 320, 270), 0)
        Display_Surface.blit(ruinsThumbnail, (850, 50))
        pygame.draw.rect(Display_Surface, Gray, (40, 490, 320, 270), 0)
        Display_Surface.blit(desertThumbnail, (50, 500))
        pygame.draw.rect(Display_Surface, Gray, (840, 490, 320, 270), 0)
        Display_Surface.blit(spaceThumbnail, (850, 500))
        
        #Displaying the text on the start-up screen
        grasslands_text = start_font.render("Grasslands", True, White)
        Display_Surface.blit(grasslands_text, (97, 262))
        desert_text = start_font.render("Desert", True, White)
        Display_Surface.blit(desert_text, (136, 713))
        ruins_text = start_font.render("Ruins", True, White)
        Display_Surface.blit(ruins_text, (954, 262))
        space_text = start_font.render("Space", True, White)
        Display_Surface.blit(space_text, (944, 713))
        location = game_start.render("Location", True, Red)
        Display_Surface.blit(location, (375, 350))
        instructions = pause_font.render("INSTRUCTIONS", True, White)
        Display_Surface.blit(instructions, (450, 500))
        instructions1 = instructions_font.render("- Choose your location", True, White)
        Display_Surface.blit(instructions1, (420, 560))
        instructions2 = instructions_font.render("- You will have 30 seconds to", True, White)
        Display_Surface.blit(instructions2, (420, 590))
        instructions3 = instructions_font.render("  shoot as many targets as you can", True, White)
        Display_Surface.blit(instructions3, (420, 621))
        instructions4 = instructions_font.render("- Don't miss the target or else you'll", True, White)
        Display_Surface.blit(instructions4, (420, 655))
        instructions5 = instructions_font.render("  lose points", True, White)
        Display_Surface.blit(instructions5, (422, 682))
        instructions6 = instructions_font.render("- Good luck and have fun :)", True, White)
        Display_Surface.blit(instructions6, (420, 715))
        pygame.draw.rect(Display_Surface, Yellow, (395, 480, 410, 280), 6)
        #NEED TO WRITE TARGET SHOOTING AS A TITLE
            
        for event in pygame.event.get():    #Setting the background based on what rectangle background the playerclicked
            if event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if (40 < mouseX < 360) and (40 < mouseY < 310):
                    background = grasslandsImage
                    game_run = True
                    Colour = Black
                    pausecolour = Gray
                if (840 < mouseX < 1160) and (40 < mouseY < 310):
                    background = ruinsImage
                    game_run = True
                    Colour = White
                    pausecolour = Gray
                if (40 < mouseX < 360) and (490 < mouseY < 760):
                    background = desertImage
                    game_run = True
                    Colour = Black
                    pausecolour = Gray
                if (840 < mouseX < 1160) and (490 < mouseY < 760):
                    background = spaceImage
                    game_run = True
                    Colour = Yellow
                    pausecolour = Gray

            if event.type == QUIT:    #Check if user closes window
                    pygame.quit()
                    sys.exit()
                    
            #Update the display window
            pygame.display.update()

            #Check frame rate
            fpsClock.tick(FPS)                      
            
    while game_run == True:

        while start_game == False:  #Displays click to start until the player clicks
            
            #Setting the background
            Display_Surface.blit(background, (0, 0))

            #Displaying the gun on the screen
            Display_Surface.blit(gunImage, (gunx, guny))

            start = game_start.render("Click to Start", True, Colour)
            Display_Surface.blit(start, (280 , 340))

            #Stopping the music
            pygame.mixer.music.stop()

            for event in pygame.event.get():    #If the player clicks, the game starts
                if event.type == MOUSEBUTTONDOWN:
                    start_game = True
                    run_time = True

                if event.type == QUIT:    #Check if user closes window
                    pygame.quit()
                    sys.exit()
            
            #Update the display window
            pygame.display.update()

            #Check frame rate
            fpsClock.tick(FPS)

        while start_game == True:   #Starting the actual game

            if seconds > 0: #While the timer is greater than 0, run the game

                #Setting the mouse to be invisible
                pygame.mouse.set_visible(False)
                
                #Setting the background
                Display_Surface.blit(background, (0, 0))            
                
                #Setting High Score
                if score > hiscore:
                    hiscore = score

                #Stopping the music
                pygame.mixer.music.stop()
                
                #Creating the timer, so that they have 30 seconds, and reduce by 1 each second
                if run_time == True:
                    timer += (1/30)
                    if timer >= 1:
                        seconds -= 1
                        timer = 0

                #Determining what happens when you restart
                if restart_game == True:
                    start_game = False
                    mag = 30
                    ammo = 210
                    seconds = 30
                    hit = 0
                    score = 0
                    pygame.mouse.set_visible(True)    
                    game_pause = False
                    targety = random.randint(250, 500)                                   
                    targetx = random.randint(100, 1000)
                    restart_game = False
                    gunx = 395
                    guny = 640
                
                #Drawing the target on-screen
                Display_Surface.blit(targetImage, (targetx, targety))

                #Creating a pause button
                pygame.draw.rect(Display_Surface, pausecolour, (1160, 5, 35, 35), 0)
                pygame.draw.rect(Display_Surface, White, (1166, 12, 8, 23), 0)
                pygame.draw.rect(Display_Surface, White, (1180, 12, 8, 23), 0)

                if game_pause == False:
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouseX, mouseY = pygame.mouse.get_pos()
                            mag -= 1 
                            if mag >= 0 and reload_bar == 0:
                                #Creating the collision with the targets
                                if (targetx + 2 < mouseX < targetx + 98) and (targety + 2 < mouseY < targety + 98):   
                                    hit += 1                                                                                                       
                                    score += 75
                                    targety = random.randint(250, 500)                                   
                                    targetx = random.randint(100, 1000)
                                    gunshot_sound.play()

                                elif not((1160 < mouseX < 1195) and (5 < mouseY < 40)):       #Reduces the score by a random number from 10 to 30 if you miss the target
                                    score -= random.randint(10,30)
                                    gunshot_sound.play()

                            if mag < 0:
                                mag = 0
                                emptymag_sound.play()

                            #If you click the pause button
                            if (1160 < mouseX < 1195) and (5 < mouseY < 40):
                                if mag == 0:
                                    mag = 0
                                elif mag > 0:
                                    mag += 1
                                game_pause = True
                                pygame.mouse.set_visible(True)

                        if event.type == pygame.KEYDOWN:    #Allowing you to reload whenever you want, even if your not out of bullets
                            if event.key == K_r and mag < 30:
                                reload_time = True
                                reload_sound.play()
                            if event.key == K_ESCAPE:
                                game_pause = True
                                
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit() 

                if reload_time == True:
                    reload_bar += 10
                    if reload_bar >= 200:
                        reload_bar = 0
                        ammo = ammo + mag - 30
                        reload_time = False
                        mag = 30

                if ammo < 0:
                    ammo = 0

                if score < 0:
                    score = 0

                if game_pause == True:       #While the game is paused
                    run_time = False
                    pygame.mouse.set_visible(True)
                    pygame.draw.rect(Display_Surface, pausecolour, (500, 112.5, 200, 100), 0)
                    resumetext = pause_font.render("Resume", True, White)
                    Display_Surface.blit(resumetext, (525, 145))
                    pygame.draw.rect(Display_Surface, pausecolour, (500, 237.5, 200, 100), 0)
                    restarttext = pause_font.render("Restart", True, White)
                    Display_Surface.blit(restarttext, (533, 270))
                    pygame.draw.rect(Display_Surface, pausecolour, (500, 362.5, 200, 100), 0)
                    changetext = pause_font.render("Change", True, White)
                    Display_Surface.blit(changetext, (526, 377))
                    locationtext = pause_font.render("Location", True, White)
                    Display_Surface.blit(locationtext, (520, 415))
                    pygame.draw.rect(Display_Surface, pausecolour, (500, 487.5, 200, 100), 0)
                    quittext = pause_font.render("Quit", True, White)
                    Display_Surface.blit(quittext, (555, 520))
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouseX, mouseY = pygame.mouse.get_pos()
                            if ((1160 < mouseX < 1195) and (5 < mouseY < 40)) or ((500 < mouseX < 700) and (112.5 < mouseY < 212.5)):   #If you resume
                                game_pause = False
                                run_time = True
                                pygame.mixer.music.pause()
                                targety = random.randint(250, 500)                                   
                                targetx = random.randint(100, 1000)
                            if (500 < mouseX < 700) and (237.5 < mouseY < 337.5):   #If you restart
                                restart_game = True
                            if (500 < mouseX < 700) and (362.5 < mouseY < 462.5):
                                game_run = False
                                game_pause = False
                                restart_game = True
                            if (500 < mouseX < 700) and (487.5 < mouseY < 587.5):
                                pygame.quit()
                                sys.exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                game_pause = False
                                run_time = True
                                targety = random.randint(250, 500)                                   
                                targetx = random.randint(100, 1000)
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()


                #Making the gun move
                if game_pause == False:
                    mouseX,mouseY = pygame.mouse.get_pos()
                    if (395 < mouseX < 805) and (mouseY < 800 and mouseY > 500):
                        gunx = mouseX - 180
                        gun = gunImage
                        Display_Surface.blit(gun, (gunx, guny))
                    elif (395 < mouseX < 805) and (mouseY < 500 and mouseY > 400):
                        gun9x = mouseX - 180
                        gun = gun9Image
                        Display_Surface.blit(gun, (gun9x, gun9y))
                    elif (395 < mouseX < 805) and (mouseY < 400 and mouseY > 0):
                        gun10x = mouseX - 180
                        gun = gun10Image
                        Display_Surface.blit(gun, (gun10x, gun10y))
                    elif (0 < mouseX < 395) and (mouseY < 800 and mouseY > 600):
                        gun11x = mouseX + 15
                        gun = gun11Image
                        Display_Surface.blit(gun, (gun11x, gun11y))
                    elif (0 < mouseX < 395) and (mouseY < 600 and mouseY > 500):
                        gun1x = mouseX + 15
                        gun = gun1Image
                        Display_Surface.blit(gun, (gun1x, gun1y))
                    elif (0 < mouseX < 395) and (mouseY < 500 and mouseY > 400):
                        gun2x = mouseX + 15
                        gun = gun2Image
                        Display_Surface.blit(gun, (gun2x, gun2y))
                    elif (0 < mouseX < 395) and (mouseY < 400 and mouseY > 300):
                        gun3x = mouseX + 15
                        gun = gun3Image
                        Display_Surface.blit(gun, (gun3x, gun3y))
                    elif (0 < mouseX < 395) and (mouseY < 300 and mouseY > 0):
                        gun8x = mouseX + 15
                        gun = gun8Image
                        Display_Surface.blit(gun, (gun8x, gun8y))
                    elif (805 < mouseX < 1200) and (mouseY < 300 and mouseY > 0):
                        gun4x = mouseX - 425
                        gun = gun4Image
                        Display_Surface.blit(gun, (gun4x, gun4y))
                    elif (805 < mouseX < 1200) and (mouseY < 400 and mouseY > 300):
                        gun5x = mouseX - 425
                        gun = gun5Image
                        Display_Surface.blit(gun, (gun5x, gun5y))
                    elif (805 < mouseX < 1200) and (mouseY < 500 and mouseY > 400):
                        gun6x = mouseX - 425
                        gun = gun6Image
                        Display_Surface.blit(gun, (gun6x, gun6y))
                    elif (805 < mouseX < 1200) and (mouseY < 600 and mouseY > 500):
                        gun7x = mouseX - 425
                        gun = gun7Image
                        Display_Surface.blit(gun, (gun7x, gun7y))
                    elif (805 < mouseX < 1200) and (mouseY < 800 and mouseY > 600):
                        gun12x = mouseX - 425
                        gun = gun12Image
                        Display_Surface.blit(gun, (gun12x, gun12y))
               
                #Printing the words, score, etc. on the screen
                text = game_font.render("Targets Hit: " + str(hit), True, Colour)
                Display_Surface.blit(text, (9, 5))
                scoretext = game_font.render("Score: " + str(score), True, Colour)
                Display_Surface.blit(scoretext, (10, 48))
                hiscoretext = game_font.render("Hi-Score: " + str(hiscore), True, Colour)
                Display_Surface.blit(hiscoretext, (10, 90))
                timetext = start_font.render("Time Left: " + str(seconds), True, Colour)
                Display_Surface.blit(timetext, (350, 5))
                if reload_bar == 0:
                    if (mag > 0 and ammo >= 0) or (mag <= 0 and ammo <= 0) and reload_bar == 0:
                        ammotext = game_font.render("Ammo: " + str(mag) + "/" + str(ammo), True, Colour)
                        Display_Surface.blit(ammotext, (850, 5))
                    if mag <= 0 and ammo > 0 and reload_bar == 0:
                        reloadtext = game_font.render('PRESS "R" TO RELOAD', True, Colour)
                        Display_Surface.blit(reloadtext, (750, 5))
                elif reload_bar != 0:
                    pygame.draw.rect(Display_Surface, Colour, (850, 7, reload_bar, 20), 0)                       

                #Creating a crosshair for the mouse as long as the mouse is not hovering over the pause button or not in the pause menu
                mouseX, mouseY = pygame.mouse.get_pos()
                if game_pause == False:
                    if not((1160 < mouseX < 1195) and (5 < mouseY < 40)) and game_pause == False:
                        Display_Surface.blit(reticle, (mouseX - 12.5, mouseY - 12.5))
                    else:
                        pygame.mouse.set_visible(True)
                
                #Update the display window
                pygame.display.update()

                #Check frame rate
                fpsClock.tick(FPS)

            if seconds <= 0:    #When the seconds reach 0, the game over screen pops-up

                #Setting the background to black
                Display_Surface.fill(Black)

                #Setting the mouse visible
                pygame.mouse.set_visible(True)

                #Determining what happens when you restart
                if restart_game == True:
                    start_game = False
                    mag = 30
                    ammo = 210
                    seconds = 30
                    hit = 0
                    score = 0
                    pygame.mouse.set_visible(True) 
                    game_pause = False
                    targety = random.randint(250, 500)                                   
                    targetx = random.randint(100, 1000)
                    restart_game = False
                    gunx = 395
                    guny = 640

                if not pygame.mixer.music.get_busy():   #Playing thhe music
                    pygame.mixer.music.load("ending.wav")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.15)

                pygame.draw.rect(Display_Surface, Gray, (487.5, 482.5, 225, 100), 0)
                pygame.draw.polygon(Display_Surface, White, [(25, 80), (90, 130), (90, 30)], 0)
                changetext = pause_font.render("Change", True, Green)
                Display_Surface.blit(changetext, (109.4, 39))
                locationtext = pause_font.render("Location", True, Green)
                Display_Surface.blit(locationtext, (105, 82))
                playagaintext = pause_font.render("Play Again", True, White)
                Display_Surface.blit(playagaintext, (502.5, 515))
                pygame.draw.rect(Display_Surface, Gray, (487.5, 607.5, 225, 100), 0)
                quittext = pause_font.render("Quit", True, White)
                Display_Surface.blit(quittext, (552.5, 640))
                scoretext = end_font.render("Your final score was: " + str(score), True, White)
                Display_Surface.blit(scoretext, (293, 300))
                hiscoretext = end_font.render("The hi-score is: " + str(hiscore), True, White)
                Display_Surface.blit(hiscoretext, (373, 380))
                endtext = game_start.render("Time's Up", True, Yellow)
                Display_Surface.blit(endtext, (358, 123))

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if (487.5 < mouseX < 712.5) and (482.5 < mouseY < 582.5):
                            restart_game = True
                        if (25 < mouseX < 90) and (30 < mouseY < 130):
                            game_run = False
                            restart_game = True
                        if (487.5 < mouseX < 712.5) and (607.5 < mouseY < 707.5):
                            f = open("hi-score.txt", "w")   #Writing the hi-score to a text file
                            f.write(str(hiscore))
                            f.close()
                            pygame.quit()
                            sys.exit()
                    if event.type == QUIT:
                        f = open("hi-score.txt", "w")   #Writing the hi-score to a text file
                        f.write(str(hiscore))
                        f.close()
                        pygame.quit()
                        sys.exit()
                
                #Update the display window
                pygame.display.update()

                #Check frame rate
                fpsClock.tick(FPS)
