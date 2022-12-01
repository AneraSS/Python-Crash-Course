#  12-4: Rocket
# Make a game that begins with a rocket in the center of the screen.
# Allow the player to move the rocket up, down, left, or right using the four arrow keys.
# Make sure the rocket never moves beyond any edge of the screen.


# initialize pygame
import pygame
import sys

pygame.display.init()

# set game window
width, height = 600, 400
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Moving rocket')

bg_color = (44,64,83)

# add image
rocket = pygame.image.load('images/rocket.png')
rocket = pygame.transform.scale (rocket, (100,100))

# show image in center of the screen
# transform image to rectangle and use it as such
rocket_rect = rocket.get_rect()
rocket_rect.center = screen.get_rect().center

# initialize rocket's flags
moving_right = False
moving_left = False
moving_up = False
moving_down = False


# run the game
def run_game():
    while True:
        check_events()
        update_rocket()
        update_screen()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)


def check_keydown_events(event):
    """Respond to key pressed down"""
    global moving_right, moving_left, moving_up, moving_down

    if event.key == pygame.K_RIGHT:
        moving_right = True
    elif event.key == pygame.K_LEFT:
        moving_left= True
    elif event.key == pygame.K_UP:
        moving_up = True
    elif event.key == pygame.K_DOWN:
        moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event):
    """Respond to key released up"""
    global moving_right, moving_left, moving_up, moving_down

    if event.key == pygame.K_RIGHT:
        moving_right = False
    elif event.key == pygame.K_LEFT:
        moving_left= False
    elif event.key == pygame.K_UP:
        moving_up = False
    elif event.key == pygame.K_DOWN:
        moving_down = False

ship_speed = 1.5

def update_rocket():
    if moving_right and rocket_rect.right < screen.get_rect().right:
        rocket_rect.x += ship_speed
    if moving_left and rocket_rect.left > screen.get_rect().left:
        rocket_rect.x -= ship_speed
    if moving_up and rocket_rect.top > screen.get_rect().top:
        rocket_rect.y -= ship_speed
    if moving_down and rocket_rect.bottom < screen.get_rect().bottom:
        rocket_rect.y += ship_speed

def update_screen():
    screen.fill(bg_color)
    screen.blit(rocket, rocket_rect)

    pygame.display.flip()


run_game()