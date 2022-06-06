from turtle import Screen
import numpy as np
import pygame
import sys
from random import randint

pygame.init()

# creating the window
cell=20
celln=20
screen=pygame.display.set_mode((cell*celln,cell*celln))

#creating food
fpos=[randint(0,18)*20,randint(0,18)*20]
food=pygame.Rect(fpos[0],fpos[1],cell,cell)

#creating and moving the snake
#pos is the snake position
pos=[[160,200],[180,200],[200,200]]
d=[-20,0] #direction that gets added or subtracted to/from the head position
def move_l():
    pos.pop(-1)
    npos=np.add(pos[0],d) #pos[0] is the head
    pos.insert(0,npos)
    global fpos
    global food
    if np.array_equal(npos,fpos): #making the snake munch
        print('point')
        fpos=[randint(0,18)*20,randint(0,18)*20]
        food=pygame.Rect(fpos[0],fpos[1],cell,cell)
        pos.insert(0,npos) #growing the snake
        
        
    
    


def drawsnake():
     for i in pos:
          pygame.draw.rect(screen,('black'),pygame.Rect(i[0],i[1],cell,cell))
     

#creating a timer
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,180)

#controlling fps
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            move_l()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                d=[-20,0]
            if event.key == pygame.K_UP:
                d=[0,-20]               
            if event.key == pygame.K_DOWN:
                d=[0,20]
            if event.key == pygame.K_RIGHT:
                d=[20,0]
            
    screen.fill('gold')
    pygame.draw.rect(screen,('red'),food)
    drawsnake()
    pygame.display.update()
    clock.tick(60)
