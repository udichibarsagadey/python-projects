from re import T
from turtle import done
import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((500,500))
done = False
is_purple = True
x = 10
y = 10

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_purple = not is_purple
  
    pressed = pygame.key.get_pressed()  
    if pressed[pygame.K_UP]:y -=2
    if pressed[pygame.K_DOWN]:y +=2
    if pressed[pygame.K_LEFT]:x -=2
    if pressed[pygame.K_RIGHT]:x +=2
  
    if is_purple:  
        color = (0, 128, 255)  
    else:   
        color = (128, 0, 128)  
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))  
  
    pygame.display.flip()