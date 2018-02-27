import pygame
from Player import *
from Platform import *
#initilise pygame
pygame.init()
#creating a window
window = pygame.display.set_mode((800,600))
#caption
pygame.display.set_caption("Game Window")
gravity =-0.5
#color
black = (0,0,0)
Red = (50,0,0)

#defining the fps
clock = pygame.time.Clock()
player = Player(0,0)
#25 columns, 19 rows
#using a list to create the level, the grid (800/32) so working with 25 blocks and 19 blocks(rows)
Level = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],

]
#the vlaue of the blocks is stored in this list
blocklist = []
#a for loop the range counts from 0-25, going through each coloumn
#the x goes through each zeros and if its one it will create a block.
#x32 because its 32 pixels
for y in range(0,len(Level)):
    for x in range(0,len(Level[y])):
        if(Level[y][x]==1):
            blocklist.append(platform(x*32,y*32))



#loops as long as game loop is true
GameIsRunning = True
while GameIsRunning:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            GameIsRunning = False
    #simple background color
    window.fill(Red)
    #calling this will take the values from blocklist and create a rectangle in that position
    for block in blocklist:
        block.render(window)
    #gravity so the player is always falling down
    player.update(gravity, blocklist)
    #renders what is in the window,this case its the player rect with the position(x,y) and (W,H)
    player.render(window)
    #setting the fps
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
