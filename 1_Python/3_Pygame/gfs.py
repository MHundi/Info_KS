import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen= pygame.display.set_mode([1920,1050], pygame.FULLSCREEN)

x=100
y=700
speed =10
jump_var = -16

def draw():
    pygame.draw.rect(screen, color=(0,200,255), rect=(0,0,1920,800))
    pygame.draw.rect(screen, color=(0,200,0), rect=(0,800,1920,300))
    pygame.draw.rect(screen, color=(255,0,0), rect=(x,y,50,100))
    
def obstacle(x_obstacle, y_obstacle):
    if  x>= x_obstacle and x <=x_obstacle + 50 and y==700:
        sys.exit()
    if  x+99>= x_obstacle and x+99 <=x_obstacle + 50 and y==700:
        sys.exit()
    if  x+99>= x_obstacle and x <=x_obstacle + 50 and y==700:
        sys.exit()
    pygame.draw.rect(screen, color=(255,0,0), rect=(x_obstacle, y_obstacle, 50, 50))
    
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        press = pygame.key.get_pressed()
        
    if press[pygame.K_ESCAPE]:
        sys.exit()
            
    if press[pygame.K_d]:
        x=x+speed
        
    if press[pygame.K_a]:
        x=x-speed
            
    if jump_var >=-15:
        n=1
        if jump_var<0:
            n=-1
        y -= (jump_var**2)*0.17*n
        jump_var -= 1
        
    if press[pygame.K_SPACE] and jump_var==-16:
            jump_var =15 
        
    draw()
    obstacle(1000, 800)
    pygame.display.update()
    clock.tick(60) #60 times per second the code will bie executed
    
    
    

