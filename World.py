import pygame, sys
#exit the program
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

#defining the display
WIDTH = 800
HEIGHT = 600
half_HEIGHT = HEIGHT/2
half_WIDTH = WIDTH/2
AREA = WIDTH *HEIGHT

#initialise display
pygame.init()
CLOCK=pygame.time.Clock()
DS=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Python Game")
FPS=500

#defining the colors used in the game
BLACK = (0,0,0,255)
WHITE = (255,255,255,255)
#path for the background image
#convert so that the background is the same as the display surface
Bm= pygame.image.load("mountains.png").convert()
#getting the width and height of the background image
BmWidth,BmHeight = 800,600
#sidescrolling so we only need width
stageWidth = BmWidth
stagePosX = 0
#starts the stage scrolling only if the players X pods is greater than StartScrollPosX and less than then the width of the stage-
StartScrollingPosX = half_WIDTH

#player
circleRaduis = 25
circlePosX = circleRaduis

playerPosX = circleRaduis
playerPosY = 585
#starting velocity so a positive/negative value is added depending on the direction
playerVelocity = 0
#the main game loop
while True:
    events()
    #returns the element of the key that was pressed by the user
    k = pygame.key.get_pressed()
    if k[pygame.K_RIGHT]:
        playerVelocity = 1
    elif k[pygame.K_LEFT]:
        playerVelocity = -1
    else:
        playerVelocity = 0
    #whatever pressed is added to the players X position
    playerPosX+= playerVelocity
    #creating boundries
    if playerPosX > stageWidth - circleRaduis:
        playerPosX = stageWidth-circleRaduis

    if playerPosX < circleRaduis:
        playerPosX = circleRaduis

    else:
        stagePosX += -playerVelocity

    pygame.draw.circle(DS, WHITE, (playerPosX, playerPosY - circleRaduis), circleRaduis, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)