# Reference: Coding with Russ
# https://www.youtube.com/watch?v=Vlolidaoiak&list=PLjcN1EyupaQnvpv61iriF8Ax9dKra-MhZ&index=1&t=43s&ab_channel=CodingWithRuss
# Game Creator: Steven Theron
# 11 October 2023

import pygame
from Fighter import Fighter

pygame.init()

# FPS
clock = pygame.time.Clock()
fps = 60

# Game window
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle Quest")

# Load Assets
background_img = pygame.image.load("assets/background.png").convert_alpha()
panel_img = pygame.image.load("assets/icons/panel.png").convert_alpha()


# Create Fighters
knight = Fighter(screen,200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(screen,550, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(screen,700, 270, 'Bandit', 20, 6, 1)

bandit_list = [bandit1, bandit2]


def draw_screen(img, x, y):
    screen.blit(img, (x, y))  # destination 0,0 is the top left corner.


run = True
while run:

    clock.tick(fps)     # Fix processing rate to the fps variable.

    # Draw screen
    draw_screen(background_img, 0, 0)  # draw bg
    draw_screen(panel_img, 0, SCREEN_HEIGHT - BOTTOM_PANEL)  # draw panel

    # Draw Fighters
    knight.update()
    knight.draw()

    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
            
pygame.quit()
