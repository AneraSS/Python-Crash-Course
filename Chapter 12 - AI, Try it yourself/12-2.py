# Game Character
# Find a bitmap image of a game character you like or convert an image to a bitmap.
# Make a class that draws the character at the center of the screen and match the background
# color of the image ot the background color of the screen, or vice versa.

import pygame
pygame.display.init()

width, height = 600, 400
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Whippet')

bg_color = (255,113,184)
screen.fill(bg_color)

image = pygame.image.load('images/whippet2.png')    # importing image
image = pygame.transform.scale(image, (150, 150))     # defining image size

x = width/3
y = height/3

screen.blit(image, (x,y))               # show what (image) and where (coordinates) on screen using blit()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False