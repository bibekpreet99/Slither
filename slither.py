import pygame
import time
import random

pygame.init()


# VARIABLES

width = 800
height = 600
block_size= 16
appleThickness = 24
FPS = 16
direction = 'right'

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

# GAME WINDOW
screen = pygame.display.set_mode((width,height))
gameTitle = pygame.display.set_caption("Slither")
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)
pygame.display.update()

#COLORS
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 125, 0)
light_blue = (132, 112, 255)


clock = pygame.time.Clock()

pygame.display.update()

#SELF DEFINED FUNCTIONS
img = pygame.image.load('snakehead.png')
img1 = pygame.image.load('apple.png')


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit() 

        
        screen.fill(white)
        message_to_screen("Welcome to Slither", red, -100, "large")
        message_to_screen("The objective of the game is to eat the fresh red apples"
                          , black,
                          -30)
        message_to_screen("The more apples you eat the longer you get",
                          black,
                          10)
        message_to_screen("If you cross the edges or eat yourself you die!!!",
                          black,
                          50)
        message_to_screen("Press C to play and Q to quit and P to pause",
                          black,
                          180)

        pygame.display.update()
        clock.tick(15)



def pause():

    paused = True

    message_to_screen("Paused", red, -100, "large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            #screen.fill(white)

            clock.tick(5)

def snake(block_size, snakeList):

    if direction == 'right':
        head = pygame.transform.rotate(img, 270)

    if direction == 'left':
        head = pygame.transform.rotate(img, 90)

    if direction == 'up':
        head = img

    if direction == 'down':
        head = pygame.transform.rotate(img, 180)    
    
    
    screen.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)

    elif size == "medium":
        textSurface = medfont.render(text, True, color)

    elif size == "large":    
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def score(score):
    text = smallfont.render("Score: "+ str(score), True, black)
    screen.blit(text, [0,0])

def apple_coord():
        applex = round(random.randrange(0, width-appleThickness))#/10)*10
        appley = round(random.randrange(0, height-appleThickness))#/10)*10
        return applex,appley

def message_to_screen(msg, color, y_displace = 0, size= "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (width/2) , (height/2)+ y_displace
    screen.blit(textSurf, textRect)


    #screen_text = font.render(msg, True, color)
    #screen.blit(screen_text, [width/2,height/2])

#  MAIN GAME LOOP
def gameLoop():
    global direction
    direction = "right"

    running = True
    gameOver = False
    lead_x = width/2
    lead_y = height/2

    snakeList = []
    snakeLenght = 1

    lead_x_change = 10
    lead_y_change = 0


    applex,appley = apple_coord()
    
    while running:

        if gameOver == True:
            #screen.fill(white)
            message_to_screen("Game Over", red, -50, size ="large")
            message_to_screen(" Press C to Play again Press Q to quit", black, 50, size = "small")
            text = smallfont.render("Your Score: "+ str(snakeLenght-1), True, black)
            screen.blit(text, [width/2-100,height/2+ 100])
            pygame.display.update()


        # GAME OVER LOOP
        while gameOver == True:
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        gameOver = False

                    if event.key ==  pygame.K_c:
                        gameLoop()

             # KEYS


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   direction = 'left'
                   lead_x_change = -block_size
                   lead_y_change = 0

               elif event.key == pygame.K_RIGHT:
                   direction = 'right'
                   lead_x_change = +block_size
                   lead_y_change = 0

               elif event.key == pygame.K_UP:
                   direction = 'up'
                   lead_y_change = -block_size
                   lead_x_change = 0

               elif event.key == pygame.K_DOWN:
                   direction = 'down'
                   lead_y_change = block_size
                   lead_x_change = 0

               elif event.key == pygame.K_p:
                   pause()
           # LOGIC


        if lead_x >= width or lead_x <0 or lead_y >= height or lead_y < 0:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        screen.fill((153, 255, 248))
       # pygame.draw.rect(screen, red, [applex, appley, block_size, block_size])
       

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLenght:
                del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        snake(block_size, snakeList)
        screen.blit(img1, (applex, appley))

        score(snakeLenght -1)
        pygame.display.update()


        if lead_x > applex and lead_x < applex + appleThickness or lead_x + block_size > applex and lead_x + block_size < applex + appleThickness:
            if lead_y > appley and lead_y < appley + appleThickness :
                applex,appley = apple_coord()
                snakeLenght += 1

            elif lead_y + block_size > appley and lead_y + block_size < appley + appleThickness:
                applex,appley = apple_coord()
                snakeLenght += 1 



        clock.tick (FPS)

    pygame.quit()
    quit()
game_intro()
gameLoop()
