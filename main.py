# Reference: Coding with Russ
# https://www.youtube.com/watch?v=Vlolidaoiak&list=PLjcN1EyupaQnvpv61iriF8Ax9dKra-MhZ&index=1&t=43s&ab_channel=CodingWithRuss
# Game Creator: Steven Theron
# 11 October 2023

import pygame
from Fighter import Fighter
from Healthbar import Healthbar

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

# Game Variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
clicked = False

# Fonts
font = pygame.font.SysFont("Times New Roman", 26)

# Colors
red = (255, 0, 0)
green = (0, 255, 0)

# Load Assets
background_img = pygame.image.load("assets/background.png").convert_alpha()
panel_img = pygame.image.load("assets/icons/panel.png").convert_alpha()
sword_img = pygame.image.load("assets/icons/sword.png").convert_alpha()


# Create Fighters
knight = Fighter(screen,200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(screen,550, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(screen,700, 270, 'Bandit', 20, 6, 1)

bandit_list = [bandit1, bandit2]

# Create Health bars
knight_health_bar = Healthbar(screen, 100, SCREEN_HEIGHT - BOTTOM_PANEL + 40,
                              knight.hp, knight.max_hp, red, green)
bandit1_health_bar = Healthbar(screen, 500, SCREEN_HEIGHT - BOTTOM_PANEL + 40, bandit1.hp, bandit1.max_hp, red, green)
bandit2_health_bar = Healthbar(screen, 500, SCREEN_HEIGHT - BOTTOM_PANEL + 100, bandit2.hp, bandit2.max_hp, red, green)

# bandit_health_bar_list = [bandit1_health_bar, bandit2_health_bar]


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_screen(img, x, y, is_panel):
    screen.blit(img, (x, y))  # destination 0,0 is the top left corner.

    if is_panel:
        # Show Knight stats
        draw_text(f'{knight.name} HP: {knight.max_hp}',
                  font, red, 100, SCREEN_HEIGHT - BOTTOM_PANEL + 10)

        bandit_panel_x = 500
        bandit_panel_y = (SCREEN_HEIGHT - BOTTOM_PANEL + 10)
        # Show Bandit stats
        # for bandito in bandit_list:
        #     draw_text(f'{bandito.name} {bandit_list.index(bandito)} HP: {bandito.max_hp}',
        #               font, red, bandit_panel_x, bandit_panel_y)
        for count, i in enumerate(bandit_list):
            draw_text(f'{i.name} {count} HP: {i.max_hp}',
                      font, red, bandit_panel_x, (bandit_panel_y + count * 60))


run = True
while run:

    clock.tick(fps)     # Fix processing rate to the fps variable.

    # Draw screen
    draw_screen(background_img, 0, 0, False)  # draw bg
    draw_screen(panel_img, 0, SCREEN_HEIGHT - BOTTOM_PANEL, True)  # draw panel

    knight_health_bar.draw(knight.hp)

    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)

    # Draw Fighters
    knight.update()
    knight.draw()

    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    # *** Control player actions ***
    # Reset action variables
    attack = False
    potion = False
    target = None

    pygame.mouse.set_visible(True)  # Show mouse
    mouse_pos = pygame.mouse.get_pos()

    # Mouse Icon Image
    for count, bandit in enumerate(bandit_list):
        if bandit.rect.collidepoint(mouse_pos):
            pygame.mouse.set_visible(False)     # Hide mouse
            screen.blit(sword_img, mouse_pos)   # Show Sword
            if clicked:
                attack = True
                target = bandit_list[count]

    # Player action
    if knight.alive:
        if current_fighter == 1:    # if 1 then it's the knights turn.
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                # Look for player action
                # Attack
                if attack and target is not None:
                    knight.attack(target)
                    current_fighter += 1    # It's now the next fighters turn.
                    action_cooldown = 0

    # Enemy action
    for count, bandit in enumerate(bandit_list):    # used enumerate to keep a running count.
        if current_fighter == 2 + count:    # Select the next fighter
            if bandit.alive:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    # Attack!
                    bandit.attack(knight)
                    current_fighter += 1
                    action_cooldown = 0
            else:
                current_fighter += 1

    # If all fighters have had a turn, then reset.
    if current_fighter > total_fighters:
        current_fighter = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()
            
pygame.quit()
