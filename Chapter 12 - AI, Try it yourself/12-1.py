# Blue Sky
# Pygame window with a blue bg.

# import pygame
import pygame

# initialize all the pygame modules
pygame.init()

# create a window object
width,height = 600, 400
    # initialize a screen for display
window = pygame.display.set_mode((width,height))

# set the caption of the screen
pygame.display.set_caption('Blue sky background')

# adding bg color
bg_color = (173,216,230)
    # fill the display with the color specified
window.fill(bg_color)

# update the display using flip
pygame.display.flip()

# Variable to keep our game loop running, otherwise it would be presented for 1s
running = True

# game loop ("while") and for-loop through the event queue
while running:
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:   # get events from the queue
            running = False             # close the program: pygame.quit